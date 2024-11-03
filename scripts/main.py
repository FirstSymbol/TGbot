import telebot
import keyboards
import callbackHandlers
import defaultmessages
from telebot import types
from telebot.types import Message
from telebot.types import CallbackQuery

bot = telebot.TeleBot('7918252571:AAHi5YwxTGIh73y3d-o0DI5Y5vh0amfiqpU')

@bot.message_handler(commands=['start'])
def Start(message:Message):
    bot.send_message(message.chat.id,f'Привет {message.from_user.full_name}.\nВот тебе меню:',reply_markup=keyboards.mainMenuKeyboard)

@bot.message_handler()
def mainMenuHandler(message:Message):
    if(message.text == 'Главное меню:'):
        defaultmessages.SendMainMenu(bot,message.chat.id)
    else:
        defaultmessages.MessageNotFounded(bot,message)

# Обработчик коллбэков

@bot.callback_query_handler(func=lambda callback:True)
def mainHandler(callback:CallbackQuery):
    
    # Не итерируемые коллбэки
    match callback.data:
        case 'main_button1':
            callbackHandlers.mainMenu_button1_click(bot,callback.message)
        case 'main_button2':
            callbackHandlers.mainMenu_button2_click(bot,callback.message)
        case 'main_button3':
            callbackHandlers.mainMenu_button3_click(bot,callback.message)
        case 'main_button4':
            callbackHandlers.mainMenu_button4_click(bot,callback.message)
        case 'to_mainmenu':
            callbackHandlers.toMainMenu_click(bot,callback.message)
        case 'dostoprim_page1':
            callbackHandlers.dostoprim_page1_click(bot,callback.message)
        case 'dostoprim_page2':
            callbackHandlers.dostoprim_page2_click(bot,callback.message)
        case 'dostoprim_page3':
            callbackHandlers.dostoprim_page3_click(bot,callback.message)
        case 'dostoprim_page4':
            callbackHandlers.dostoprim_page4_click(bot,callback.message)
            
    # Итерируемые коллбеки
    match callback.data[0:13]:
        case 'dostoprim_obj':
            callbackHandlers.dostoprim_obj_click(bot,callback.message,int(callback.data[13:]))
            
    
    
bot.polling(non_stop=True)