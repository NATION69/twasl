import os
from keep_alive import keep_alive

try:
    import pyTelegramBotAPI
except:
    os.system('pip install pyTelegramBotAPI')
from telebot import types

import telebot

token = '1985783210:AAEC8qjDdOkJqTkwgqvHXxXI7OjqtMe9hgc' # توكن
sudo = 1782851959 # ايدي
bot = telebot.TeleBot(token)

def ex_id(id):
    result = False
    file = open('users.txt', 'r')
    for line in file:
        if line.strip() == id:
            result = True
    file.close()
    return result


@bot.message_handler(commands=['start'])
def start(message):
    file = open('users.txt', 'r')
    li = len(file.readlines())
    file.close()
    if message.chat.type == 'private':
        idu = message.from_user.id
        f = open('users.txt', 'a')
        if (not ex_id(str(idu))):
            f.write(f"{idu}\n")
            f.close()
    file = open('users.txt', 'r')
    markup_inline = types.InlineKeyboardMarkup()
    sendfile = types.InlineKeyboardButton(text='ملف ايدي الاعضاء', callback_data='file')
    brod = types.InlineKeyboardButton(text='برودكاست 📢', callback_data='brod')
    count = types.InlineKeyboardButton(text=f'عدد الاعضاء {li}', callback_data='count')
    emt = types.InlineKeyboardButton(text=f'', callback_data='emt')
    sendmm = types.InlineKeyboardButton(text=f'ارسال رساله لشخص معين 📩', callback_data='smo')
    markup_inline.row_width = 2
    markup_inline.add(sendfile, brod, count, emt, sendmm)
    li = len(file.readlines())
    idd = message.from_user.id

    if idd == sudo:
        bot.send_message(sudo, text='Hi boss\n\n'
                         , parse_mode='markdown', reply_markup=markup_inline)

    bot.send_message(message.chat.id, text='*Hi (: 🤍*\n\n'
                                           f'مرحبا بك في بوت تواصل Spark ارسل رسالتك وسوف يتم الرد عليك في اسرع وقت'
                     , parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'file':
        files(call.message)

    elif call.data == 'brod':
        mesgg = bot.send_message(call.message.chat.id, text='*ارسل رسالتك 📢 :*', parse_mode='markdown')
        bot.register_next_step_handler(mesgg, broddd)
    elif call.data == 'smo':
        mesgg = bot.send_message(call.message.chat.id, text='*ارسل الايدي :*', parse_mode='markdown')
        bot.register_next_step_handler(mesgg, iddd)


def iddd(message):
    iddd = message.text
    length = bot.send_message(message.chat.id, text='🔢 ارسل الرسال 📩 :')
    bot.register_next_step_handler(length, smo, iddd)


def smo(message, iddd):
    msg = message.text
    bot.send_message(iddd, text=f'*{msg}*', parse_mode='markdown')
    bot.send_message(sudo, text=f'*تم ارسال الرساله بنجاح ✅*', parse_mode='markdown')


def broddd(message):
    mes = message.text
    readd = open('users.txt', 'r')
    for idu in readd:
        bot.send_message(idu, text=f'*{mes}*', parse_mode='markdown')
    bot.send_message(sudo, text=f'*تم عمل اذاعة بنجاح ✅*', parse_mode='markdown')


def files(message):
    file = open('users.txt', 'rb')
    bot.send_document(message.chat.id, file)


@bot.message_handler(func=lambda m: True)
def check(message):
    username = message.from_user.username
    msg = message.text
    idd = message.from_user.id
    bot.forward_message(sudo, message.chat.id, message.message_id)
    bot.send_message(sudo, text='*{}*'.format(msg), parse_mode='markdown')
    bot.send_message(sudo, text=f'*Text : {msg}\n\n*'
                                f'*Username : @{username}*\n\n'
                                f'ID : `{idd}`', parse_mode='markdown')
    bot.send_message(message.chat.id, text=f'*تم ارسال الرساله بنجاح ✅*', parse_mode='markdown')


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as ex:
        telebot.logger.error(ex)
keep_alive()
