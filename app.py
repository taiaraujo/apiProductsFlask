from flask import jsonify

from config.marshmallow import ma
from config.database import db
from controllers.product import ProductList, Product
from server.server import server
from marshmallow.exceptions import ValidationError

api = server.api
app = server.app


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(ProductList, '/product')
api.add_resource(Product, '/product/<int:id>')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()