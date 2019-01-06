from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api, Resource
from controllers.IdentityController import GetIdentity, InsertIdentity, UpdateIdentity, DeleteIdentity
import utility
import os

load_dotenv()

app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS'] = False


class GetVersion(Resource):
    @staticmethod
    def get():
        return utility.give_response("00", os.getenv('APP_NAME'))

@app.errorhandler(404)
def page_not_found(e):
    return utility.give_response("01","THIS METHOD DOES NOT EXIST")


api.add_resource(GetVersion, '/')
api.add_resource(GetIdentity, '/getIdentity')
api.add_resource(InsertIdentity, '/insertIdentity')
api.add_resource(UpdateIdentity, '/updateIdentity/<int:id>')
api.add_resource(DeleteIdentity, '/deleteIdentity/<int:id>')

if __name__ == '__main__':
    app.run()
