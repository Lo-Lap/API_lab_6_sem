from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('\U0001F4DA Главное меню')
b2 = KeyboardButton('\U00002795 Добавить напоминание')
b3 = KeyboardButton('\U0001F4C3 Текущие дела')
b4 = KeyboardButton('\U0001F4DC Выполненные дела')
kb_start.add(b1).add(b2).add(b3).add(b4)



