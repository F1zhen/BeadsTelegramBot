import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6441987581:AAHrXPukocrqHP4RLUpZByMpDavWXnmhK2g')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Каталог', callback_data='Каталог')
    markup.add(btn1)
    btn2 = types.InlineKeyboardButton('Заказ украшения', callback_data='Заказ украшения')
    btn3 = types.InlineKeyboardButton('Заказ одежды', callback_data='Заказ одежды')
    btn4 = types.InlineKeyboardButton('Подбор украшения', callback_data='Подбор одежды')
    btn5 = types.InlineKeyboardButton('Выбор подарка', callback_data='Выбор подарка')
    btn6 = types.InlineKeyboardButton("Direct", callback_data='Direct')
    markup.row(btn2, btn3)
    markup.row(btn4, btn5)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)

@bot.callback_query_handler(func = lambda call: call.data == 'Каталог')
def callback_handler(call):
    bot.send_message(call.message.chat.id, 'Вы выбрали каталог. Вот ссылка на каталог: [Ваша ссылка]')


@bot.callback_query_handler(func = lambda call: call.data == 'Direct')
def callback_handler(call):
    markup = types.InlineKeyboardMarkup()
    webbrowser.open('https://www.instagram.com/direct/t/110412183687781')
    bot.reply_to(message,э reply_markup=markup)




@bot.message_handler(commands = ['start', 'main', 'hello'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Каталог', url='https://ya.zerocoder.ru/pgt-zarabotok-v-telegramme-na-botah-realnaya-vozmozhnost-zarabotat/'))
    webbrowser.open('https://open.spotify.com/')
    bot.reply_to(message, 'привет', reply_markup=markup)



@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Каталог', url = 'https://ya.zerocoder.ru/pgt-zarabotok-v-telegramme-na-botah-realnaya-vozmozhnost-zarabotat/')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото' , callback_data = 'delete' )
    btn3 = types.InlineKeyboardButton('изменить текст', callback_data='edit')
    markup.row(btn2, btn3)

    bot.reply_to(message, 'Спасибо за представленный пример', reply_markup=markup)


@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

bot.polling(none_stop=True)