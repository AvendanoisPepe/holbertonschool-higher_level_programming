#!/usr/bin/python3
"""Este módulo contiene métodos sobre la creación y manejo de Objetos SingleLinkedList y Node.
"""


class Node():
    def __init__(self, data, next_node=None):
        """Inicializamos los datos del nodo
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """Obtenemos el valor de datos de  un nodo
        """
        return self.__data
    
    @data.setter
    def data(self, value):
        """Manipulacion del valor del dato del nodo
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Obtener el siguiente nodo del nodo existente.
        """
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """Manipular el valor del dato del siguiente nodo
        """
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList():
    def __init__(self):
        """Inicializamos la lista.
        """
        self.__head = None
    
    def insert(self):
        nuevo = ""
        node = self.__head
        while node is not None:
            nuevo = nuevo + str(node.data) + '\n'
            node = node.next_nodo
        return (nuevo[:-1])

    def sorted_insert(self, value):
        node = self.__head
        if self.__head.data >= value:
            self.__head = Node(value, self.__head)
        