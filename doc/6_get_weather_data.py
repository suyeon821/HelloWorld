import json

with open('./6_sample_api.json') as data_file:
    data = json.load(data_file)
    toCelsius = data['main']['temp'] - 273
    weather = data['weather'][0]['main']
    s = "온도는 %f 입니다." % toCelsius

    f = open("C:/Users/suyeo/Desktop/practice.txt","w")
    f.write(s)
    f.close()