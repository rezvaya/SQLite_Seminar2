from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QInputDialog


class ConsolePrinter:
    @staticmethod
    def print_result(message):
        print(message)


class Presenter:
    def __init__(self, ingredient_service, meal_service, view):
        self.ingredient_service = ingredient_service
        self.meal_service = meal_service
        self.view = view

    def run(self):
        while True:
            self.view.show_menu()

            choice = self.view.get_user_input()

            if choice == '0':
                break

            user_input = self.view.get_user_input("Введите название: ").capitalize()

            if choice == '1':
                self.view.show_result(
                    f"Количество калорий в {user_input}: {self.ingredient_service.find_calories_by_ingredient(user_input)} ккал на 100 грамм")
            elif choice == '2':
                result = self.meal_service.get_ingredients_by_meal(user_input)
                if result:
                    for meal_name, ingredients in result.items():
                        self.view.show_result(f"Ингредиенты в блюде '{meal_name}':")
                        for ingredient in ingredients:
                            self.view.show_result(f"---{ingredient}")
                else:
                    self.view.show_result(f"Блюдо '{user_input}' не найдено")
            elif choice == '3':
                total_calories = self.meal_service.calculate_calories_for_meal(user_input)
                self.view.show_result(
                    f"Общее количество калорий в блюде '{user_input}': {total_calories} ккал" if total_calories is not None else f"Блюдо '{user_input}' не найдено")
            else:
                self.view.show_result("Некорректный ввод. Пожалуйста, выберите корректное действие.")


class View:
    @staticmethod
    def show_menu():
        print("\nВыберите действие:")
        print("1. Найти количество калорий в ингредиенте")
        print("2. Получить ингредиенты в блюде")
        print("3. Рассчитать общее количество калорий в блюде")
        print("0. Выход")

    @staticmethod
    def get_user_input(prompt="Введите номер действия: "):
        return input(prompt)

    @staticmethod
    def show_result(message):
        print(message)



class CalorieTrackerApp(QWidget):
    def __init__(self, presenter):
        super().__init__()

        self.presenter = presenter

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Calorie Tracker')
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        self.menu_label = QLabel('Выберите действие:')
        layout.addWidget(self.menu_label)

        self.menu_button_1 = QPushButton('1. Найти количество калорий в ингредиенте')
        self.menu_button_1.clicked.connect(self.handle_menu_button_1)
        layout.addWidget(self.menu_button_1)

        self.menu_button_2 = QPushButton('2. Получить ингредиенты в блюде')
        self.menu_button_2.clicked.connect(self.handle_menu_button_2)
        layout.addWidget(self.menu_button_2)

        self.menu_button_3 = QPushButton('3. Рассчитать общее количество калорий в блюде')
        self.menu_button_3.clicked.connect(self.handle_menu_button_3)
        layout.addWidget(self.menu_button_3)

        self.menu_button_exit = QPushButton('0. Выход')
        self.menu_button_exit.clicked.connect(self.handle_menu_button_exit)
        layout.addWidget(self.menu_button_exit)

        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def handle_menu_button_1(self):
        ingredient_name, ok = self.get_user_input('Введите название ингредиента:')
        if ok:
            result = self.presenter.ingredient_service.find_calories_by_ingredient(ingredient_name)
            self.show_result(result)
            print(result)

    def handle_menu_button_2(self):
        meal_name, ok = self.get_user_input('Введите название блюда:')
        if ok:
            result = self.presenter.meal_service.get_ingredients_by_meal(meal_name)
            self.show_result(result)

    def handle_menu_button_3(self):
        meal_name, ok = self.get_user_input('Введите название блюда:')
        if ok:
            result = self.presenter.meal_service.calculate_calories_for_meal(meal_name)
            self.show_result(result)

    def handle_menu_button_exit(self):
        self.close()

    def get_user_input(self, prompt):
        text, ok = QInputDialog.getText(self, "Input", prompt)
        return text, ok

    def show_result(self, result):
        if result is not None:
            self.result_label.setText(str(result))
        else:
            self.result_label.setText("Результат не найден.")

