from flask import Flask, Blueprint
from flask_restplus import Api


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.bluePrint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.bluePrint)
        self.app.register_blueprint(self.bluePrint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        self.product_ns = self.product_ns

        super().__init__()

    def product_ns(self):
        return self.api.namespace(name='Products', path='/')

    def run(self):
        self.app.run(debug=True)


server = Server()
