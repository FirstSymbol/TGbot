from fileinput import close
from statistics import median
from sys import path_hooks

import telebot
import keyboards
from telebot import types
from telebot.types import Message, InputFile
from telebot import TeleBot
from telebot.types import CallbackQuery

def SendMainMenu(bot:TeleBot,chatID:int):
    bot.send_message(chat_id=chatID,
                     text='📋| Главное меню:',
                     reply_markup=keyboards.mainMenuKeyboard)

def EditMainMenu(bot:TeleBot,message:Message):
    if message.photo:
        chat = message.chat.id
        bot.delete_message(chat_id=message.chat.id,
                           message_id=message.message_id)
        SendMainMenu(bot,chat)
    else:
        bot.edit_message_text(text='📋| Главное меню:',
                              chat_id=message.chat.id,
                              message_id=message.message_id,
                              reply_markup=keyboards.mainMenuKeyboard)

def MessageNotFounded(bot:TeleBot,message:Message):
    bot.send_message(text='❌| Данная команда не найдена. Обратитесь к меню.', chat_id=message.chat.id, reply_markup=keyboards.ToMainMenuKeyboard())

def SendDostoprimPage1(bot: telebot.TeleBot, chatID: int):
    bot.send_message(text='🏛| Достопримечательности Бресткой области [1 / 4]',
                    chat_id=chatID,
                    reply_markup=keyboards.DostoprimPageKeybord(1))

def SendDostoprimPage2(bot: telebot.TeleBot, chatID: int):
    bot.send_message(text='🏛| Достопримечательности Бресткой области [2 / 4]',
                    chat_id=chatID,
                    reply_markup=keyboards.DostoprimPageKeybord(2))

def SendDostoprimPage3(bot: telebot.TeleBot, chatID: int):
    bot.send_message(text='🏛| Достопримечательности Бресткой области [3 / 4]',
                    chat_id=chatID,
                    reply_markup=keyboards.DostoprimPageKeybord(3))

def SendDostoprimPage4(bot: telebot.TeleBot, chatID: int):
    bot.send_message(text='🏛| Достопримечательности Бресткой области [4 / 4]',
                    chat_id=chatID,
                    reply_markup=keyboards.DostoprimPageKeybord(4))

def EditDostoprimPage1(bot: telebot.TeleBot, message: Message):
    if message.photo:
        chatID = message.chat.id
        bot.delete_message(message_id=message.message_id,
                           chat_id=message.chat.id)
        SendDostoprimPage1(bot, chatID)
    else:
        bot.edit_message_text(text='🏛| Достопримечательности Бресткой области [1 / 4]',
                              chat_id=message.chat.id,
                              message_id=message.message_id,
                              reply_markup=keyboards.DostoprimPageKeybord(1))

def EditDostoprimPage2(bot: telebot.TeleBot, message: Message):
    if message.photo:
        chatID = message.chat.id
        bot.delete_message(message_id=message.message_id,
                           chat_id=message.chat.id)
        SendDostoprimPage2(bot,chatID)
    else:
        bot.edit_message_text(text='🏛| Достопримечательности Бресткой области [2 / 4]',
                              chat_id=message.chat.id,
                              message_id=message.message_id,
                              reply_markup=keyboards.DostoprimPageKeybord(2))

def EditDostoprimPage3(bot: telebot.TeleBot, message: Message):
    if message.photo:
        chatID = message.chat.id
        bot.delete_message(message_id=message.message_id,
                           chat_id=message.chat.id)
        SendDostoprimPage3(bot, chatID)
    else:
        bot.edit_message_text(text='🏛| Достопримечательности Бресткой области [3 / 4]',
                              chat_id=message.chat.id,
                              message_id=message.message_id,
                              reply_markup=keyboards.DostoprimPageKeybord(3))

def EditDostoprimPage4(bot: telebot.TeleBot, message: Message):
    if message.photo:
        chatID = message.chat.id
        bot.delete_message(message_id=message.message_id,
                           chat_id=message.chat.id)
        SendDostoprimPage4(bot, chatID)
    else:
        bot.edit_message_text(text='🏛| Достопримечательности Бресткой области [4 / 4]',
                              chat_id=message.chat.id,
                              message_id=message.message_id,
                              reply_markup=keyboards.DostoprimPageKeybord(4))
    
def EditDostoprimObj(bot:TeleBot,message:Message,obj_id:int):
    global photo
    match obj_id:
        case 1:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='Брестская крепость\n\n'+
                                                  'Местоположение: город Брест\n\n'+
                                                  'Описание: Мемориальный комплекс и символ мужества советских солдат во время Великой Отечественной войны. Известна обороной 1941 года, когда защитники крепости мужественно противостояли немецким войскам. На территории находится Музей обороны Брестской крепости и знаменитый монумент «Мужество».'
                                          )

        case 2:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='Беловежская пуща\n\n'+
                                                  'Местоположение: агрогородок Каменюки\n\n'+
                                                  'Описание: Один из старейших заповедников Европы, известный своими вековыми лесами и популяцией зубров. Это национальный парк, включенный в список Всемирного наследия ЮНЕСКО, и знаменитое место отдыха и туризма в Беларуси.'
                                          )
        case 3:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='Каменецкая башня\n\n'+
                                                  'Местоположение: город Каменец, Каменецкий район\n\n'+
                                                  'Описание: Каменецкая башня, или Белая вежа, — средневековая башня, построенная в XIII веке. Она является одним из старейших оборонительных сооружений Беларуси и важным историко-архитектурным памятником, символизирующим архитектуру того времени.'
                                          )
        case 4:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='Ружанский замок\n\n'+
                                                  'Местоположение: поселок Ружаны, Пружанский район\n\n'+
                                                  'Описание: Ружанский замок — резиденция рода Сапегов, построенная в стиле барокко и классицизма. Разрушенный в войнах, он частично восстановлен и является популярным местом для экскурсий и съемок.'
                                          )
        case 5:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='Коссовский дворец\n\n'+
                                                  'Местоположение: город Коссово, Ивацевичский район\n\n'+
                                                  'Описание: Коссовский дворец, также известный как Дворец Пусловских, является уникальным примером неоготического стиля в Беларуси. Здание имеет 12 башен, каждая из которых символизирует месяц года.'
                                          )
        case 6:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='Свято-Афанасьевский монастырь\n\n'+
                                                  'Местоположение: город Брест\n\n'+
                                                  'Описание: Свято-Афанасьевский мужской монастырь — действующий православный монастырь в Бресте. Основан в XVII веке, он славится своей архитектурой и духовной атмосферой, привлекая паломников и туристов.'
                                          )
        case 7:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='Кобринский парк имени Суворова\n\n'+
                                                  'Местоположение: город Кобрин\n\n'+
                                                  'Описание: Кобринский парк имени Суворова — один из старейших парков Беларуси, основанный в XIX веке. В парке находится музей Суворова, посвященный знаменитому русскому полководцу, а также разнообразные памятники и скульптуры.'
                                          )
        case 8:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='Музей железнодорожной техники\n\n'+
                                                  'Местоположение: город Брест\n\n'+
                                                  'Описание: Музей железнодорожной техники — музей под открытым небом, где представлена коллекция исторических локомотивов и вагонов. Это место привлекает туристов и любителей железнодорожной истории.',
                                          )
        case 9:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='Спасо-Преображенский монастырь\n\n'+
                                                  'Местоположение: город Кобрин\n\n'+
                                                  'Описание: Спасо-Преображенский монастырь — православный монастырь, известный своим храмом, в котором хранится уникальная икона Богоматери. Комплекс монастыря выделяется своими старинными постройками и духовным значением.'
                                          )
        case 10:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='Сапегский дворец\n\n'+
                                                  'Местоположение: деревня Деречин, Зельвенский район\n\n'+
                                                  'Описание: Сапегский дворец, построенный в XVII веке, является одним из примеров белорусской аристократической архитектуры. Он служил резиденцией рода Сапегов и славится своей богатой историей и великолепной архитектурой.'
                                          )
        case 11:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 12:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 13:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 14:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 15:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 16:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 17:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )

        case 18:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 19:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )

        case 20:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 21:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 22:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 23:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 24:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 25:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 26:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 27:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 28:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 29:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 30:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 31:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 32:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 33:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 34:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 35:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 36:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 37:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 38:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 39:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case 40:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='\n\n' +
                                                  '\n\n' +
                                                  ''
                                          )
        case _:
            pass
    bot.edit_message_media(chat_id=message.chat.id,
                           message_id=message.message_id,
                           reply_markup=keyboards.DostoprimObjKeybord(obj_id),
                           media=photo)
