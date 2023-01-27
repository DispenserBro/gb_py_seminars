from random import randint

from telegram import Bot, Update
from telegram.ext import (Updater,
                          CommandHandler,
                          CallbackContext,
                          MessageHandler,
                          Filters)


TOKEN = '5860877963:AAFnDA9JL9bXIrjEHcgTisEJQw3zQVxvKXs'

bot = Bot(TOKEN)
updater = Updater(TOKEN)
dp = updater.dispatcher


def start(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Hello!')


def rand(update: Update, context: CallbackContext):
    rand_number = randint(1, 10000)

    context.bot.send_message(update.effective_chat.id, f'Your random number: {rand_number}')


def default(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, f'I don\'t know such command as: {update.effective_message.text}')


def hello_ru(update: Update, context: CallbackContext):
    text = update.effective_message.text

    if 'прив' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'Хелло май френд!')


start_handler = CommandHandler('start', start)
rand_handler = CommandHandler('random', rand)
hello_ru_handler = MessageHandler(Filters.text, hello_ru)
default_cmd_handler = MessageHandler(Filters.command, default)



dp.add_handler(start_handler)
dp.add_handler(rand_handler)
dp.add_handler(default_cmd_handler)
dp.add_handler(hello_ru_handler)

if __name__ == "__main__":
    updater.start_polling()
    updater.idle()
