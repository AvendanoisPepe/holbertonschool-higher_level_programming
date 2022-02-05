![](https://parzibyte.me/blog/wp-content/uploads/2018/12/Leer-archivos-de-texto-con-Python.png)

# 0x0C. Python - Almost a circle

------------

## General

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

------------

## List of poinst.

|  Point | What is done at this point? | level |
| ------------ | ------------ | ------------ |
| tests/ | All your files, classes and methods must be unit tested and be PEP 8 validated. | Mandatory |
| models/base.py | This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs) | Mandatory |
| models/rectangle.py | Write the class Rectangle that inherits from Base: | Mandatory |
| models/rectangle.py | Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded): | Mandatory |
| models/rectangle.py | Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.| Mandatory |
| models/rectangle.py | Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height> | Mandatory |
| models/rectangle.py | Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y | Mandatory |
| models/rectangle.py | Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute: | Mandatory |
| models/rectangle.py | Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes: | Mandatory |
| models/square.py | Write the class Square that inherits from Rectangle: | Mandatory |
| models/square.py | Update the class Square by adding the public getter and setter size | Mandatory |
| models/square.py | Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes: | Mandatory | 
| models/rectangle.py | Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle: | Mandatory |
| models/square.py | Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square: | Mandatory |
| models/base.py | JSON is one of the standard formats for sharing data representation. | Mandatory |
| models/base.py | Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file: | Mandatory |
| models/base.py | Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file: | Mandatoy |
| models/base.py | Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string: | Mandatory |
| models/base.py | Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set: | Mandatory |
| models/base.py | Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances: | Mandatory |

------------

## List of repository files:

|  Point | own comments.  | level |
| ------------ | ------------ | ------------ |
| tests/ | Testing de su chinita | Mandatory |
| models/base.py | se inicializa el id (int): el identificador del objeto Base. | Mandatory |
| models/rectangle.py | Generamos los getters and setters del rectangulo | Mandatory |
| models/rectangle.py | Agregamos las condicionales correspondientes | Mandatory |
| models/rectangle.py | Imprime un rectangulo con el caracter # | Mandatory |
| models/rectangle.py | Imprime la descripcion de un rectangulo | Mandatory |
| models/rectangle.py | Ahora se maneja x y y en la funcion diplay | Mandatory |
| models/rectangle.py | Actualiza los atributos de la instancia | Mandatory |
| models/rectangle.py | asigna un argumento clave/valor a los atributos: | Mandatory |
| models/square.py | Generamos el constructor con los atributos heredados | Mandatory |
| models/square.py | Generamos los getters and setters de size | Mandatory |
| models/square.py | Actualiza los atributos de la instancia | Mandatory |
| models/rectangle.py | Returna una representacion de el rectangle en un diccionario. | Mandatory |
| models/square.py | Returna una representacion de el cuadrado en un diccionario. | Mandatory |
| models/base.py | Representamos un objeto json en forma de cadena | Mandatory |
| models/base.py | Creamos un archivo .json con contenido de cadenas de bibliotecas | Mandatory |
| models/base.py | Devuelve la lista de la representación de cadena JSON | Mandatory |
| models/base.py | Returnamos con datos ficticios la funcion update en created |  Mandatory |
| models/base.py  | Usando dos metodos anteriores creamos un nuevo archivo con un diccionario de listas | Mandatory |

------------

# Documentation:

### Links:

- https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/
- https://docs.python.org/3/library/json.html
- https://docs.python.org/3.4/library/unittest.html#module-unittest
- https://www.pythonsheets.com/notes/python-tests.html

------------

# Author


## Juan Sebastian Avendaño Gonzalez:
- Git: https://github.com/AvendanoisPepe
- Twitter: https://twitter.com/Sebastian_Aven
- Linkedin: https://www.linkedin.com/in/juan-sebastian-avenda%C3%B1o-gonz%C3%A1lez-8b1185200/

------------

![](https://scontent.fbog4-1.fna.fbcdn.net/v/t39.30808-6/271153206_3074657909465585_6907762404450913633_n.jpg?_nc_cat=105&_nc_rgb565=1&ccb=1-5&_nc_sid=730e14&_nc_ohc=Wm9imN7mxqAAX_DgRTy&_nc_ht=scontent.fbog4-1.fna&oh=00_AT9bMuywrpnZKR3yaTAPu-lqwQ0uJpFTGIYQPM2wabvWlg&oe=61EB1180)