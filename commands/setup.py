from telegram.ext import CommandHandler
from . import command_save_shopping_cart_entry as command_save_shopping_cart_entry
from . import command_list_products as command_list_products


commands = [command_list_products,
            command_save_shopping_cart_entry]


def setup_commands(application):
    help_text = []
    for c in commands:
        application.add_handler(CommandHandler(c.command_name, c.handler))
        help_text.append(f"/{c.command_name}: {c.description}")
    help_text = "\n\n".join(help_text)
    print('******************** HELPTEXT START')
    print(help_text)
    print('******************** HELPTEXT END')