# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import dao.CryptoDao
from webscrap import spanTest
from webscrap import siblingTest
from webscrap import wikiLinkTest
from wikiwebcrawl import *
from cryptoLevelCrawling import *
from persistJsonAssetFile import *
from ApiCall import *
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from dao import CryptoDao

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('action')
parser.add_argument('crypto')
parser.add_argument('date')


class Req(Resource):
    #curl http://localhost:5000/
    def get(self):
        return dao.CryptoDao.retrieveCryptoFromDB()

    #curl http://localhost:5000/ -X DELETE
    def delete(self, id,id2):
        args = parser.parse_args()
        pass

    #curl http://localhost:5000/ -X PUT
    def put(self):

        args = parser.parse_args()
        action = args["action"]
        asset="%"

        if args["crypto"]:
            asset = args["crypto"]
        date=args["date"]

        if action.upper() == 'RETRIEVE':
            return dao.CryptoDao.retrieveCryptoFromDB(crypto=asset,date=date)
        elif action.upper() == 'UPDATE':
            jsonFile = retrieveFullCoingecko(retrieveExtra=False, maxPage=10)
            persist(jsonFile)

api.add_resource(Req, '/')



if __name__ == '__main__':
    app.run(debug=True)

