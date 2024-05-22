import os
import requests
from bs4 import BeautifulSoup

# crear carpetas si no existen
if not os.path.exists('images'):
    os.makedirs('images')

url = 'https://www.google.com/search?sca_esv=8b3c2fe050857b40&sxsrf=ADLYWILNxvLDeiVg4-QhhNAhiwdMHlQgOw:1716381846051&q=burros&tbm=isch&source=lnms&sa=X&ved=2ahUKEwij8-3RpKGGAxWxu5UCHbTVBJUQ0pQJegQIDRAB&biw=1366&bih=647&dpr=1'

# realizamos la petición y pasarle el texto plano a BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# traemos todas las etiquetas img.
results = soup.find_all('img')

# filtrar los resultados
results = [img for img in results if img["src"].startswith("https://")]

# definimos las extensiones permitidas
permited_extensions = {
    'image/jpeg',
    'image/png',
    'image/webp',
}

# se descargan cada una de las imagenes
for i, img in enumerate(results, start=1):
    filename = f'Imagen-{i}.jpg'
    result_image = requests.get(img["src"])

    # comprobar que la imagen tiene el formato permitido
    if (result_image.headers.get('content-type') in permited_extensions):
        with open(f'images/{filename}', 'wb') as file:
            file.write(result_image.content)

print("Imagenes descargadas exitosamente")