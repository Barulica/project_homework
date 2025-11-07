class Car:

    cars = {
    "Audi": [
        {"model": "A4", "production_year": 2004},
        {"model": "A6", "production_year": 2010},
        {"model": "Q5", "production_year": 2015}
    ],
    "BMW": [
        {"model": "320i", "production_year": 2008},
        {"model": "X3", "production_year": 2013},
        {"model": "M3", "production_year": 2016}
    ],
    "Mercedes": [
        {"model": "C200", "production_year": 2012},
        {"model": "E220", "production_year": 2014},
        {"model": "GLA", "production_year": 2018}
    ],
    "Volkswagen": [
        {"model": "Golf 6", "production_year": 2010},
        {"model": "Passat B7", "production_year": 2011},
        {"model": "Tiguan", "production_year": 2017}
    ],
    "Opel": [
        {"model": "Astra H", "production_year": 2007},
        {"model": "Insignia", "production_year": 2013},
        {"model": "Corsa D", "production_year": 2009}
    ]
}



    def __init__(self):
        self.__brand = None
        self.__model = None
        self.__production_year = None

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if brand not in Car.cars:
            raise ValueError("Invalid brand")
        self.__brand = brand

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model):

        if self.__brand is None:
            raise ValueError("Must be set")
        valid_models = [car['model'] for car in Car.cars[self.__brand]]

        if model not in valid_models:
            raise ValueError("Invalid model")

        self.__model = model

        for car_model in Car.cars[self.__brand]:
            if car_model['model'] == model:
                self.__production_year = car_model['production_year']

    @property
    def production_year(self):
        return self.__production_year

    @production_year.setter
    def production_year(self, production_year):
        if self.__model is None or self.__production_year is not None:
            raise ValueError("Model or production year is None")

        self.__production_year = production_year
audi = Car()

audi.brand = "Audi"
audi.model = "A4"
print(audi.production_year)