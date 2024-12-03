from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://www.elpais.com/" # url de la web de noticias
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    noticias = []
   # Refactorizamos para cargar artículo
   #  titulares = soup.find_all("h2", class_="c_t") 
    articulos = soup.find_all("article", class_="c c-d c--m") # la clase depende del sitio web

    #for titular in titulares:
    for articulo in articulos:
        try:
            titular = articulo.find("h2", class_="c_t")
            enlace = titular.find("a")["href"]
            imagen = articulo.find("img")
            if imagen:
                imagen = imagen["src"] # Extraemos url de la imagen
            else:
                imagen = None 
            noticias.append({"titular" : titular.text, "enlace" : enlace, "imagen" : imagen})
        except KeyError:
            print("KeyError")

    return render_template("index.html", noticias = noticias)

if __name__ == "__main__":
    app.run(debug=True)