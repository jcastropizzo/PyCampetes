from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from db.models import Product

command_name = 'list_products'

description = 'Lista los productos disponibles y sus precios'

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    products = Product.select()
    response_text = []
    for prd in products:
        response_text.append(str(prd))
    response_text = '\n'.join(response_text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)


command_handler = CommandHandler(command_name, handler)