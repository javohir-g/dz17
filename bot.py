import telebot
from database import init_db, save_user, save_contact, save_location
from buttons import language_buttons, register_buttons

bot = telebot.TeleBot('7927478236:AAEaWaz1v2rNK9W5Oc2cZ7PPRjDhaZZMUHk')
init_db()

USD_TO_UZS_RATE = 12000

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выберите язык:", reply_markup=language_buttons())

@bot.callback_query_handler(func=lambda call: call.data.startswith("lang_"))
def set_language(call):
    user_id = call.from_user.id
    language = "ru" if call.data == "lang_ru" else "uz"
    bot.send_message(call.message.chat.id, f"Вы выбрали язык: {language}. Пожалуйста, зарегистрируйтесь.", reply_markup=register_buttons())
    save_user(user_id, call.from_user.first_name, language)

@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    user_id = message.from_user.id
    save_contact(user_id, message.contact.phone_number)
    bot.send_message(message.chat.id, "Спасибо за номер телефона!")

@bot.message_handler(content_types=['location'])
def location_handler(message):
    user_id = message.from_user.id
    location = f"{message.location.latitude}, {message.location.longitude}"
    save_location(user_id, location)
    bot.send_message(message.chat.id, "Спасибо за локацию!")

bot.polling()
