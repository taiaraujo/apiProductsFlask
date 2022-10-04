from flask import request
from flask_restplus import Resource
from models.product import ProductModel
from schemas.product import ProductSchema
from server.server import server
from marshmallow import ValidationError


product_ns = server.product_ns

product_schema = ProductSchema()
product_list_schema = ProductSchema(many=True)


class ProductList(Resource):

    def get(self):
        return product_list_schema.dump(ProductModel.find_all()), 200

    def post(self):
        try:
            product_json = request.get_json()
            product_data = product_schema.load(product_json)
            product_data.save_to_db()
            return product_schema.dump(product_data), 201
        except ValidationError as error:
            return {'message': error.normalized_messages()}, 400


class Product(Resource):

    def get(self, id):
        product_data = ProductModel.find_by_id(id)
        if product_data:
            return product_schema.dump(product_data), 200
        return {'message': 'produto não encontrado'}, 404

    def delete(self, id):
        product_data = ProductModel.find_by_id(id)
        if product_data:
            product_data.delete_from_db()
            return '', 204
        return {'message': 'produto não encontrado'}, 404

    def put(self, id):
        try:
            product_data = ProductModel.find_by_id(id)
            product_json = request.get_json()
            if not product_data:
                return {'message': 'produto não encontrado'}, 404
            if product_schema.load(product_json):
                product_data.name = product_json["name"]
                product_data.sku = product_json["sku"]
                product_data.price = product_json["price"]
                product_data.save_to_db()
                return product_schema.dump(product_data), 200
        except ValidationError as error:
            return {'message': error.normalized_messages()}, 400




