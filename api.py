from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS

from profanity_check import predict, predict_prob

app = Flask(__name__)
CORS(app)
api = Api(app)


class ProfanityChecker(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str, help='String to be tested')
        args = parser.parse_args()

        prob = predict_prob([args.text])

        return {'probability': prob[0]}

api.add_resource(ProfanityChecker, '/probability')

if __name__ == '__main__':
    app.run(debug=True)