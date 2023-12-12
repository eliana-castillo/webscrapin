import requests
from bs4 import BeautifulSoup
import pandas as pd

Nombres = list()
Apellidos = list()
Cursos = list()
url = 'http://127.0.0.1:8000/'
html_doc= requests.get(url)
print(html_doc)
soup = BeautifulSoup(html_doc.text,'html.parser')
data = soup.find_all(name='td',attrs={"class":"table_primary"})

tabla = soup.find('table')

# obtener las filas de la tabla
filas = tabla.find_all('tr')

# iterar sobre las filas e imprimir los datos
    for fila in filas:
#obtener las celdas de las filas
        celdas = filas.find_all('td')
        if len(celdas)>0:
            Nombres.append(celdas[0].string)
            Apellidos.append(celdas[1].string)
           Cursos.append(celdas[2].string)


print(Apellidos)
print(Nombres)
print(Cursos)

df = pd.DataFrame({'Nombres':Nombres, 'Apellidos':Apellidos, 'Cursos':Cursos})
df.to_csv(path_or_buf='docentes.csv', index=False, encoding='utf-8')





