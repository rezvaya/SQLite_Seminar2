import sqlite3

products_data = [
    (1, 'Яблоко', 52.0),
    (2, 'Гречка', 123.0),
    (3, 'Куриное филе', 165.0),
    (4, 'Огурец', 16.0),
    (5, 'Молоко', 42.0),
    (6, 'Рис', 130.0),
    (7, 'Тунец', 130.0),
    (8, 'Банан', 89.0),
    (9, 'Грейпфрут', 42.0),
    (10, 'Творог', 103.0), 
    (11, 'Апельсин', 43.0),
    (12, 'Картошка', 77.0),
    (13, 'Лосось', 206.0),
    (14, 'Помидор', 18.0),
    (15, 'Кефир', 51.0),
    (16, 'Греческий йогурт', 59.0),
    (17, 'Мед', 304.0),
    (18, 'Шпинат', 23.0),
    (19, 'Авокадо', 160.0),
    (20, 'Морковь', 41.0),
    (21, 'Кукуруза', 96.0),
    (22, 'Чернослив', 240.0),
    (23, 'Свекла', 43.0),
    (24, 'Малина', 52.0),
    (25, 'Куриное яйцо', 155.0),
    (26, 'Креветки', 106.0),
    (27, 'Говядина', 250.0),
    (28, 'Капуста', 25.0),
    (29, 'Киноа', 120.0),
    (30, 'Гранат', 83.0),
    (31, 'Фасоль', 341.0),
    (32, 'Арахис', 567.0),
    (33, 'Сливки', 340.0),
    (34, 'Инжир', 74.0),
    (35, 'Чеснок', 149.0),
    (36, 'Лаваш', 260.0),
    (37, 'Телятина', 143.0),
    (38, 'Киш-миш', 415.0),
    (39, 'Красная смородина', 56.0),
    (40, 'Персик', 39.0),
    (41, 'Творожный сыр', 174.0),
    (42, 'Базилик', 23.0),
    (43, 'Ананас', 50.0),
    (44, 'Спаржа', 20.0),
    (45, 'Сельдерей', 16.0)
]

meals_data = [
    (1, 'Салат с курицей и огурцом'),
    (2, 'Рыбный суп'),
    (3, 'Фруктовый смузи'),
    (4, 'Овощной салат'),
    (5, 'Куриные котлеты с гречкой'),
    (6, 'Печеный лосось с картошкой'),
    (7, 'Фасоль с тунцом'),
    (8, 'Творожные оладьи с малиной'),
    (9, 'Авокадо-томатный салат'),
    (10, 'Греческий йогурт с медом'),
    (11, 'Омлет с овощами'),
    (12, 'Суп с чесноком и инжиром'),
    (13, 'Свекольный суп'),
    (14, 'Куриные крылышки с гранатом'),
    (15, 'Медовый банановый десерт'),
    (16, 'Малиновый чизкейк'),
    (17, 'Телятина с лавашом'),
    (18, 'Картошка с базиликом'),
    (19, 'Ананасовый смузи'),
    (20, 'Сельдерейный суп')
]

meal_components_data = [
    (11, 1, 3, 150),
    (12, 1, 4, 100),
    (13, 1, 18, 50),
    (14, 2, 7, 200),
    (15, 2, 23, 50),
    (16, 2, 28, 30),
    (17, 2, 35, 20),
    (18, 3, 1, 1),
    (19, 3, 8, 1),
    (20, 3, 29, 50),
    (21, 3, 30, 50),
    (22, 3, 40, 1),
    (23, 4, 4, 150),
    (24, 4, 14, 100),
    (25, 4, 19, 50),
    (26, 4, 22, 30),
    (27, 5, 3, 200),
    (28, 5, 2, 100),
    (29, 5, 6, 150),
    (30, 6, 13, 150),
    (31, 6, 12, 100),
    (32, 6, 8, 1),
    (33, 7, 31, 150),
    (34, 7, 7, 100),
    (35, 8, 10, 100),
    (36, 8, 24, 50),
    (37, 8, 40, 50),
    (38, 9, 14, 50),
    (39, 9, 19, 100),
    (40, 9, 22, 30),
    (41, 10, 16, 200),
    (42, 10, 17, 30),
    (43, 11, 3, 100),
    (44, 11, 4, 50),
    (45, 11, 12, 50),
    (46, 11, 28, 20),
    (47, 11, 35, 10),
    (48, 12, 34, 50),
    (49, 12, 35, 30),
    (50, 12, 42, 10),
    (51, 13, 22, 100),
    (52, 13, 23, 50),
    (53, 13, 34, 30),
    (54, 14, 3, 200),
    (55, 14, 30, 50),
    (56, 14, 31, 30),
    (57, 15, 8, 1),
    (58, 15, 16, 100),
    (59, 15, 26, 50),
    (60, 15, 40, 1),
    (61, 16, 41, 200),
    (62, 16, 24, 100),
    (63, 16, 26, 50),
    (64, 16, 29, 30),
    (65, 16, 40, 1),
    (66, 17, 37, 150),
    (67, 17, 36, 1),
    (68, 18, 12, 150),
    (69, 18, 42, 10),
    (70, 19, 43, 1),
    (71, 19, 1, 1),
    (72, 19, 29, 50),
    (73, 19, 30, 50),
    (74, 20, 35, 50),
    (75, 20, 44, 30),
    (76, 20, 45, 20)
]

# 1. Создать подключение к базе данных
conn = sqlite3.connect('calorie_tracker.db')

# 2. Создать курсор
cursor = conn.cursor()

# 3. Вставить записи в таблицу Products
cursor.executemany('INSERT INTO Products (ProductID, ProductName, CaloriesPer100g) VALUES (?, ?, ?)', products_data)

# 4. Вставить записи в таблицу Meals
cursor.executemany('INSERT INTO Meals (MealID, MealName) VALUES (?, ?)', meals_data)

# 5. Вставить записи в таблицу MealComponents
cursor.executemany('INSERT INTO MealComponents (ComponentID, MealID, ProductID, Quantity) VALUES (?, ?, ?, ?)', meal_components_data)

# 6. Закрыть соединение с базой данных
conn.commit()
conn.close()