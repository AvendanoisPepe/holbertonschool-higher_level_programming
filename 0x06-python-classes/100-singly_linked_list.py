#!/usr/bin/python3
"""Este módulo contiene métodos sobre la creación
y manejo de Objetos SingleLinkedList y Node.
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


"""En esta clase agragamos los nodos a la nueva
SingleLinkedList
"""


class SinglyLinkedList():
    def __init__(self):
        """Inicializamos la lista.
        """
        self.__head = None

    def sorted_insert(self, value):
        """Generamos las condicionales para verificar
        si es nulo seguido de como agregarlo y despues
        un ciclo que lo agrega.
        """
        if self.__head is None:
            self.__head = Node(value)
        elif value < self.__head.data:
            self.__head = Node(value, self.__head)
        else:
            __current = self.__head
            while __current.next_node is not None:
                if value < __current.next_node.data:
                    break
                __current = __current.next_node
            __current.next_node = Node(value, __current.next_node)

    def __str__(self):
        """En la lista agregamos con append el contenido
        convertido con str y lo unimos con join"""
        __current = self.__head
        listasa = []
        while __current is not None:
            listasa.append(str(__current.data))
            __current = __current.next_node
        return '\n'.join(listasa)
