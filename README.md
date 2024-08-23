# Desafío - Métodos y Atributos en Python

Este desafío tiene como objetivo crear un prototipo de aplicación para una cadena de pizzerías que permita a los clientes autogestionar sus pedidos. Utilizando las características de la Programación Orientada a Objetos en Python, se desarrollará un sistema que permita ordenar una pizza con 3 ingredientes y escoger el tipo de masa.

## Requisitos

1. **Clase `Pizza`**  
   Crear una clase `Pizza` que permita crear objetos de tipo Pizza, considerando los atributos de clase adecuados.

   ```python
   class Pizza:
       precio = 10000  # Precio fijo de la pizza
       tamano = "familiar"  # Tamaño fijo de la pizza

       def __init__(self):
           self.ingrediente_proteico = None
           self.ingredientes_vegetales = []
           self.tipo_masa = None
           self.es_valida = False
   ```

2. **Método para Validar Ingredientes**  
   Agregar un método estático que permita validar un elemento dentro de una lista de casos posibles. Este método debe recibir dos argumentos: el elemento a validar y los valores posibles.

   ```python
   class Pizza:
       # Código anterior...

       @staticmethod
       def validar_elemento(elemento, lista_posibles):
           return elemento in lista_posibles
   ```

3. **Método para Realizar un Pedido**  
   Agregar un método que permita realizar un pedido, solicitando al usuario ingresar el ingrediente proteico, los dos ingredientes vegetales y el tipo de masa.

   ```python
   class Pizza:
       # Código anterior...

       def realizar_pedido(self):
           self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ")
           self.ingredientes_vegetales.append(input("Ingrese el primer ingrediente vegetal: "))
           self.ingredientes_vegetales.append(input("Ingrese el segundo ingrediente vegetal: "))
           self.tipo_masa = input("Ingrese el tipo de masa: ")
   ```

4. **Validación del Pedido**  
   Dentro del método `realizar_pedido`, validar los ingredientes y el tipo de masa usando el método del paso 2. Si los valores son válidos, se almacenará un atributo que indique si la pizza es válida.

   ```python
   class Pizza:
       # Código anterior...

       def realizar_pedido(self):
           # Código anterior...

           self.es_valida = (
               self.validar_elemento(self.ingrediente_proteico, ingredientes_proteicos) and
               all(self.validar_elemento(ing, ingredientes_vegetales) for ing in self.ingredientes_vegetales) and
               self.validar_elemento(self.tipo_masa, tipos_masa)
           )
   ```

5. **Archivo `evaluaciones.py`**  
   Crear un archivo que importe la clase `Pizza` y realice las siguientes acciones:

   ```python
   from pizza import Pizza
   from ingredientes import ingredientes_proteicos, ingredientes_vegetales, tipos_masa

   # a. Mostrar los atributos de clase
   print(f"Precio de la pizza: {Pizza.precio}")
   print(f"Tamaño de la pizza: {Pizza.tamano}")

   # b. Validar si 'salsa de tomate' está en la lista de salsas
   print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

   # c. Crear una instancia de Pizza y solicitar ingredientes
   mi_pizza = Pizza()
   mi_pizza.realizar_pedido()

   # d. Mostrar los ingredientes y si es una pizza válida
   print(f"Ingrediente proteico: {mi_pizza.ingrediente_proteico}")
   print(f"Ingredientes vegetales: {mi_pizza.ingredientes_vegetales}")
   print(f"Tipo de masa: {mi_pizza.tipo_masa}")
   print(f"¿Es una pizza válida? {mi_pizza.es_valida}")

   # e. Intentar mostrar si la clase Pizza es una pizza válida
   print(f"¿Es una clase Pizza válida? {Pizza.es_valida}")  # Esto debería generar un error
   ```

## Tip

Puedes crear un archivo `ingredientes.py` con listas que contengan los valores de ingredientes proteicos, vegetales, y tipos de masa.

```python
# ingredientes.py

ingredientes_proteicos = ["pollo", "vacuno", "carne vegetal"]
ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
tipos_masa = ["tradicional", "delgada"]
```
