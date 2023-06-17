from aiogram import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item1 = types.KeyboardButton("/Препараты")
item2 = types.KeyboardButton("/Услуги")
markup.add(item1).add(item2)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item3 = types.KeyboardButton("/Кардиология")
item6 = types.KeyboardButton("/Генетика")
item5 = types.KeyboardButton("/Медосмотр")
item4 = types.KeyboardButton("/Стоматология")
item15 = types.KeyboardButton("/Меню")
markup2.add(item3).add(item4).add(item5).add(item6).add(item15)

markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item7 = types.KeyboardButton("/Врачи(стоматология)")
item8 = types.KeyboardButton("/Стоимость(стоматология)")
item17 = types.KeyboardButton("/Назад")
markup4.add(item7).add(item8).add(item17)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item9 = types.KeyboardButton("/Врачи(кардиология)")
item10 = types.KeyboardButton("/Стоимость(кардиология)")
markup3.add(item9).add(item10).add(item17)

markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item11 = types.KeyboardButton("/Врачи(медосмотр)")
item12 = types.KeyboardButton("/Стоимость(медосмотр)")
markup5.add(item11).add(item12).add(item17)

markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item13 = types.KeyboardButton("/Врачи(генетика)")
item14 = types.KeyboardButton("/Стоимость(генетика)")
markup6.add(item13).add(item14).add(item17)

markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup7.add(item1).add(item15)