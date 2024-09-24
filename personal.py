print("Examen1060")
print("Emiliano De Santiago Soto, 22308051281060")

print("")
# Zona De Clases
class Personal1060:
    # Zona de atributos
    capacitacion=""
    motivacion=""
    habilidades=""
    comunicacion=""
    adaptabilidad=""
    rol=""
    contratacion=""
# Zona de funciones dentro de la clase
    def mostrardatos1060(self):
        print(f"")
    
    def listapersonal1060(self):
        lista_Nomempleados=["Edgar", "Cesar", "Pao", "jus", "Larrondo"]
        for x in lista_Nomempleados:
            print(x)

    def tuplas1060(self):
        tupla_roles=("limpieza", "cajero", "gerente", "encargado", "seguridad")
        for y in tupla_roles:
            print(y)

    def diccionariopersonal1060(self):
        roles_personal = {
    "Pao: ": "Gerente",
    "Cesar: ": "Cajero",
    "Edgar: ": "Limpieza",
    "jus: ": "encargado",
    "Larrondo: ":"seguridad"}

        for x, y in roles_personal.items():
            print(x,y)

    def altas1060(self):
        print(f"La cantidad de solicitudes de empleo son altas")
        
    def bajas1060(self):
        print(f"La cantidad de renuncias de personal son bajas")


# Zona de creación de objetos
personal=Personal1060()
# Zona usando objetos

personal.capacitacion="tiene formacion universitaria y tiene 5 años de experiencia"
personal.motivacion="tiene una esposa y 2 hijos"
personal.habilidades="es habil hablando y cuando se dirige a la gente"
personal.comunicacion="buena"
personal.adaptabilidad="excelente"
personal.rol="cajero"
personal.contratacion="18-05-2023"

print("Datos del personal en la base de datos")
print(f"Capacitacion: {personal.capacitacion}")
print(f"Motivacion: {personal.motivacion}")
print(f"Habilidades: {personal.habilidades}")
print(f"Comunicacion: {personal.comunicacion}")
print(f"Adaptabilidad: {personal.adaptabilidad}")
print(f"Rol del empleado: {personal.rol}")
print(f"Fecha de contratacion: {personal.contratacion}")

# Zona usando funciones
personal.mostrardatos1060()
print(" ")
print("Nombres de empleados")
personal.listapersonal1060()
print(" ")
print("Tipos de roles")
personal.tuplas1060()
print(" ")
print("Roles asignados a empleados")
personal.diccionariopersonal1060()
print(" ")
personal.altas1060()
personal.bajas1060()