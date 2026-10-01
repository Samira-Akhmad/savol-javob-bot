import telebot
import wikipedia


TOKEN = '8991027156:AAFFgWqLO5frvFrK_SAXqkvhSO_F7Gui8Qo'
bot = telebot.TeleBot(TOKEN)

wikipedia.set_user_agent("MyTelegramBot/1.0 (contact@example.com)")

wikipedia.set_lang("uz")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello! Please ask your question:")


@bot.message_handler(func=lambda message: True)
def send_wiki_info(message):
    try:
        info = wikipedia.summary(message.text, sentences=3)
        bot.send_message(message.chat.id, info)
    finally:
        bot.send_message(message.chat.id, "Savolingiz uchun rahmat!")


bot.polling()