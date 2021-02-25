from tkinter import * # importamos todo de tkinter
import requests
#cf132075fa76ae921b4bab3239821e50
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def mostrar_respuesta(clima):# cremos la funcion para mostrar el clima por pantalla
    try:
      nombre_ciudad = clima["name"]
      descrip = clima["weather"][0]["description"]
      temp = clima["main"]["temp"]
      sen_like = clima["main"]['feels_like']
      max_temp = clima["main"]['temp_max']

      ciudad["text"]=nombre_ciudad#ingresamos el nombre de  las variables para que se vena por pantalla
      temperatura["text"]=  str (int(temp)) + "C"
      descripcion["text"]=descrip
      sensacion_termica["text"]=str(sen_like) + "  sensacion termica"
      temperatura_max["text"]=str (max_temp)+ "   maxima para hoy "
    except:ciudad["text"]="INTENTA NUEVAMENTE"



def clima(ciudad):#se crea la funcion para obtener los datos del clima
    try:# manejo de errores
      API_key="cf132075fa76ae921b4bab3239821e50"#compiamos la api de la pag openweathermap
      URL_key="https://api.openweathermap.org/data/2.5/weather"
      parametros ={'appID':API_key,"q":ciudad, "units":"metric","lang":"es"}# le indicamos como queremos las medidas de medicion del clima
      response = requests.get(URL_key,params=parametros)
      clima = response.json()
      mostrar_respuesta(clima)
      print(clima["name"])
      print(clima["weather"][0]["description"])
      print(clima["main"]["temp"])
      print(clima["main"]['feels_like'])
      print(clima["main"]['temp_max'])
    except:
        print("ERROR")





#creamos la ventana y su forma
ventana = Tk()
ventana.geometry ("500x600")#le damos el tamano  a la ventana
texto_ciudad = Entry(ventana,font=("courier",20,"normal"),justify="center")#le creamos la entrada de texto  le damos la fuente y centramos el cursor
texto_ciudad.pack(padx=30,pady=30)
obtener_clima=Button(ventana,text='OBTENER CLIMA',font=("courier",20,"normal"),command=lambda:clima(texto_ciudad.get()))#creamos boton de obtner el clima,creamos la funcion para obtenr los datos
obtener_clima.pack()
#creamos las etiquetas de nuestra app
ciudad=Label(font=("courier",20 ,"normal"))
ciudad.pack(padx=30,pady=30)

temperatura=Label(font=("Bintank",30 ,"normal"))
temperatura.pack(padx=30,pady=25)

descripcion=Label(font=("courier",20 ,"normal"))
descripcion.pack(padx=10,pady=10)

sensacion_termica=Label(font=("courier",20 ,"normal"))
sensacion_termica.pack(padx=10,pady=10)

temperatura_max=Label(font=("courier",20 ,"normal"))
temperatura_max.pack(padx=10,pady=10)




ventana.mainloop()


