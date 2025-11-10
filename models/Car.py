from datetime import datetime

from models.Db import Db

class Car(Db):

    def __init__(self):
        super().__init__()
        self.__brand = None
        self.__model = None
        self.__production_year = None


    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        cursor = self._connection.cursor()
        cursor.execute('SELECT DISTINCT brand FROM cars')
        brands_raw = cursor.fetchall()
        self._connection.commit()
        cursor.close()

        brands = [b[0] for b in brands_raw]

        if brand not in brands:
            raise ValueError("Invalid brand")
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        cursor = self._connection.cursor()
        cursor.execute('SELECT model FROM cars')
        models_raw = cursor.fetchall()
        self._connection.commit()
        cursor.close()

        models = [m[0] for m in models_raw]

        if model not in models:
            raise ValueError("Invalid model")
        self.__model = model


    @property
    def production_year(self):
        return self.__production_year

    @production_year.setter
    def production_year(self, production_year):
        production_year = int(production_year)

        cursor = self._connection.cursor()
        cursor.execute('SELECT production_year FROM cars')
        production_years_raw = cursor.fetchall()
        self._connection.commit()
        cursor.close()

        production_years = [p[0] for p in production_years_raw]

        if production_year not in production_years:
            raise ValueError("Invalid year")
        self.__production_year = production_year


    def show_rented_or_available_cars(self, option):
        cursor = self._connection.cursor()
        option = str(option)
        if option == "3":
            cursor.execute('SELECT * FROM cars WHERE rented = True')
        else:
            cursor.execute('SELECT * FROM cars WHERE rented = False')
        result = cursor.fetchall()
        cursor.close()

        return result
    def available_to_rent_by_id(self,id):
        cursor = self._connection.cursor()
        cursor.execute('''SELECT rented, brand, model, production_year FROM cars WHERE id = %s''', (id,))
        result = cursor.fetchone()
        cursor.close()

        if result is None:
            return None

        return {
            "rented": result[0],
            "brand": result[1],
            "model": result[2],
            "production_year": result[3]
        }


    def available_to_rent_by_brand(self, brand, model, production_year):
        cursor = self._connection.cursor()
        cursor.execute("SELECT rented FROM cars WHERE brand = %s AND model = %s AND production_year = %s", (brand, model, str(production_year)))
        result = cursor.fetchone()
        cursor.close()


        if result is None:
            return None

        return result[0]

    def rent_a_car(self):
        cursor = self._connection.cursor()
        cursor.execute('''UPDATE cars SET rented = FALSE, car_rented_until = date_trunc('minute', NOW() + INTERVAL '7 days') WHERE brand = %s and model = %s and production_year = %s''',
                       (self.brand, self.model, self.production_year))

        cursor.execute('''SELECT car_rented_until FROM cars WHERE brand = %s AND model = %s AND production_year = %s''', (self.brand, self.model, self.production_year))
        result = cursor.fetchone()

        self._connection.commit()
        cursor.close()

        return result[0] if result else None

    def format_cars_table(self, cars):
        print(f"{'ID':<3} {'Marka':<10} {'Model':<10} {'Godina':<6} {'Rented':<8} {'Remaining Time':<20}")
        print("-" * 60)
        for car in cars:
            car_id, brand, model, year, rented, rented_until = car
            if rented_until:
                remaining = rented_until - datetime.now()
                if remaining.days >= 1:
                    remaining_str = f"{remaining.days} days"
                else:
                    remaining_hours = remaining.total_seconds() / 3600
                    remaining_str  = f"{int(remaining_hours)} hours"
            else:
                remaining_str = "N/A"

            print(f"{car_id:<3} {brand:<10} {model:<10} {year:<6} {str(rented):<8} {remaining_str:<20}")







