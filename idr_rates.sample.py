import requests

#json_data = requests.get('https://www.floatrates.com/daily/idr.json')
json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.6780516976557e-5,"date":"Fri, 21 Jul 2023 02:55:01 GMT","inverseRate":14974.427352083},"eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.9759418372504e-5,"date":"Fri, 21 Jul 2023 02:55:01 GMT","inverseRate":16733.763936031}}

for data in json_data.values():
     print(data['code'])
     print(data['name'])
     print(data['date'])
     print(data['inverseRate'])
