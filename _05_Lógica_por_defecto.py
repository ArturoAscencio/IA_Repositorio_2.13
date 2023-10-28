class AgenteLogicoPorDefecto:
    def __init__(self):
        # Base de conocimiento de hechos por defecto
        self.hechos_por_defecto = {
            "Puede_volar": True,  # Suponemos que los p�jaros pueden volar por defecto
            "Es_un_p�jaro": True  # Suponemos que si algo puede volar, es un p�jaro por defecto
        }

    def verificar_hecho(self, hecho):
        if hecho in self.hechos_por_defecto:
            return self.hechos_por_defecto[hecho]
        else:
            return False  # Si el hecho no est� en la base de conocimiento, por defecto asumimos que es falso

# Crear un agente l�gico por defecto
agente = AgenteLogicoPorDefecto()

# Consultas
animal = "Ping�ino"  # Un ping�ino, que no es un p�jaro
puede_volar = agente.verificar_hecho("Puede_volar")
es_un_pajaro = agente.verificar_hecho("Es_un_p�jaro")

print(f"�{animal} puede volar? {puede_volar}")
print(f"�{animal} es un p�jaro? {es_un_pajaro}")
