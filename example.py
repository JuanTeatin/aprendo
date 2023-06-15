usuario={
 "nombre":"",
 "edad":"",
 "documento" :"",
 "tipo_de_documento": "",
 "contraseña": "",
 "correo": "",
 "fecha_nacimiento": ""

}



def  crear_Usuario():
    Nombre=input("Digite su nombre: ")
    Edad=int(input("Digite su edad: "))
    Documento=int(input("Digite su documento: "))
    tipo_de_documento=input("Digite el tipo de documento: ")
    contraseña=input("Digite su contraseña: ")
    Correo=input("Digite su correo: ")
    fecha_nacimiento=int(input("Digite su fecha de nacimiento: "))

    usuario["nombre"]=  Nombre
    usuario["edad"]= Edad
    usuario["documento"]= Documento
    usuario["tipo_de_documento"]= tipo_de_documento
    usuario["contraseña"]= contraseña
    usuario["correo"]= Correo
    usuario["fecha_nacimiento"]= fecha_nacimiento


#Lista

def cursos():
    Cursos = [
    "Html", "Python", "Java", "C#", "Javascript", "Introduccion a la programacion", "Desarrollo web", 
    "Seguridad informatica", "Desarrollo de videojuegos", "Base de datos", "Desarrollo de aplicaciones moviles", 
    "Programacion orientada a objetos", "Ciencia de datos y analisis"
    ]

    print("¡Bienvenido! Por favor, elige uno de los siguientes cursos:")

    for index, curso in enumerate(Cursos, start=1):
        print(f"{index}. {curso}")

    opcion = int(input("Ingresa el número correspondiente al curso que deseas: "))

    if opcion >= 1 and opcion <= len(Cursos):
        curso_elegido = Cursos[opcion - 1]
    print(f"Has elegido el curso de {curso_elegido}. ¡Disfrútalo!")
    



#Diccionario

def Diccionario():
    print("╔════════════════════════════════════════════╗")
    print("║              CURSOS APRENDO                ║")
    print("║                                            ║")
    print("║ 1-  Html                                   ║")
    print("║ 2-  Python                                 ║")
    print("║ 3-  JAVA                                   ║")
    print("║ 4-  C#                                     ║")
    print("║ 5-  JavaScript                             ║")
    print("║ 6-  Introducción a la programación         ║")
    print("║ 7-  Desarrollo web                         ║")
    print("║ 8-  Seguridad informatica                  ║")
    print("║ 9-  Desarrollo de videojuegos              ║")
    print("║ 10- Base de datos                          ║")
    print("║ 11- Desarrollo de aplicaciones moviles     ║")
    print("║ 12- Programación orientada a objetos       ║")
    print("║ 13- Ciencia de datos y analisis            ║")
    print("║                                            ║")
    print("╚════════════════════════════════════════════╝")

    opcion=input("¡Bienvenido! Estos son los cursos disponibles elija su opción")

    if opcion==1: 
        print("Curso de introducción al lenguaje de marcado HTML para la creación de páginas web")
    elif opcion==2:
        print("Curso de programación en Python, un lenguaje versátil y fácil de aprender")
    elif opcion==3
    print("Curso de programación en Java, un lenguaje utilizado en aplicaciones empresariales y Android")
    elif opcion==4
    print("Curso de programación en C#, un lenguaje orientado a objetos para el desarrollo de aplicaciones .NET")
    elif opcion==5
    print("Curso de programación en Javascript, utilizado para la creación de interacciones dinámicas en páginas web")
    elif opcion==6
    print("Curso introductorio a la programación, donde se cubren los conceptos básicos y fundamentos")
    elif opcion==7
    print("Curso de desarrollo web abarcando HTML, CSS y JavaScript, junto con frameworks y herramientas populares")
    elif opcion==8
    print("Curso de seguridad informática, donde se enseñan técnicas para proteger sistemas y redes contra amenazas cibernéticas")
    elif opcion==9
    print("Curso de desarrollo de videojuegos utilizando motores como Unity o Unreal Engine")
    elif opcion==10
    print("Curso de bases de datos, abarcando conceptos y tecnologías como MySQL, PostgreSQL o MongoDB")
    elif opcion==11
    print("Curso de desarrollo de aplicaciones móviles, enfocado en Android (Java o Kotlin) o iOS (Swift)")
    elif opcion==12
    print("Curso de programación orientada a objetos, utilizando lenguajes como Java o C++")
    elif opcion==13
    print("Curso de ciencia de datos y análisis, utilizando herramientas y técnicas para procesar y analizar datos")


#IniciarSesion


def inicioSesion():


    print("╔════════════════════════════════════════════╗")
    print("║            ══ INICIO SESION ══             ║")
    print("║                                            ║") 
    correo=input("║   Ingrese su correo:                       ║")
    contraseña=input("║   Ingrese su contraseña:                   ║")
    print("║                                            ║")
    print("║            ┌───────────────┐               ║")
    print("║            │    INICIAR    │               ║")
    print("║            └───────────────┘               ║")
    print("╚════════════════════════════════════════════╝")

    if(correo == usuario["correo"] and  contraseña == usuario["contraseña"]):
        print("Bienvenido a APRENDO")

    else:
        print("Correo o contraseña incorrecta, pruebe nuevamente")

#Buscador de cursos

def Buscador(Lista, Valor):

    posicion= 0
    encontrar= False

    while posicion < len(Lista) and not encontrar:
        if  Lista[posicion] == Valor:
            encontrar = True
        else:
            posicion += 1
    return encontrar, posicion

lista=("")
    

#MENU

z=2
z2=2
while z>1:
 z2=2
 print("╔════════════════════════════════════════════╗")
 print("║                 ── MENU ──                 ║")
 print("║                                            ║")
 print("║ 1- Registrar Usuario                       ║")
 print("║ 2- Lista cursos                            ║")
 print("║ 3- Diccionario cursos                      ║")
 print("║ 4- inicio sesion                           ║")
 print("║ 5- Buscador                                ║")
 print("║                                            ║")
 print("╚════════════════════════════════════════════╝")
 opcion=int(input("ingrese la opción que desea realizar "))
 print(" ")
  

 if(opcion==1):
    crear_Usuario()
 elif(opcion==2):
     cursos()
 elif(opcion==3):
     Diccionario()
 elif(opcion==4):
     inicioSesion()
 elif(opcion==5):
     Buscador()
 else:
     print("por favor elija una opción válida ")
     z2=0

 while z2>1:
      print("1-salir")
      print("2-realizar otra acción")
      opcion2=int(input("elija la opción "))
      if(opcion2==1):
          z=0
          z2=0
      elif(opcion2==2):
          z2=0
      else:
          print("Elija una opción valida ")