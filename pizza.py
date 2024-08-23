
from ingredientes import proteicos, vegetales, masas

class Pizza:
    # Atributos de clase
    precio = 10000
    tamaño = "familiar"

    def __init__(self):
        self.ingrediente_proteico = None
        self.ingrediente_vegetal_1 = None
        self.ingrediente_vegetal_2 = None
        self.tipo_masa = None
        self.es_valida = False

    @staticmethod
    def validar_ingrediente(ingrediente, lista_ingredientes):
        """Método estático para validar si un ingrediente está en una lista dada."""
        return ingrediente in lista_ingredientes

    def realizar_pedido(self):
        """Método para realizar un pedido de pizza."""
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ")
        self.ingrediente_vegetal_1 = input("Ingrese el primer ingrediente vegetal: ")
        self.ingrediente_vegetal_2 = input("Ingrese el segundo ingrediente vegetal: ")
        self.tipo_masa = input("Ingrese el tipo de masa: ")

        # Validación de ingredientes
        if (self.validar_ingrediente(self.ingrediente_proteico, proteicos) and
                self.validar_ingrediente(self.ingrediente_vegetal_1, vegetales) and
                self.validar_ingrediente(self.ingrediente_vegetal_2, vegetales) and
                self.validar_ingrediente(self.tipo_masa, masas)):
            self.es_valida = True
        else:
            self.es_valida = False
