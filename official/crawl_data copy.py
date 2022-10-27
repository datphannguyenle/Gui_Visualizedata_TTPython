import requests

base_url = 'http://api.openweathermap.org/data/2.5/forecast?'
api_key = 'ba6a67a16c5be47d1383d19b93965582'
city = 'ho cHi Minh'
url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=' + api_key
time_to_get = 0

def kelvin_to_celius(kelvin):
    celcius = kelvin - 273.15
    return celcius

response = requests.get(url).json()
#Ngay lay thong so
str(response['list'][time_to_get]['dt_txt'])

#Nhiet do theo ngay (*c)
round(kelvin_to_celius(float(response['list'][time_to_get]['main']['temp'])))

#Do am theo ngay (%)
float(response['list'][time_to_get]['main']['humidity'])

#Ap suat khi quyen tren mat dat (hPa))
float(response['list'][time_to_get]['main']['grnd_level'])

#Toc do gio (m/s))
float(response['list'][time_to_get]['wind']['speed'])

#Lay luong mua : Moi ngay lay du lieu 8 lan (cach 3 tieng) + api cho lay 5 ngay -> gioi han la counter = 40
try:
    response['list'][time_to_get]['rain']
except:
    pass