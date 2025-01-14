import json
import requests
import telebot
import time

def call_llama(model, prompt, stream=False):
    url = 'http://localhost:11434/api/generate' 
    data = {
        'model': model,
        'prompt': prompt,
        'stream': stream
    } 

    json_data = json.dumps(data)
    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        return response.json()
    else:
        return f'Error: {response.status_code}'

TELEGRAM_TOKEN = 'YOUR_BOT_TOKEN' 
bot = telebot.TeleBot(TELEGRAM_TOKEN)

active_chats = set()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    active_chats.add(message.chat.id)
    bot.reply_to(message, '👋 Hi! I am your Llama chatbot. How can I assist you today?')

@bot.message_handler(commands=['quit'])
def quit_bot(message):
    markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, '😥 Are you sure?', reply_markup=markup)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    btn_yes = telebot.types.KeyboardButton('YES ✅')
    btn_no = telebot.types.KeyboardButton('NO ❌')
    markup.add(btn_yes, btn_no)
    bot.send_message(message.chat.id, '🔮 Please confirm:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'YES ✅')
def confirm_quit(message):
    bot.reply_to(message, '🙋 Goodbye! Ending the chat now.')
    active_chats.discard(message.chat.id)
    bot.send_message(message.chat.id, "🔙 You have been disconnected. To start a new chat, type /start.", reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(func=lambda message: message.text == 'NO ❌')
def cancel_quit(message):
    bot.send_message(message.chat.id, 'Returning to chat...', reply_markup=telebot.types.ReplyKeyboardRemove())
    send_welcome(message)

@bot.message_handler(commands=['help'])
def help_bot(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    btn_about = telebot.types.KeyboardButton('🗒️ about us 🗒️')
    btn_contact = telebot.types.KeyboardButton('📱 contact us 📱')
    btn_main_menu = telebot.types.KeyboardButton('🔙')
    markup.add(btn_about, btn_contact, btn_main_menu)
    bot.send_message(message.chat.id, '🤔 How can I help you?', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == '🗒️ about us 🗒️')
def about_us(message):
    bot.send_message(message.chat.id, '🗨️ This robot designed by Mehrdad Ourang and Llama3.2')

@bot.message_handler(func=lambda message: message.text.lower() == '📱 contact us 📱')
def contact_us(message):
    bot.send_message(message.chat.id, '📖 Name: Mehrdad Ourang\n📧 Email: mehrdadourang2@gmail.com\n☎️ Phone: 021-1452172\n🍾 Telegram : @MEHRDAD87ORG')

@bot.message_handler(func=lambda message: message.text.lower() == '🔙')
def main_menu(message):
    bot.send_message(message.chat.id, '😇 Returning to main menu...', reply_markup=telebot.types.ReplyKeyboardRemove())
    send_welcome(message)  

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.chat.id in active_chats:
        user_input = message.text
        response = call_llama('llama3.2', user_input)['response']
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "🤠 Please start the chat by typing /start.")

def main():
    while True:
        try:
            bot.polling(none_stop=True, timeout=600000)  
        except Exception as e:
            print(f"🔁 try again : {e}")
            time.sleep(4)  

if __name__ == '__main__':
    main()
