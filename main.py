from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api, Resource
from controllers.AuthController import ChangePassword, VerifyLogin
from controllers.IdentityController import GetIdentity, InsertIdentity, UpdateIdentity, DeleteIdentity
from controllers.UserController import GetUser, InsertUser, UpdateUser, DeleteUser
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
    return utility.give_response("01", str(e))


api.add_resource(GetVersion, '/')
api.add_resource(GetIdentity, '/getIdentity')
api.add_resource(InsertIdentity, '/insertIdentity')
api.add_resource(UpdateIdentity, '/updateIdentity/<int:id_identity>')
api.add_resource(DeleteIdentity, '/deleteIdentity/<int:id_identity>')
api.add_resource(GetUser, '/getUser')
api.add_resource(InsertUser, '/insertUser')
api.add_resource(UpdateUser, '/updateUser/<int:sysuser_id>')
api.add_resource(DeleteUser, '/deleteUser/<int:sysuser_id>')
api.add_resource(ChangePassword, '/changePassword')
api.add_resource(VerifyLogin, '/verifyLogin')

if __name__ == '__main__':
    app.run()
