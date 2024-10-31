from telebot import types

def language_buttons():
    markup = types.InlineKeyboardMarkup()
    button_ru = types.InlineKeyboardButton("Русский", callback_data="lang_ru")
    button_uz = types.InlineKeyboardButton("O'zbek", callback_data="lang_uz")
    markup.add(button_ru, button_uz)
    return markup

def register_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_phone = types.KeyboardButton("Отправить номер телефона", request_contact=True)
    button_location = types.KeyboardButton("Отправить локацию", request_location=True)
    markup.add(button_phone, button_location)
    return markup
