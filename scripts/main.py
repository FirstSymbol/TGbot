import telebot
from telebot.types import CallbackQuery
from telebot.types import Message

import callbackHandlers
import defaultmessages
import keyboards
from Test_module import Test
from Test_module import TestStartPage

bot = telebot.TeleBot('7918252571:AAHi5YwxTGIh73y3d-o0DI5Y5vh0amfiqpU')
tests:list[Test] = list()
tests.append(Test(testID=0,
                  questionCount=10,
                  startPage=TestStartPage('Это начальная страница теста 1'))
             )
tests[0].questions[0].text = 'Вопрос1'
tests[0].questions[0].correctAnswer = 2
tests[0].questions[1].text = 'Вопрос2'
tests[0].questions[1].correctAnswer = 3
tests[0].questions[2].text = 'Вопрос3'
tests[0].questions[3].text = 'Вопрос4'
tests[0].questions[4].text = 'Вопрос5'
tests[0].questions[5].text = 'Вопрос6'
tests[0].questions[6].text = 'Вопрос7'
tests[0].questions[7].text = 'Вопрос8'
tests[0].questions[8].text = 'Вопрос9'
tests[0].questions[9].text = 'Вопрос10'


@bot.message_handler(commands=['start'])
def Start(message:Message):
    bot.send_message(message.chat.id,f'Привет {message.from_user.full_name}.\nВот тебе меню:',reply_markup=keyboards.mainMenuKeyboard)

@bot.message_handler()
def mainMenuHandler(message:Message):
    if(message.text == 'В главное меню'):
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
            
    # Итерируемые коллбеки
    match callback.data[0:13]:
        case 'dostoprim_obj':
            callbackHandlers.dostoprim_obj_click(bot,callback.message,int(callback.data[13:]))

    match callback.data[0:6]:
        case 'otvet_':
            pass
    match callback.data[0:9]:
        case 'load_test':
            values = callback.data[10:].split('_')
            tests[int(values[0])].LoadTest(bot,callback.message)

    match callback.data[0:10]:
        case 'start_test':
            values = callback.data[11:].split('_')
            tests[int(values[0])].LoadQuestion(bot,callback.message,int(values[1]))
            tests[int(values[0])].answers.clear()

    match callback.data[0:11]:
        case 'answer_test':
            values = callback.data[12:].split('_')
            callbackHandlers.answer_test_click(bot=bot,
                                               message=callback.message,
                                               values=values,
                                               tests=tests)


@bot.message_handler(content_types=['location'])
def FindDostoprim(message:Message):
    defaultmessages.GeoMessage(bot,message)

bot.polling(non_stop=True)