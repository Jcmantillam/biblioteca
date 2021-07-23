# biblioteca
Proyecto en python django para buscar y almacenar información, permitiendo la consulta a los APIs de Google books y Oreilly

#Instalación
Se descarga el proyecto, y se va a la ubicación del direcotrio principal, se utilizan los siguientes comandos:
```
git clone https://github.com/Jcmantillam/biblioteca.git
cd biblioteca
pip install -r requirements.txt
python manage.py migrate
```
#Servicios
Los servicios principales son el de búsqueda, guardar un libro y eliminar un libro. Adicionalmente, se puede utilizar le servicio ofrecido por Django Rest framework consultar los libros guardados, o crear un super usuario para Django Admin.  A continuación se explica cada servicio:

**Search Book**
Este servicio permite buscar información de libros tanto en la BD local, como en los servicios externos soportados `GoogleBooks` y `Oreilly`
----
  <Retorna un json con los resultado encontrados, si no hay datos en la BD local, busca en el servicio alternativo indicado>
 
 * **URL**

  <api/v1/search_book/>
 
 * **Método:**
  `GET`

* **Parámetros de datos**
**Requeridos:**
  `search_term=[String]`
  `alternative_service:[Char]`
 <`search_term` es el término buscado, mientras que `alternative_service` determina qué API externa se usará, G para Google y O para O'reilly>

* **Respuesta:**
  
  BD Local
  * **Code:** 200
    **Content:**
  ```
  [
    {
        "id": 5,
        "title": "Python machine learning",
        "subtitle": "aprendizaje automático y aprendizaje profundo con Python, scikit-learn y TensorFlow",
        "release_date": "2019-01-01",
        "image": null,
        "description": "Not found",
        "editor": 5,
        "authors": [
            8,
            9
        ],
        "categories": [
            17
        ],
        "service": "local"
    }
  ]
  ``` 
  
 
