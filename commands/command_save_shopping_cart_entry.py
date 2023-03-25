from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

command_name = 'save_shopping_cart_entry'

description = 'Guarda un elemento en el shopping cart'

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='gracias reyyyyy')

