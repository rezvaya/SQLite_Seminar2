from database import DatabaseConnection
from services import IngredientService, MealService
from ui import ConsolePrinter, Presenter, View, CalorieTrackerApp
from PySide6.QtWidgets import QApplication


app = QApplication([])

db = DatabaseConnection()
ingredient_service = IngredientService(db)
meal_service = MealService(db)
view = CalorieTrackerApp(Presenter(ingredient_service, meal_service, None))

view.show()

app.exec_()

