from persona import Persona


if __name__ == "__main__":
    persona = Persona()
    print(persona.__nombre__,persona.__apellido__, persona.__du__) #No se hace, vas a recursar
    persona = Persona() 
    print(persona.__dict__) #Tampoco se hace
    print(persona.mostrar_datos())
    print(persona)
