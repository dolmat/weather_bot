
import telebot
import pyowm
from telebot.types import Message
from telebot import types

omw = pyowm.OWM('token', language="there_is_language")
bot = telebot.TeleBot('token')

users = set()

@bot.message_handler(content_types=['text'])
def send_echo(message: Message):
    observation = omw.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status(
    ) + "\n"
    answer += "Температура в районе " + str(round(temp)) + "\n\n"

    if temp <= 10:
        answer += "Очень холодно"
    elif 10 < temp < 20:
        answer += "Терпимо, накинь ветровку"
    else:
        answer += "Нормально, можно в футболке"

    bot.reply_to(message, answer)

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    sticker_id = 'CAADAgAD9QEAArJh9gP2aVyuvJNBwBYE'
    bot.send_sticker(message.chat.id, sticker_id)

@bot.message_handler(content_types=['text'])
def echo_test(message: Message):
    reply = str(message, answer)
    if message.from_user.id in users:
        reply += f" {message.from_user.id}, и снова привет!"
        bot.reply_to(message, reply)
        bot.send_message.from_user.id

@bot.inline_handler(lambda query: query.query)
def query_text(inline_query):
    print(inline_query)
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


bot.polling(none_stop=True)
