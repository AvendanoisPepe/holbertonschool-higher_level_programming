![](https://parzibyte.me/blog/wp-content/uploads/2018/12/Leer-archivos-de-texto-con-Python.png)

# 0x0B. Python - Input/Output

------------

## General

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

------------

## List of poinst.

|  Point | What is done at this point? | level |
| ------------ | ------------ | ------------ |
| 0-read_file.py | Write a function that reads a text file (UTF8) and prints it to stdout: | Mandatory |
| 1-write_file.py | Write a function that writes a string to a text file (UTF8) and returns the number of characters written: | Mandatory |
| 2-append_write.py | Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added: | Mandatory |
| 3-to_json_string.py | Write a function that returns the JSON representation of an object (string): | Mandatory |
| 4-from_json_string.py | Write a function that returns an object (Python data structure) represented by a JSON string: | Mandatory |
| 5-save_to_json_file.py | Write a function that writes an Object to a text file, using a JSON representation: | Mandatory |
| 6-load_from_json_file.py | Write a function that creates an Object from a “JSON file”: | Mandatory |
| 7-add_item.py | Write a script that adds all arguments to a Python list, and then save them to a file: | Mandatory |

------------

## List of repository files:

|  Point | own comments.  | level |
| ------------ | ------------ | ------------ |
| 0-read_file.py | Open abre el archivo y returna su objeto | Mandatory |
| 1-write_file.py | La escritura de una cadena o secuencia de bytes (para archivos binarios) se realiza mediante el método write(). Este método devuelve el número de caracteres escritos en el archivo. | Mandatory |
| 2-append_write.py | usamos write para el retorno de los caracteres contados y "a" en open->mode para agregar una cadena al final | Mandatory |
| 3-to_json_string.py | La función json.dumps() convierte un objeto Python en una cadena json. | Mandatory |
| 4-from_json_string.py |  El método json.loads() se puede utilizar para analizar una cadena JSON válida y convertirla en un diccionario de Python | Mandatory |
| 5-save_to_json_file.py | Combinamos lo aprendido anteriormente mandado la funcion json en el write | Mandatory |
| 6-load_from_json_file.py | load() lee el archivo en formato json | Mandatory |
| 7-add_item.py | Usando la logica de argv se soluciona todo papi | Mandatory |

------------

# Documentation:

### Links:

- https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- https://www.programiz.com/python-programming/methods/built-in/open
- https://www.programiz.com/python-programming/file-operation

------------

# Author


## Juan Sebastian Avendaño Gonzalez:
- Git: https://github.com/AvendanoisPepe
- Twitter: https://twitter.com/Sebastian_Aven
- Linkedin: https://www.linkedin.com/in/juan-sebastian-avenda%C3%B1o-gonz%C3%A1lez-8b1185200/
- https://docs.python.org/3/library/json.html#json.dumps
- https://www.geeksforgeeks.org/json-dumps-in-python/

------------


![](https://scontent.fbog4-1.fna.fbcdn.net/v/t39.30808-6/271153206_3074657909465585_6907762404450913633_n.jpg?_nc_cat=105&_nc_rgb565=1&ccb=1-5&_nc_sid=730e14&_nc_ohc=Wm9imN7mxqAAX_DgRTy&_nc_ht=scontent.fbog4-1.fna&oh=00_AT9bMuywrpnZKR3yaTAPu-lqwQ0uJpFTGIYQPM2wabvWlg&oe=61EB1180)