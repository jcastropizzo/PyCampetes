from peewee import *

db = SqliteDatabase('shop.db')
db.connect()

class Product(Model):
    id = IntegerField(primary_key = True)
    name = CharField()
    price = IntegerField()

    def __str__(self):
        return f'{self.name}: {self.price} morlacos'

    class Meta:
        database = db
        table_name = 'products'


class ShoppingCart(Model):
    id = IntegerField(primary_key = True)
    cart_holder = CharField()

    class Meta:
        database = db
        table_name = 'shopping_carts'


class ShoppingCartEntry(Model):
    id = IntegerField(primary_key = True)
    cart = ForeignKeyField(ShoppingCart, backref='entries')
    product = ForeignKeyField(Product, backref='entries')
    quantity = IntegerField()

    class Meta:
        database = db
        table_name = 'shopping_carts_x_products'

def migrate():
    db.create_tables([Product, ShoppingCart, ShoppingCartEntry])


def get_db_connection():
    return db