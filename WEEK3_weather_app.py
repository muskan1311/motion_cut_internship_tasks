from tkinter import *
import tkinter as tk

import requests
import time
 

def getWeather(app):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=36fe1c2661ba7e3a136abd0ed659fc54"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    

    w1_label.config(text= condition)
    temp1_label.config(text= str(temp) + "°C" )
    mintemp1_label.config(text= str(min_temp))
    maxtemp1_label.config(text= str(max_temp))
    pressure1_label.config(text= str(pressure))
    humidity1_label.config(text= str(humidity))
    wind1_label.config(text= str(wind))
    sunrise1_label.config(text= sunrise)
    sunset1_label.config(text= sunset)




app = tk.Tk()
app.geometry("900x1500")
app.title("Weather App")
app.config(bg= "pink")



name_label = tk.Label(app,bg = "white",text = "WEATHER APP",font= ("helvetica",20,"bold"))
name_label.place(x=235,y= 50, height=70,width=450)



textField = tk.Entry(app, justify='center', font= ("helvetica",15))
textField.place(x= 235,y =180,height= 50, width= 450)
textField.focus()
textField.bind('<Return>', getWeather)



w_label = tk.Label(app,bg = "hotpink",text = "Weather climate",font= ("helvetica",10,"bold"))
w_label.place(x=25,y= 350, height=50,width=350)
w1_label = tk.Label(app,bg = "hotpink",text = "",font= ("helvetica",10,"bold"))
w1_label.place(x=500,y= 350, height=50,width=350)

temp_label = tk.Label(app,bg = "hotpink",text = "Tempratue",font= ("helvetica",10,"bold"))
temp_label.place(x=25,y= 450, height=50,width=350)
temp1_label = tk.Label(app,bg = "hotpink",text = "",font= ("helvetica",10,"bold"))
temp1_label.place(x=500,y= 450, height=50,width=350)

mintemp_label = tk.Label(app,bg = "hotpink",text = "Minimum Temprture",font= ("helvetica",10,"bold"))
mintemp_label.place(x=25,y= 550, height=50,width=350)
mintemp1_label = tk.Label(app,bg = "hotpink",text = "",font= ("helvetica",10,"bold"))
mintemp1_label.place(x=500,y= 550, height=50,width=350)

maxtemp_label = tk.Label(app,bg = "hotpink",text = "Maximum Temprature",font= ("helvetica",10,"bold"))
maxtemp_label.place(x=25,y= 650, height=50,width=350)
maxtemp1_label = tk.Label(app,bg = "hotpink",text = "",font= ("helvetica",10,"bold"))
maxtemp1_label.place(x=500,y= 650, height=50,width=350)

humidity_label = tk.Label(app,bg = "hotpink",text = "Humidity",font= ("helvetica",10,"bold"))
humidity_label.place(x=25,y= 750, height=50,width=350)
humidity1_label = tk.Label(app,bg = "hotpink",text = "",font= ("helvetica",10,"bold"))
humidity1_label.place(x=500,y= 750, height=50,width=350)

pressure_label = tk.Label(app,bg = "hotpink",text = "Pressure",font= ("helvetica",10,"bold"))
pressure_label.place(x=25,y= 850, height=50,width=350)
pressure1_label = tk.Label(app,bg = "hotpink",text = "",font= ("helvetica",10,"bold"))
pressure1_label.place(x=500,y= 850, height=50,width=350)

wind_label = tk.Label(app,bg = "hotpink",text = "Wind Speed",font= ("helvetica",10,"bold"))
wind_label.place(x=25,y= 950, height=50,width=350)
wind1_label = tk.Label(app,bg = "hotpink",text = "",font= ("helvetica",10,"bold"))
wind1_label.place(x=500,y= 950, height=50,width=350)

sunrise_label = tk.Label(app,bg = "hotpink",text = "Sunrise",font= ("helvetica",10,"bold"))
sunrise_label.place(x=25,y= 1050, height=50,width=350)
sunrise1_label = tk.Label(app,bg = "hotpink",text = "",font= ("helvetica",10,"bold"))
sunrise1_label.place(x=500,y= 1050, height=50,width=350)

sunset_label = tk.Label(app,bg = "hotpink",text = "Sunset",font= ("helvetica",10,"bold"))
sunset_label.place(x=25,y= 1150, height=50,width=350)
sunset1_label = tk.Label(app,bg = "hotpink",text = "",font= ("helvetica",10,"bold"))
sunset1_label.place(x=500,y= 1150, height=50,width=350)


app.mainloop()