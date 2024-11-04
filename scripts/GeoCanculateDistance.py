from math import radians, cos, sin, sqrt, atan2

# Пример базы данных достопримечательностей
places = [
    {'name': "Брестская крепость", "latitude": 52.085608, "longitude": 23.655606},
    {"name": "Беловежская пуща", "latitude": 52.773278, "longitude": 23.874983},
    {"name": "Каменецкая башня", "latitude":52.404767, "longitude":23.819429},
    {"name": "Ружанский замок", "latitude":52.861393, "longitude":24.896075},
    {"name": "Коссовский дворец", "latitude":52.767579, "longitude":25.125259},
    {"name": "Свято-Афанасьевский монастырь", "latitude":52.056656, "longitude":23.698426},
    {"name": "Кобринский парк имени Суворова", "latitude":52.200801, "longitude":24.352276},
    {"name": "Музей железнодорожной техники", "latitude":52.085633, "longitude":23.672120},
    {"name": "Спасо-Преображенский монастырь", "latitude":52.214834, "longitude":24.355756},
    {"name": "Музей Белорусского Полесья", "latitude":52.111166, "longitude":26.103826},
    {"name": "Музей природы Беловежской пущи", "latitude":52.572606, "longitude":23.801718},
    {"name": "Холмские ворота", "latitude":52.081291, "longitude":23.656394},
    {"name": "Музей обороны Брестской крепости", "latitude":52.083702, "longitude":23.657960},
    {"name": "Усадьба Немцевичей", "latitude":52.155796, "longitude":23.637893},
    {"name": "Музей народного творчества \"Бездежский фартушок\"", "latitude":52.312859, "longitude":25.309762},
    {"name": "Барановичский Парк животных", "latitude":53.096581, "longitude":26.010405},
    {"name": "Пинская набережная и речной порт", "latitude":52.110185, "longitude":26.104263},
    {"name": "Костел Сердца Иисуса", "latitude":53.212019, "longitude":26.035049},
    {"name": "Хмелёвский Спасо-Преображенский монастырь", "latitude":52.252033, "longitude":23.887674},
    {"name": "Кобринская синагога", "latitude":52.211807, "longitude":24.365059},
    {"name": "Костёл Пресвятой Девы Марии", "latitude":52.112972, "longitude":26.108384},
    {"name": "Музей космонавтики", "latitude":51.561516, "longitude":23.601473},
    {"name": "Озеро Каташи", "latitude":52.126210, "longitude":24.346833},
    {"name": "Дом-музей Адама Мицкевича", "latitude":53.278636, "longitude":26.115304},
    {"name": "Музей-усадьба им. Т. Костюшко", "latitude":52.767558, "longitude":25.125298},
    {"name": "Усадьба Котлубаев", "latitude":53.031215, "longitude":25.959322},
    {"name": "Форт V Брестской крепости", "latitude":52.047719, "longitude":23.672870},
    {"name": "Усадьба Бохвицей", "latitude":53.092468, "longitude":26.269185},
    {"name": "Жировицкая икона Божией Матери", "latitude":53.013885, "longitude":25.346153},
    {"name": "Собор святых Петра и Павла", "latitude":52.338033, "longitude":25.986816},
]


def calculate_distance(lat1, lon1, lat2, lon2):
    # Формула для вычисления расстояния между двумя координатами
    R = 6371  # Радиус Земли в километрах
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) * sin(dlat / 2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) * sin(dlon / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def find_nearest_places(user_lat, user_lon,count:int):
    distances = []
    for place in places:
        distance = calculate_distance(user_lat, user_lon, place["latitude"], place["longitude"])
        distances.append((place, distance))

    # Сортируем по расстоянию и выбираем ближайшие 3 места
    distances.sort(key=lambda x: x[1])
    nearest = distances[:count]  # Извлекаем три ближайших места

    result = f"Ближайшие {count} достопримечательностей:\n\n"
    for place, dist in nearest:
        result += f"{place['name']} ({dist:.2f} км)\n"
    return result
