import telebot
from telebot import TeleBot
from telebot import types
from telebot.apihelper import delete_message
from telebot.types import Message, InputFile

import GeoCanculateDistance
import keyboards


def SendMainMenu(bot:TeleBot,chatID:int):
    newmessage = bot.send_message(text='.',
                                  chat_id=chatID,
                                  reply_markup=types.ReplyKeyboardRemove())
    bot.delete_message(chat_id=chatID,
                       message_id=newmessage.message_id)
    bot.send_message(chat_id=chatID,
                     text='📋| Главное меню:',
                     reply_markup=keyboards.mainMenuKeyboard)

def SendMainMenuRemoveKeyboard(bot:TeleBot,message:Message):
    bot.delete_message(chat_id=message.chat.id,
                   message_id=message.message_id)
    SendMainMenu(bot,message.chat.id)



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
    bot.send_message(text='🏛| Достопримечательности Бресткой области [1 / 3]',
                    chat_id=chatID,
                    reply_markup=keyboards.DostoprimPageKeybord(1))

def SendDostoprimPage2(bot: telebot.TeleBot, chatID: int):
    bot.send_message(text='🏛| Достопримечательности Бресткой области [2 / 3]',
                    chat_id=chatID,
                    reply_markup=keyboards.DostoprimPageKeybord(2))

def SendDostoprimPage3(bot: telebot.TeleBot, chatID: int):
    bot.send_message(text='🏛| Достопримечательности Бресткой области [3 / 3]',
                    chat_id=chatID,
                    reply_markup=keyboards.DostoprimPageKeybord(3))

def EditDostoprimPage1(bot: telebot.TeleBot, message: Message):
    if message.photo:
        chatID = message.chat.id
        bot.delete_message(message_id=message.message_id,
                           chat_id=message.chat.id)
        SendDostoprimPage1(bot, chatID)
    else:
        bot.edit_message_text(text='🏛| Достопримечательности Бресткой области [1 / 3]',
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
        bot.edit_message_text(text='🏛| Достопримечательности Бресткой области [2 / 3]',
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
        bot.edit_message_text(text='🏛| Достопримечательности Бресткой области [3 / 3]',
                              chat_id=message.chat.id,
                              message_id=message.message_id,
                              reply_markup=keyboards.DostoprimPageKeybord(3))
    
def EditDostoprimObj(bot:TeleBot,message:Message,obj_id:int):
    global photo
    match obj_id:
        case 1:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj1.jpg'),
                                          caption='Брестская крепость\n\n'+
                                                  'Местоположение: город Брест\n\n'+
                                                  'Описание: Мемориальный комплекс и символ мужества советских солдат во время Великой Отечественной войны. Известна обороной 1941 года, когда защитники крепости мужественно противостояли немецким войскам. На территории находится Музей обороны Брестской крепости и знаменитый монумент «Мужество».'+
                                                  f'\n\n[{obj_id}/30]'
                                          )

        case 2:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj2.jpg'),
                                          caption='Беловежская пуща\n\n'+
                                                  'Местоположение: агрогородок Каменюки\n\n'+
                                                  'Описание: Один из старейших заповедников Европы, известный своими вековыми лесами и популяцией зубров. Это национальный парк, включенный в список Всемирного наследия ЮНЕСКО, и знаменитое место отдыха и туризма в Беларуси.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 3:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj3.jpg'),
                                          caption='Каменецкая башня\n\n'+
                                                  'Местоположение: город Каменец, Каменецкий район\n\n'+
                                                  'Описание: Каменецкая башня, или Белая вежа, — средневековая башня, построенная в XIII веке. Она является одним из старейших оборонительных сооружений Беларуси и важным историко-архитектурным памятником, символизирующим архитектуру того времени.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 4:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj4.jpg'),
                                          caption='Ружанский замок\n\n'+
                                                  'Местоположение: поселок Ружаны, Пружанский район\n\n'+
                                                  'Описание: Ружанский замок — резиденция рода Сапегов, построенная в стиле барокко и классицизма. Разрушенный в войнах, он частично восстановлен и является популярным местом для экскурсий и съемок.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 5:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj5.jpg'),
                                          caption='Коссовский дворец\n\n'+
                                                  'Местоположение: город Коссово, Ивацевичский район\n\n'+
                                                  'Описание: Коссовский дворец, также известный как Дворец Пусловских, является уникальным примером неоготического стиля в Беларуси. Здание имеет 12 башен, каждая из которых символизирует месяц года.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 6:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj6.jpg'),
                                          caption='Свято-Афанасьевский монастырь\n\n'+
                                                  'Местоположение: город Брест\n\n'+
                                                  'Описание: Свято-Афанасьевский мужской монастырь — действующий православный монастырь в Бресте. Основан в XVII веке, он славится своей архитектурой и духовной атмосферой, привлекая паломников и туристов.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 7:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj7.jpg'),
                                          caption='Кобринский парк имени Суворова\n\n'+
                                                  'Местоположение: город Кобрин\n\n'+
                                                  'Описание: Кобринский парк имени Суворова — один из старейших парков Беларуси, основанный в XIX веке. В парке находится музей Суворова, посвященный знаменитому русскому полководцу, а также разнообразные памятники и скульптуры.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 8:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj8.jpg'),
                                          caption='Музей железнодорожной техники\n\n'+
                                                  'Местоположение: город Брест\n\n'+
                                                  'Описание: Музей железнодорожной техники — музей под открытым небом, где представлена коллекция исторических локомотивов и вагонов. Это место привлекает туристов и любителей железнодорожной истории.'+
                                                  f'\n\n[{obj_id}/30]',
                                          )
        case 9:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj9.jpg'),
                                          caption='Спасо-Преображенский монастырь\n\n'+
                                                  'Местоположение: город Кобрин\n\n'+
                                                  'Описание: Спасо-Преображенский монастырь — православный монастырь, известный своим храмом, в котором хранится уникальная икона Богоматери. Комплекс монастыря выделяется своими старинными постройками и духовным значением.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 10:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj10.jpg'),
                                          caption='Музей Белорусского Полесья\n\n'+
                                                  'Местоположение: город Пинск\n\n'+
                                                  'Описание: Музей белорусского Полесья — это культурный и исторический центр, посвященный уникальному наследию региона Полесье. В музее представлены коллекции, отражающие традиции, быт и культуру полесских народов, включая предметы искусства, этнографические экспонаты и фотографии. Здесь можно узнать о природных особенностях региона, а также о его историческом значении.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 11:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj11.jpg'),
                                          caption='Музей природы Беловежской пущи\n\n' +
                                                  'Местоположение: Каменецкий район, Беловежская пуща\n\n' +
                                                  'Описание: Музей природы в Беловежской пуще предлагает уникальную экспозицию, рассказывающую о богатстве флоры и фауны заповедника. Здесь можно увидеть чучела редких животных и познакомиться с историей охраны природы.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 12:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj12.jpg'),
                                          caption='Холмские ворота\n\n' +
                                                  'Местоположение: город Брест\n\n' +
                                                  'Описание: Холмские ворота — один из символов Брестской крепости, через который в 1941 году немцы начали штурм. Это памятник мужеству и стойкости защитников крепости, сохранившийся до наших дней.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 13:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj13.jpg'),
                                          caption='Музей обороны Брестской крепости\n\n' +
                                                  'Местоположение: город Брест\n\n' +
                                                  'Описание: Музей обороны Брестской крепости — это важный исторический и мемориальный комплекс, посвященный событиям Великой Отечественной войны. Он расположен на территории Брестской крепости, которая стала символом мужества и героизма советских солдат. Музей предлагает посетителям уникальные экспонаты, включая военное оружие, документы и личные вещи защитников крепости. Здесь проводятся экскурсии, на которых рассказывают о героической обороне крепости в июне 1941 года, а также об истории самого объекта, что позволяет глубже понять важность этих событий для Беларуси и всего мира.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 14:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj14.jpg'),
                                          caption='Усадьба Немцевичей\n\n' +
                                                  'Местоположение: деревня Скоки, Брестский район\n\n' +
                                                  'Описание: Усадьба Немцевичей — бывшая резиденция знаменитого рода Немцевичей, построенная в стиле классицизма. Здесь часто проводятся экскурсии, знакомящие посетителей с культурой и историей белорусской шляхты.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 15:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj15.jpg'),
                                          caption='Музей народного творчества "Бездежский фартушок"\n\n' +
                                                  'Местоположение: деревня Бездеж, Брестская область\n\n' +
                                                  'Описание: Музей народного творчества "Бездежский фартушок"" является уникальным местом, посвященным белорусским традициям и ремеслам. Здесь представлены коллекции народных костюмов, текстиля, вышивки и других видов народного искусства. Музей предлагает посетителям познакомиться с богатым культурным наследием региона, а также поучаствовать в мастер-классах по народным ремеслам, таким как вышивка и ткачество. Экскурсии позволяют глубже понять традиции и обычаи белорусского народа, сохранившиеся на протяжении веков.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 16:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj16.jpg'),
                                          caption='Барановичский Парк животных\n\n' +
                                                  'Местоположение: город Барановичи\n\n' +
                                                  'Описание: Барановичский парк животных — это зоологический комплекс, где можно увидеть множество различных животных, как местных, так и экзотических видов. Парк создает условия для комфортного пребывания животных и активно занимается их охраной и размножением. Посетители могут насладиться прогулками по территории парка, а также познакомиться с редкими видами и узнать об их привычках и среде обитания. Парк подходит для семейного отдыха и является отличным местом для обучения детей о мире животных и важности их сохранения.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 17:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj17.jpg'),
                                          caption='Пинская набережная и речной порт\n\n' +
                                                  'Местоположение: город Пинск\n\n' +
                                                  'Описание: Пинская набережная — живописное место для прогулок с видами на реку Пина. Речной порт Пинска — это не только транспортный узел, но и важная достопримечательность города, где можно увидеть старинные суда.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )

        case 18:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj18.jpg'),
                                          caption='Костел Сердца Иисуса\n\n' +
                                                  'Местоположение: агрогородок Столовичи, Барановичский район\n\n' +
                                                  'Описание: Костёл Сердца Иисуса — католический храм, построенный в начале XX века. Это прекрасное здание в стиле неоготики славится своей архитектурной элегантностью и живописным местоположением. Внутри храма находятся красивые витражи и иконы, которые создают атмосферу спокойствия и молитвы. Костёл является важным духовным центром для местной католической общины и привлекает паломников и туристов.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 19:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj19.jpg'),
                                          caption='Хмелёвский Спасо-Преображенский монастырь\n\n' +
                                                  'Местоположение: деревня Хмелёва, Брестский район\n\n' +
                                                  'Описание: Хмелёвский Спасо-Преображенский монастырь — это действующий православный монастырь, основанный в начале XX века. Он известен своими живописными природными ландшафтами и спокойной атмосферой. Монастырь привлекает паломников и туристов, желающих погрузиться в духовную атмосферу и насладиться тишиной. Здесь проводятся богослужения, а также доступны экскурсии, знакомящие с историей и традициями монастыря.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )

        case 20:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj20.jpg'),
                                          caption='Кобринская синагога\n\n' +
                                                  'Местоположение: город Кобрин\n\n' +
                                                  'Описание: Кобринская синагога — историческое здание и символ еврейской общины города. Построенная в начале XX века, она напоминает о культурном разнообразии и историческом наследии Кобрина.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 21:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj21.jpg'),
                                          caption='Костёл Пресвятой Девы Марии\n\n' +
                                                  'Местоположение: город Пинск\n\n' +
                                                  'Описание: Костёл Пресвятой Девы Марии — католический храм, построенный в стиле барокко в XVII веке. Здание славится своими великолепными внутренними интерьерами и является одним из культурных центров католической общины Пинска.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 22:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj22.jpg'),
                                          caption='Музей космонавтики\n\n' +
                                                  'Местоположение: деревня Томашовка, Брестский район\n\n' +
                                                  'Описание: Музей космонавтики в Томашовке — уникальный музей, посвященный истории освоения космоса. Он был открыт в память о выдающемся советском космонавте Петре Климуке, который родился в этих местах. Экспозиция музея включает в себя разнообразные экспонаты, связанные с космическими исследованиями, личные вещи космонавтов, макеты космических аппаратов и фотографии. Музей является важным культурным объектом, привлекающим как школьников, так и взрослых посетителей, интересующихся историей космонавтики.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 23:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj23.jpg'),
                                          caption='Озеро Каташи\n\n' +
                                                  'Координаты: 52.126607, 24.345715 ,Кобринский район, Брестская область\n\n' +
                                                  'Описание: Озеро Каташи — одно из живописных озер Брестской области, расположенное в окружении густых лесов и зелени. Это место привлекает туристов своей красотой и спокойствием, являясь идеальным для отдыха на природе, рыбалки и пикников. Озеро славится чистой водой и разнообразной фауной, что делает его популярным среди любителей наблюдать за птицами и фотографов.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 24:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj24.jpg'),
                                          caption='Дом-музей Адама Мицкевича\n\n' +
                                                  'Местоположение: деревня Заосье, Ивацевичский район\n\n' +
                                                  'Описание: Дом-музей Адама Мицкевича — место, где родился известный польско-белорусский поэт Адам Мицкевич. Здесь представлены экспозиции, рассказывающие о жизни и творчестве великого писателя.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 25:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj25.jpg'),
                                          caption='Музей-усадьба им. Т. Костюшко\n\n' +
                                                  'Местоположение: Коссово, Ивацевичский район\n\n' +
                                                  'Описание: Музей-усадьба имени Тадеуша Костюшко — это место, где родился и провел ранние годы жизни выдающийся национальный герой Польши, Беларуси и США. Комплекс включает восстановленный усадебный дом и парк. Здесь представлены экспозиции, рассказывающие о жизни и деятельности Костюшко, его участии в борьбе за независимость Америки и вклад в европейские освободительные движения. Музей также освещает исторический контекст эпохи и роль Костюшко в мировой истории.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 26:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj26.jpg'),
                                          caption='Усадьба Котлубаев\n\n' +
                                                  'Местоположение: деревня Ястрембель, Барановичский район\n\n' +
                                                  'Описание: Усадьба Котлубаев — историческое поместье, построенное в XIX веке, принадлежавшее шляхетскому роду Котлубаев. Архитектурный комплекс включает главный дом, выполненный в стиле классицизма, и живописный парк с аллеями и редкими видами деревьев. Усадьба известна своей культурной и исторической ценностью, так как в ней часто проводились собрания местной интеллигенции и гостей из разных частей Беларуси. Сегодня усадьба является объектом культурного наследия и привлекает туристов, интересующихся историей и архитектурой.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 27:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj27.jpg'),
                                          caption='Форт V Брестской крепости\n\n' +
                                                  'Местоположение: город Брест\n\n' +
                                                  'Описание: Форт V Брестской крепости является частью системы оборонительных сооружений, построенных в XIX веке для защиты западных границ Российской империи. Расположенный на северо-западной окраине Бреста, форт сохранился до наших дней и напоминает о военных событиях, связанных с Первой и Второй мировыми войнами. В его стенах проходили ожесточенные бои, особенно в период обороны Брестской крепости в 1941 году. Сегодня форт открыт для посетителей как исторический памятник, позволяющий ощутить атмосферу прошлого и узнать больше о героических страницах истории города.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 28:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj28.jpg'),
                                          caption='Усадьба Бохвицей\n\n' +
                                                  'Местоположение: деревня Флерьяново, Пинский район\n\n' +
                                                  'Описание: Усадьба Бохвицей — это архитектурный комплекс, построенный в начале XX века, представляющий собой образец белорусской усадебной архитектуры. Усадьба окружена живописным парком и прудом, создающим атмосферу уединения и спокойствия. Вокруг усадьбы расположены старинные деревья и ландшафтные элементы, которые придают этому месту особую историческую ценность. Усадьба Бохвицей является значимой частью культурного наследия региона и привлекает туристов своим уникальным стилем и атмосферой.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 29:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj29.jpg'),
                                          caption='Жировицкая икона Божией Матери\n\n' +
                                                  'Местоположение: Явленская церковь Свято-Успенского Жировичского ставропигиального мужского монастыря, деревня Жировичи, Слонимский район\n\n' +
                                                  'Описание: Жировицкая икона Божией Матери — одна из самых почитаемых святынь Беларуси. Хранится в Жировичском монастыре и ежегодно привлекает множество паломников, которые приходят поклониться иконе.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case 30:
            photo = types.InputMediaPhoto(InputFile('../images/dostoprim/obj30.jpg'),
                                          caption='Собор святых Петра и Павла\n\n' +
                                                  'Местоположение: поселок Логишин, Пинский район\n\n' +
                                                  'Описание: Собор святых Петра и Павла в Логишине — православный храм, известный своей историей и архитектурой. Построенный в XIX веке, он является важным духовным центром поселка. Собор выделяется своим красивым фасадом и внутренними фресками, привлекающими верующих и туристов. Храм также связан с почитанием иконы Логишинской Божией Матери, которая считается чудотворной и привлекает паломников со всей Беларуси.'+
                                                  f'\n\n[{obj_id}/30]'
                                          )
        case _:
            return
    bot.edit_message_media(chat_id=message.chat.id,
                           message_id=message.message_id,
                           reply_markup=keyboards.DostoprimObjKeybord(obj_id),
                           media=photo)

def GetGeo(bot:TeleBot, message:Message):
    chatID = message.chat.id

    bot.delete_message(chat_id=chatID,
                       message_id=message.message_id)
    bot.send_message(text='Нажав кнопку "Поиск" вы передаете свое местоположение боту для осуществения поиска.',
                    chat_id=chatID,
                    reply_markup=keyboards.GetGeoKeyboard())
def GeoMessage(bot:TeleBot, message:Message):
    newmessage = bot.send_message(chat_id=message.chat.id,
                     text='.',
                     reply_markup=types.ReplyKeyboardRemove())
    bot.delete_message(chat_id=newmessage.chat.id,
                       message_id=newmessage.message_id)
    bot.send_message(chat_id=message.chat.id,
                     text=GeoCanculateDistance.find_nearest_places(message.location.latitude,
                                                                   message.location.longitude,
                                                                   10),
                     reply_markup=keyboards.ToMainMenuKeyboard())

def EditGeneralInformation(bot:TeleBot,message:Message):
    bot.edit_message_text(text='Данный бот был создан в рамках какого-то там конкурса учащимся колледжа БГКЛ им. В.Е.Чернышева Жуковцом А.В.',
                          chat_id=message.chat.id,
                          message_id=message.message_id,
                          reply_markup=keyboards.ToMainMenuKeyboard())

def EditTests(bot:TeleBot,message:Message):
    bot.edit_message_text(text='Тест на знание городов достопримечательностей',
                          chat_id=message.chat.id,
                          message_id=message.message_id,
                          reply_markup=keyboards.StartTestKeybord())

anwsers = []

def TestingMessages(bot:telebot.TeleBot,message:Message,index:int):
    nextIndex = index + 1
    print(anwsers)

    corrects = ['a','a','b','c','d','a','b','c','d','d']

    match index:
        case 1:
            anwsers.clear()
            bot.edit_message_text(text='Вопрос 1',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.TestKeybord(corrects[0],index))
        case 2:
            bot.edit_message_text(text='Вопрос 2',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.TestKeybord(corrects[1],index))
        case 3:
            bot.edit_message_text(text='Вопрос 3',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.TestKeybord(corrects[2],index))
        case 4:
            bot.edit_message_text(text='Вопрос 4',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.TestKeybord(corrects[3],index))
        case 5:
            bot.edit_message_text(text='Вопрос 5',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.TestKeybord(corrects[4],index))
        case 6:
            bot.edit_message_text(text='Вопрос 6',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.TestKeybord(corrects[5],index))
        case 7:
            bot.edit_message_text(text='Вопрос 7',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.TestKeybord(corrects[6],index))
        case 8:
            bot.edit_message_text(text='Вопрос 8',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.TestKeybord(corrects[7],index))
        case 9:
            bot.edit_message_text(text='Вопрос 9',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.TestKeybord(corrects[8],index))
        case 10:
            bot.edit_message_text(text='Вопрос 10',
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.TestKeybord(corrects[9],index))
        case _:
            bot.edit_message_text(text="Тест закончен",
                                  chat_id=message.chat.id,
                                  message_id=message.message_id,
                                  reply_markup=keyboards.ToMainMenuKeyboard())
