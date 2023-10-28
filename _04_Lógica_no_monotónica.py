pip install pyke

import pyke

# Crear un motor de inferencia
engine = pyke.get_default_engine()

# Definir hechos iniciales
engine.activate('facts')

# Definir una regla inicial
engine.activate('rules')

# Definir una nueva regla no mon�tona
engine.add_unsourced('facts', ('Puede_volar', 'Ping�ino'), user_data='puede no volar')

# Consulta para verificar si un ping�ino puede volar
consulta = "Puede_volar ?x"
engine.prove_1_goal('facts', consulta)

# Imprimir los resultados
for plan in engine.plans:
    print(plan.__str__())

# Retractar la nueva regla no mon�tona
engine.remove_unsourced('facts', ('Puede_volar', 'Ping�ino'), user_data='puede no volar')

# Consulta nuevamente
engine.reset()  # Reiniciar el motor
engine.activate('facts')
engine.prove_1_goal('facts', consulta)

# Imprimir los resultados
for plan in engine.plans:
    print(plan.__str__())
