pip install modal-logic

from modal_logic import Formula, K, M

# Definir f�rmulas
p = Formula('p')
q = Formula('q')
r = Formula('r')

# Crear una f�rmula modal: "Es necesario que p o q"
necesario = K(p | q)

# Imprimir la f�rmula modal
print(necesario)

# Comprobar si una f�rmula es v�lida en un mundo posible
mundo_posible = M()
mundo_posible.add_fact(p)

# Verificar si la f�rmula "Es necesario que p o q" es v�lida en el mundo posible
es_valida = mundo_posible.is_valid(necesario)
print(f"�La f�rmula es v�lida en el mundo posible? {es_valida}")
