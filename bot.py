import logging
from telegram.ext import ApplicationBuilder
from config import TOKEN
from base import start_handler, echo_handler
from ejemplo import ejemplo_handler
from db.models import migrate, Product, ShoppingCart, ShoppingCartEntry

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    migrate()
    random_product = Product(name='Coso', price=15)
    random_product.save()
    random_cart = ShoppingCart(cart_holder='Pepito')
    random_cart.save()
    random_shopping_cart_entry = ShoppingCartEntry(cart=random_cart,product=random_product,quantity=1)
    random_shopping_cart_entry.save()

    print(Product.select().get().name)
    print(ShoppingCart.select().get())
    print(ShoppingCartEntry.select().get())
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(ejemplo_handler)

    application.run_polling()