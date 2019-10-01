import telebot
import pyowm

omw = pyowm.OWM('7c0bb0c14f5da7b74d25f7668ef00176', language="ru")
bot = telebot.TeleBot("447794786:AAHLQdR5Qo-T3XLtgFVUllhhoJsN0n_yM7Q")


@bot.message_handler(content_types=['text'])
def send_echo(message):
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

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)