from tinydb import TinyDB, Query
import csv

# db setting
db = TinyDB('db.json')



class Models:
    def __init__(self, **dic):
        self.number = dic['number']
        self.fullname = dic['fullname']
        self.nickname = dic['nickname']
        self.fightsong = dic['fightsong']
        self.tag = dic['tag']
    
    def genericsongs(self):
        pass


# import csvfile
with open('DeNA_players.csv', 'r') as csvf:
    csv.reader(csvf,)


db.insert_multiple()