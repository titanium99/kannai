"""# DeNA応援歌用Line Bot

## settings for start-app
0. start docker container // Write later!!
$ docker 

1. set your machene env
$ MY_CHANNEL_ACCESS_TOKEN=''
$ MY_CHANNEL_SECRET=''

2. git clone https://github.com/titanium99/kannai

3. change directory 
$ cd kannnai

4. crate python env
$ python3 -m env botenv
$ source botenv/bin/activate

5. install library
$ pip install -r requirements.txt

6. start app
$ python app.py

# Todo
- write settings No.0
"""
import os, sys
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from tinydb import TinyDB, Query


db = TinyDB('dbs.json')
Song = Query()
app = Flask(__name__)


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)


line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route('/')
def index():
    return 'Hello Everyone.'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=searchsongs(event.message.text))
    )

def searchsongs(kwd):
    player = db.search(Song.fullname.matches(kwd))
    if len(player) == 1:
        return player[0]['fightsong']
    elif len(player) == 0:
        return '選手が見つかりません'
    else:
        names = ",".join([i['fullname'] for i in player])
        return "複数の選手が見つかりました\n{}".format(names)


if __name__ == '__main__':
    
    appenv = os.getenv('APP_ENV', None)

    if appenv == 'heroku':
        port = int(os.getenv('PORT', None))
    
    else:
        port = 8081
        
    app.run(host="0.0.0.0", port=port, debug=True)