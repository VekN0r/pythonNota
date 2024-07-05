import tkinter as tk
import requests #solicituides hhtp a la API
from io import BytesIO #Manejar datos binarios
from PIL import Image, ImageTk #Imagen
import random
def buscarPokemon():
    nombrePokemon = entry_pokemon.get().lower() #Obtener el nombre del pokemon
    url = f"https://pokeapi.co/api/v2/pokemon/{nombrePokemon}"

    response = requests.get(url)#Realizamos una solicitud get con la url

    if response.status_code == 200:#Si el estado del codigo es 200 ta ready
        data = response.json() #Convertimos la respuesta en un foramto json

        nombre = data["name"]
        numero = data["id"]
        tipos = [tipo["type"]["name"] for tipo in data["types"]]

        resultado = f"Nombre: {nombre}\n Numero: {numero}\n Tipo(s):{', '.join(tipos)}"

        imagen_url = data["sprites"]["front_default"]
        response_imagen = requests.get(imagen_url)#Realizamos un get a la imagen
        imagen = Image.open(BytesIO(response_imagen.content))
        imagen = imagen.resize((300,300), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(imagen)#Convertimos la imagen para trabajar con tkinter
        label_imagen.config(image=foto)#Configura label para mostrar la foto
        label_imagen.image = foto#Guarda una referencia a la imagen para evitar que sea eliminada por el recolector de basura
    else:
        
        label_imagen.config(image="")
        resultado = "No se encontro al aweonao del pokemon, sigue buscando larva"
       

    label_resultado.config(text=resultado)        
def buscarPokemonA():
    alPokemon = random.randint(0,1026)
    url = f"https://pokeapi.co/api/v2/pokemon/{alPokemon}"

    url3 = f"https://pokeapi.co/api/v2/pokemon-species/{alPokemon}"

    response = requests.get(url)#Realizamos una solicitud get con la url
    response2 = requests.get(url3)
    if response2.status_code == 200:
        dates = response2.json()
    if response.status_code == 200:#Si el estado del codigo es 200 ta ready
        data = response.json() #Convertimos la respuesta en un foramto json

        nombre = data["name"]
        numero = data["id"]
        altura = data["height"]
        especie = dates["name"]
        color = dates["color"]["name"]
        forma = dates["shape"]["name"]
        tipos = [tipo["type"]["name"] for tipo in data["types"]]
        stats = [(stat["stat"]["name"],stat["base_stat"]) for stat in data["stats"]]
        

        resultado = f"Nombre: {nombre}\nNúmero: {numero}\nTipo(s): {', '.join(tipos)}\nAltura: {altura}\nCARACTERISTICAS {color,forma,especie}\n"
        for stat_name, stat_value in stats:
            resultado += f"{stat_name}: {stat_value}\n"

            # Mostrar cada estadística una por una
            label_resultado.config(text=resultado)
            window.update()  # Actualizar la ventana para mostrar el cambio
        imagen_url = data["sprites"]["front_default"]
        response_imagen = requests.get(imagen_url)#Realizamos un get a la imagen
        imagen = Image.open(BytesIO(response_imagen.content))
        imagen = imagen.resize((300,300), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(imagen)#Convertimos la imagen para trabajar con tkinter
        label_imagen.config(image=foto)#Configura label para mostrar la foto
        label_imagen.image = foto#Guarda una referencia a la imagen para evitar que sea eliminada por el recolector de basura
    else:
        label_imagen.config(Image="") 
        resultado = "No se encontro al aweonao del pokemon, sigue buscando larva"
        

    label_resultado.config(text=resultado) 

def buscarDigimon():
    nombreDigimon = entry_digimon.get().lower()
    urlDigimon = f"https://digi-api.com/api/v1/digimon/{nombreDigimon}"
    responseDigimon = requests.get(urlDigimon)
    if responseDigimon.status_code == 200:
        dataD = responseDigimon.json()
        nombre = dataD["name"]

        resul = f"Nombre: {nombre}"

        imagen_url = dataD["sprites"]["front_default"]
        response_imagenD = requests.get(imagen_url)#Realizamos un get a la imagen
        imagen = Image.open(BytesIO(response_imagenD.content))
        imagen = imagen.resize((300,300), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(imagen)#Convertimos la imagen para trabajar con tkinter
        label_imagen.config(image=foto)#Configura label para mostrar la foto
        label_imagen.image = foto#Guarda una referencia a la imagen para evitar que sea eliminada por el recolector de basura
    else:
        label_imagen.config(image="")
        resul = "No se encontro al aweonao del digimon, sigue buscando larva"
    
    label_resultadoD.config(text=resul)

window = tk.Tk()#Creo la ventana principal
window.title("Encuentra tu pokemon")

saludos = tk.Label(window,text="Saludos, Ingrese su pokemon a buscar")
saludos.pack()

label_pokemon = tk.Label(window)
label_pokemon.pack()

entry_pokemon = tk.Entry(window)
entry_pokemon.pack()

entry_digimon = tk.Entry(window)
entry_digimon.pack()

button_buscarD = tk.Button(window, text="Buscar Digimon",command=buscarDigimon)
button_buscarD.pack()

button_buscar = tk.Button(window, text="Buscar", command=buscarPokemon)
button_buscar.pack()

aleatorio_buscar = tk.Button(window, text="Aleatorio", command=buscarPokemonA)
aleatorio_buscar.pack()

def clearTextInput():
    entry_pokemon.delete(0, "end")
    if label_pokemon:
        label_pokemon.config(text="que es esto")
    if label_resultado:
        label_resultado.config(text="y estoasd")
    if label_imagen:
        label_imagen.config(image="")

    button_buscar.config(state="normal")
    aleatorio_buscar.config(state="normal")


btnRead = tk.Button(window,text="Limpiar", command=clearTextInput)
btnRead.pack()

label_resultado = tk.Label(window, text="")#Creamos una etiqueta vacia para mostrar el resultado por ventana
label_resultado.pack()

label_resultadoD = tk.Label(window, text="")#Creamos una etiqueta vacia para mostrar el resultado por ventana
label_resultadoD.pack()

label_imagen = tk.Label(window)
label_imagen.pack()

window.mainloop()