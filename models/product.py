from config.database import db
from typing import List


class ProductModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    def __init__(self, sku, name, price):
        self.name = name
        self.sku = sku
        self.price = price

    def __repr__(self):
        return f'ProductModel(name={self.name}, sku={self.sku}, price={self.price})'

    def json(self):
        return {'name': self.name, 'sku': self.sku, 'price': self.price}

    @classmethod
    def find_all(cls) -> List["ProductModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id) -> "ProductModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

