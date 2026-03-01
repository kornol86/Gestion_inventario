from servicios.inventario import Inventario

def mostrar_menu():
    print("\n--------|Sistema Avanzado de Gestión de Inventario|--------")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto")
    print("4. Buscar productos por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                id_nuevo = inventario.añadir_producto(nombre, cantidad, precio)
                print(f"Producto añadido con ID: {id_nuevo}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '2':
            try:
                id_producto = int(input("ID del producto a eliminar: "))
                if inventario.eliminar_producto(id_producto):
                    print("Producto eliminado.")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("ID inválido.")

        elif opcion == '3':
            try:
                id_producto = int(input("ID del producto a actualizar: "))
                cantidad_str = input("Nueva cantidad (deje en blanco para no cambiar): ")
                precio_str = input("Nuevo precio (deje en blanco para no cambiar): ")
                cantidad = int(cantidad_str) if cantidad_str else None
                precio = float(precio_str) if precio_str else None
                if inventario.actualizar_producto(id_producto, cantidad, precio):
                    print("Producto actualizado.")
                else:
                    print("Producto no encontrado.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '4':
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for prod in resultados:
                    print(f"ID: {prod.get_id()}, Nombre: {prod.get_nombre()}, Cantidad: {prod.get_cantidad()}, Precio: {prod.get_precio()}")
            else:
                print("No se encontraron productos.")

        elif opcion == '5':
            productos = inventario.mostrar_todos()
            if productos:
                for prod in productos:
                    print(f"ID: {prod.get_id()}, Nombre: {prod.get_nombre()}, Cantidad: {prod.get_cantidad()}, Precio: {prod.get_precio()}")
            else:
                print("Inventario vacío.")

        elif opcion == '6':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()