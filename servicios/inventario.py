import json
import os
from modelos.producto import Producto


class Inventario:
    """
    gestión del inventario.
    """

    def __init__(self, archivo='inventario.json'):
        # DICCIONARIO: almacenamiento principal
        self._productos = {}

        # CONJUNTO (SET): almacena nombres únicos
        # Evita productos con nombre duplicado
        self._nombres_unicos = set()

        self._next_id = 1
        self._archivo = archivo
        self.cargar_desde_archivo()

    def añadir_producto(self, nombre, cantidad, precio):

        # Validación usando SET
        if nombre.lower() in self._nombres_unicos:
            raise ValueError("Ya existe un producto con ese nombre.")

        producto = Producto(self._next_id, nombre, cantidad, precio)

        # Diccionario
        self._productos[self._next_id] = producto

        # Agregamos al SET
        self._nombres_unicos.add(nombre.lower())

        self._next_id += 1
        self.guardar_en_archivo()

        return producto.get_id()

    def eliminar_producto(self, id_producto):
        if id_producto in self._productos:
            nombre = self._productos[id_producto].get_nombre()

            # Eliminamos del SET
            self._nombres_unicos.discard(nombre.lower())

            del self._productos[id_producto]
            self.guardar_en_archivo()
            return True
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self._productos:
            producto = self._productos[id_producto]

            if cantidad is not None:
                producto.set_cantidad(cantidad)

            if precio is not None:
                producto.set_precio(precio)

            self.guardar_en_archivo()
            return True

        return False

    def buscar_por_nombre(self, nombre):
        resultados = []

        for producto in self._productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)

        return resultados

    def mostrar_todos(self):
        return list(self._productos.values())

    # Método que devuelve LISTA de TUPLAS
    def resumen_productos(self):
        """
        Devuelve una lista de TUPLAS (id, nombre)
        """
        return [producto.resumen() for producto in self._productos.values()]

    def guardar_en_archivo(self):
        data = {
            'next_id': self._next_id,
            'productos': [p.to_dict() for p in self._productos.values()]
        }

        with open(self._archivo, 'w') as f:
            json.dump(data, f, indent=4)

    def cargar_desde_archivo(self):
        if os.path.exists(self._archivo):
            with open(self._archivo, 'r') as f:
                data = json.load(f)
                self._next_id = data.get('next_id', 1)

                for prod_data in data.get('productos', []):
                    producto = Producto.from_dict(prod_data)
                    self._productos[producto.get_id()] = producto

                    # Reconstruimos el SET
                    self._nombres_unicos.add(producto.get_nombre().lower())