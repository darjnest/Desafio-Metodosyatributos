from pizza import Pizza

# a) Mostrar valores de los atributos de clase sin crear una instancia
print(f"Precio de la pizza: ${Pizza.precio}")
print(f"Tamaño de la pizza: {Pizza.tamaño}")

# b) Verificar si 'salsa de tomate' está en la lista ['salsa de tomate', 'salsa bbq']
print(Pizza.validar_ingrediente("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c) Crear una instancia de la clase Pizza y realizar un pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d) Mostrar los ingredientes y tipo de masa, y si la pizza es válida o no
print(f"Ingredientes vegetales: {mi_pizza.ingrediente_vegetal_1}, {mi_pizza.ingrediente_vegetal_2}")
print(f"Ingrediente proteico: {mi_pizza.ingrediente_proteico}")
print(f"Tipo de masa: {mi_pizza.tipo_masa}")
#print(f"¿Es la pizza válida? {'Sí' si mi_pizza.es_valida else 'No'}")

# e) Intentar acceder a la validez de la pizza desde la clase (esto debería generar un error)
#print(Pizza.es_valida)