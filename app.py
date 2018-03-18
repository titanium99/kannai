"""# DeNA応援歌用Line Bot

## settings for start-app
0. start docker container // Write later!!
$ docker 

1. set env
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
from bottle import route, run, template
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

line_bot_api = LineBotApi('MY_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('MY_CHANNEL_SECRET')

@post('/callback')
def callback():
    pass

run(host='0.0.0.0', port=8081, debug=True)