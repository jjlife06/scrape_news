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
    titulares = soup.find_all("h2", class_="c_t") # la clase depende del sitio web

    for titular in titulares:
        enlace = titular.find("a")["href"]
        noticias.append({"titular" : titular.text, "enlace" : enlace})

    return render_template("index.html", noticias = noticias)

if __name__ == "__main__":
    app.run(debug=True)