class Producto:
  

    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id_producto

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # TUpla: devuelve datos inmutables del producto
    def resumen(self):
        """
        Retorna una TUPLA
        """
        return (self._id_producto, self._nombre)

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self._cantidad = cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa.")

    def set_precio(self, precio):
        if precio >= 0:
            self._precio = precio
        else:
            raise ValueError("El precio no puede ser negativo.")

    def to_dict(self):
        return {
            'id': self._id_producto,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data['id'], data['nombre'], data['cantidad'], data['precio'])