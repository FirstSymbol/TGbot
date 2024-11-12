import sqlite3
from random import randint
from tkinter.constants import INSERT

import telebot
from telebot.types import CallbackQuery
from telebot.types import Message
import callbackHandlers
import defaultmessages
import keyboards
from Fakt_module import Fakt
from Test_module import Test
from Test_module import TestStartPage

bot = telebot.TeleBot('7918252571:AAHi5YwxTGIh73y3d-o0DI5Y5vh0amfiqpU')

#db = sqlite3.connect('../database/database.db')
#c = db.cursor()
#c.execute("""DELETE FROM users WHERE user_id = 1416150901""")
#db.commit()
#db.close()

def init_tests():
    tests[0].questions[0].text = ('Где находится усадьба Бохвицей?\n'
                                  'а) Пинск\n'
                                  'б) Флерьяново\n'
                                  'в) Кобрин\n'
                                  'г) Барановичи\n'
                                  )
    tests[0].questions[0].correctAnswer = 2

    tests[0].questions[1].text = ('В каком агрогородке находится костел Сердца Иисуса?\n'
                                  'а) Столовичи\n'
                                  'б) Телеханы\n'
                                  'в) Жабинка\n'
                                  'г) Беловежа')
    tests[0].questions[1].correctAnswer = 1

    tests[0].questions[2].text = ('Где расположен Сапегский дворец?\n'
                                  'а) Ружаны\n'
                                  'б) Барановичи\n'
                                  'в) Каменец\n'
                                  'г) Пружаны\n')
    tests[0].questions[2].correctAnswer = 1

    tests[0].questions[3].text = ('В каком месте находится Музей космонавтики?\n'
                                  'а) деревня Томашовка\n'
                                  'б) Брест\n'
                                  'в) Мотоль\n'
                                  'г) Пинск')
    tests[0].questions[3].correctAnswer = 1

    tests[0].questions[4].text = ('В каком месте находится Брестская крепость?\n'
                                  'а) Каменец\n'
                                  'б) Пинск\n'
                                  'в) Барановичи\n'
                                  'г) Брест')
    tests[0].questions[4].correctAnswer = 4

    tests[0].questions[5].text = ('Где находятся Холмские ворота?\n'
                                  'а) Пинск\n'
                                  'б) Беловежа\n'
                                  'в) Брест\n'
                                  'г) Пружаны')
    tests[0].questions[5].correctAnswer = 3

    tests[0].questions[6].text = ('В каком населенном пункте можно увидеть Пружанский дворец?\n'
                                  'а) Брест\n'
                                  'б) Пинск\n'
                                  'в) Пружаны\n'
                                  'г) Ганцевичи')
    tests[0].questions[6].correctAnswer = 3

    tests[0].questions[7].text = ('Где расположен Музей-усадьба им. Т. Костюшко?\n'
                                  'а) Беловежа\n'
                                  'б) Коссово\n'
                                  'в) Мотоль\n'
                                  'г) Ляховичи')
    tests[0].questions[7].correctAnswer = 2

    tests[0].questions[8].text = ('Где находится музей "Каменецкая башня"?\n'
                                  'а) Каменец\n'
                                  'б) Брест\n'
                                  'в) Пружаны\n'
                                  'г) Барановичи')
    tests[0].questions[8].correctAnswer = 1

    tests[0].questions[9].text = ('Где расположен Музей Белорусского Полесья?\n'
                                  'а) Каменец\n'
                                  'б) Пинск\n'
                                  'в) Кобрин\n'
                                  'г) Барановичи')
    tests[0].questions[9].correctAnswer = 2

    # --------------------------------------------------



    tests[1].questions[0].text = ('Когда отмечается День Конституции Республики Беларусь?\n'
                                  'а) 3 июля\n'
                                  'б) 15 марта\n'
                                  'в) 9 мая\n'
                                  'г) 1 сентября\n'
                                  )
    tests[1].questions[0].correctAnswer = 2

    tests[1].questions[1].text = ('В какой день празднуют День защитников Отечества и Вооруженных Сил Республики Беларусь?\n'
                                  'а) 1 января\n'
                                  'б) 15 февраля\n'
                                  'в) 23 февраля\n'
                                  'г) 9 мая')
    tests[1].questions[1].correctAnswer = 3

    tests[1].questions[2].text = ('В какой день отмечают День памяти воинов-интернационалистов?\n'
                                  'а) 15 февраля\n'
                                  'б) 2 апреля\n'
                                  'в) 26 апреля\n'
                                  'г) 7 ноября\n')
    tests[1].questions[2].correctAnswer = 1

    tests[1].questions[3].text = ('Какого числа празднуется День Победы в Беларуси?\n'
                                  'а) 3 июля\n'
                                  'б) 9 мая\n'
                                  'в) 22 июня\n'
                                  'г) 7 ноября')
    tests[1].questions[3].correctAnswer = 2

    tests[1].questions[4].text = ('В какой день празднуют День Государственного герба и флага Республики Беларусь?\n'
                                  'а) Первое воскресенье октября\n'
                                  'б) Второе воскресенье мая\n'
                                  'в) Последнее воскресенье июня\n'
                                  'г) Третье воскресенье сентября')
    tests[1].questions[4].correctAnswer = 2

    tests[1].questions[5].text = ('В какой день отмечается День независимости Республики Беларусь (День Республики)?\n'
                                  'а) 3 июля\n'
                                  'б) 26 апреля\n'
                                  'в) 9 мая\n'
                                  'г) 7 ноября')
    tests[1].questions[5].correctAnswer = 1

    tests[1].questions[6].text = ('В какой день отмечают День матери в Беларуси?\n'
                                  'а) 15 октября\n'
                                  'б) 8 марта\n'
                                  'в) 14 октября\n'
                                  'г) 1 октября')
    tests[1].questions[6].correctAnswer = 3

    tests[1].questions[7].text = ('Когда в Беларуси празднуют День Октябрьской революции?\n'
                                  'а) 1 мая\n'
                                  'б) 7 ноября\n'
                                  'в) 1 января\n'
                                  'г) 9 мая')
    tests[1].questions[7].correctAnswer = 2

    tests[1].questions[8].text = ('Какого числа отмечают День белорусского кино?\n'
                                  'а) 15 сентября\n'
                                  'б) 17 декабря\n'
                                  'в) 25 декабря\n'
                                  'г) 10 декабря')
    tests[1].questions[8].correctAnswer = 2

    tests[1].questions[9].text = ('Когда празднуется День знаний в Беларуси?\n'
                                  'а) 1 сентября\n'
                                  'б) 1 июня\n'
                                  'в) 5 апреля\n'
                                  'г) 18 октября')
    tests[1].questions[9].correctAnswer = 1

fakts:list[Fakt] = list()
tests:list[Test] = list()

test0 = Test(testID=0,
                  questionCount=10,
                  startPage=TestStartPage('Этот тест на знание городов достопримечательностей.'))
tests.append(test0)
test1 = Test(testID=1,
                  questionCount=10,
                  startPage=TestStartPage('Этот тест на знание памятных дат и праздников РБ.'))
tests.append(test1)
init_tests()


for i in range(15):
    fakts.append(Fakt())
    fakts[i].id = i
    fakts[i].text = f'Факт о РБ {i+1}'

fakts[0].text = ('Историческая столица книги\n\n'+
                 'Белорусский город Минск был провозглашён Всемирной столицей книги ЮНЕСКО в 2017 году за вклад в продвижение чтения и литературы.\n1/15')
fakts[1].text = ('Древний Полоцк\n\n'
                 'Город Полоцк считается одним из старейших городов Восточной Европы – первые упоминания о нём датируются 862 годом.\n2/15')
fakts[2].text = ('Исторический центр Европы\n\n'
                 'Географический центр Европы по одной из методик расчета находится в Беларуси, неподалёку от деревни Полотово в Витебской области.\n3/15')
fakts[3].text = ('Страна озёр\n\n'
                 'В Беларуси насчитывается около 11 тысяч озёр, из которых самым крупным является Нарочь.\n4/15')
fakts[4].text = ('Сильный дух спорта\n\n'
                 'Беларусь прославилась в спортивном мире благодаря достижениям в таких видах, как биатлон, теннис и лёгкая атлетика. Белорусские спортсмены регулярно занимают высокие места на международных соревнованиях.\n5/15')
fakts[5].text = ('Уникальные флора и фауна Полесья\n\n'
                 'Полесские болота известны своей уникальной экосистемой и являются домом для редких видов птиц, растений и насекомых, привлекая исследователей и экотуристов.\n6/15')
fakts[6].text = ('Биосферные заповедники\n\n'
                 'На территории Беларуси находится несколько биосферных заповедников, включая Березинский биосферный заповедник, который охраняет редкие виды животных и растений.\n7/15')
fakts[7].text = ('Традиция Купалья\n\n'
                 'Белорусы празднуют ночь на Ивана Купалу — древний славянский праздник, на котором жгут костры, плетут венки и совершают обряды на поиски папоротника.\n8/15')
fakts[8].text = ('Национальная библиотека — «алмаз» Минска\n\n'
                 'Здание Национальной библиотеки Беларуси часто называют «алмазом» Минска из-за его оригинальной формы, напоминающей многогранный кристалл.\n9/15')
fakts[9].text = ('Минск – город-герой\n\n'
                 'Во время Второй мировой войны город Минск был практически полностью разрушен, но его восстановили, и за мужество его жителей Минску присвоили звание "Город-герой".\n10/15')
fakts[10].text = ('Государство без гор\n\n'
                 'Беларусь — одна из немногих стран Европы, в которой нет гор. Её самая высокая точка — гора Дзержинская (около 345 метров).\n11/15')
fakts[11].text = ('Уникальный музей валунов в Минске\n\n'
                 'В Минске расположен один из крупнейших в мире музеев валунов под открытым небом, где собраны камни, привезенные со всей страны для сохранения культурного наследия.\n12/15')
fakts[12].text = ('Родина многих известных личностей\n\n'
                 'На территории Беларуси родились такие выдающиеся личности, как художник Марк Шагал, философ Соломон Маймон, космонавт Петр Климук и многие другие.\n13/15')
fakts[13].text = ('Фестиваль «Славянский базар»\n\n'
                 'Ежегодно в Витебске проводится международный фестиваль искусств «Славянский базар», который объединяет музыкантов и артистов из многих стран мира.\n14/15')
fakts[14].text = ('Дом легендарного Статута Великого княжества Литовского\n\n'
                 'В 1588 году был принят третий Статут Великого княжества Литовского, одного из наиболее прогрессивных правовых документов своего времени. Статут был составлен на старобелорусском языке.\n15/15')


def registerUser(message:Message):
    db = sqlite3.connect('../database/database.db')
    c = db.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    check = False
    for user in users:
        if user[0] == message.chat.id:
            print('Найдено совпадение')
            check = True

            if user[1] != message.chat.id:
                c.execute(f"UPDATE users SET user_chat = {message.chat.id} WHERE user_id = {message.chat.id}")
                db.commit()
            break
    else:
        if check == False:
            print('Совпадение не найдено')
            c.execute(f"INSERT INTO users VALUES ({message.chat.id},{message.chat.id})")
            c.execute(f"INSERT INTO test0 VALUES ({message.chat.id},'0000000000',0)")
            c.execute(f"INSERT INTO test1 VALUES ({message.chat.id},'0000000000',0)")
            c.execute(f"INSERT INTO test2 VALUES ({message.chat.id},'0000000000',0)")
            db.commit()
    db.close()

@bot.message_handler(commands=['start'])
def Start(message:Message):
    registerUser(message)
    bot.send_message(message.chat.id,f'Привет {message.from_user.full_name}.\nВот тебе меню:',reply_markup=keyboards.mainMenuKeyboard)


@bot.message_handler()
def mainMenuHandler(message:Message):
    registerUser(message)
    if(message.text == 'В главное меню'):
        defaultmessages.SendMainMenu(bot,message.chat.id)
    else:
        defaultmessages.MessageNotFounded(bot,message)

# Обработчик коллбэков

@bot.callback_query_handler(func=lambda callback:True)
def mainHandler(callback:CallbackQuery):
    registerUser(callback.message)
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
        case 'load_zapovedniki':
            callbackHandlers.zapovedniki_click(bot,callback.message)
        case 'load_prazdniki':
            callbackHandlers.prazdniki_click(bot,callback.message)
        case 'load_prazdnik_globals':
            callbackHandlers.prazdnik_globals_click(bot,callback.message)
        case 'load_prazdnik_days':
            callbackHandlers.prazdnik_days_click(bot,callback.message)
        case 'load_prazdnik_pamyat':
            callbackHandlers.prazdnik_pamyat_click(bot,callback.message)
            
    # Итерируемые коллбеки
    print(callback.data)
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

        case 'load_fakt':
            values = callback.data[10:].split('_')
            if values[0] == 'random':
                num = randint(0,len(fakts)-1)
                try:
                    fakts[num].LoadFakt(bot,callback.message)
                except:
                    num = randint(0,len(fakts)-1)
                    fakts[num].LoadFakt(bot, callback.message)
            else:
                try:
                    fakts[int(values[0])].LoadFakt(bot,callback.message)
                except:
                    pass

    match callback.data[0:10]:
        case 'start_test':
            values = callback.data[11:].split('_')
            tests[int(values[0])].LoadQuestion(bot,callback.message,int(values[1]))
            db = sqlite3.connect('../database/database.db')
            c = db.cursor()
            c.execute(f"""UPDATE test{values[0]} SET marks = '0000000000' WHERE user_id = {callback.message.chat.id}""")
            db.commit()
            db.close()

    match callback.data[0:11]:
        case 'answer_test':
            values = callback.data[12:].split('_')
            callbackHandlers.answer_test_click(bot=bot,
                                               message=callback.message,
                                               values=values,
                                               tests=tests)
        case 'load_zapov_':
            values = callback.data[11:].split('_')
            callbackHandlers.zapovednik_click(bot, callback.message, int(values[0]))


@bot.message_handler(content_types=['location'])
def FindDostoprim(message:Message):
    registerUser(message)
    defaultmessages.GeoMessage(bot,message)



bot.polling(non_stop=True)