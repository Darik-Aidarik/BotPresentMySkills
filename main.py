# My tg bot for presentation my skills
# hello

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("")

link_hh = 'https://spb.hh.ru/resume/3edb82d0ff0d1485690039ed1f5438644b6c59'
resume_pdf = 'resume_september_2025.pdf'
resume_docx = 'resume_september_2025.docx'

# Создание inline клавиатуры
markup = InlineKeyboardMarkup()
markup.row_width = 2
markup.add(
    InlineKeyboardButton("Хочу резюме в pdf формате", callback_data="pdfButton"),
    InlineKeyboardButton("Хочу резюме в docx формате", callback_data="docxButton")
)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я бот для того, чтобы прислать вам резюме моего создателя! Тыкай на кнопку и получай моё резюме!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def echo_message(message):
    bot.send_message(message.chat.id, "Привет! Я бот для того, чтобы прислать вам резюме моего создателя! Тыкай на кнопку и получай моё резюме!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def send_document(call):
    if call.data == "pdfButton":
        try:
            with open(f'{resume_pdf}', 'rb') as file:
                bot.send_document(call.message.chat.id, file, caption="Вот ваш файл в формате pdf!")
        except FileNotFoundError:
            bot.answer_callback_query(call.id, f"Файл не найден! Вот ссылка на hh в таком случае -> {link_hh}")
    elif call.data == "docxButton":
        try:
            with open(f'{resume_docx}', 'rb') as file:
                bot.send_document(call.message.chat.id, file, caption="Вот ваш файл в формате docx!")
        except FileNotFoundError:
            bot.answer_callback_query(call.id, f"Файл не найден! Вот ссылка на hh в таком случае -> {link_hh}")


bot.polling()