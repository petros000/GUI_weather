import requests


class Weather:
    USER_KEY = 'c39185aed07be0cc7121e07f30cd6867'
    URL_BASE = 'https://api.openweathermap.org//data//2.5//'

    def __init__(self, city_name, country_code=''):
        print(city_name)
        self.city_name = 'Moscow'
        self.country_code = 'RU'

        if self.__is_valid_data(city_name):
            self.city_name = city_name
        if self.__is_valid_data(country_code) or country_code == "":
            self.country_code = country_code

        self.city = ','.join([self.city_name, self.country_code])
        self.params = {'q': self.city, 'units': 'metric', 'appid': self.USER_KEY}

    @classmethod
    def __is_valid_data(cls, text):
        if type(text) is str and text.isalpha():
            return True
        return False

    @staticmethod
    def parsing_data(data: list) -> tuple:
        out_time = []
        out_temp = []
        for d in data:
            out_time.append(d['dt_txt'])
            out_temp.append(d['main']['temp'])
        return (out_time, out_temp)

    def call_current_weather_data(self):
        url = self.URL_BASE + 'weather'
        response = requests.get(url, self.params).json()
        return response['main']['temp']

    def call_5_day_3hour_forecast_data(self):
        url = self.URL_BASE + 'forecast'
        response = requests.get(url, self.params).json()['list']
        return self.parsing_data(response)
        # return response

#w = Weather('Moscow')
#print(w.call_current_weather_data())
# print(w.call_5_day_3hour_forecast_data())
