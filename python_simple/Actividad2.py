def mostrar_tareas(param_lista):
    print("Total de elementos:", len(param_lista))
    i = 1
    for elemento in param_lista:
        print("[", i, "]: ",param_lista[i-1])
        i += 1
    print()
def agregar_tarea(param_lista):
    var1 = input("Escribe el elemento a agregar: ")
    param_lista.append(var1)
    print("Agregado en posición: ", len(param_lista))
    print()
    return param_lista
def editar_tarea(param_lista):
        input1 = input("¿Cuál número de elemento deseas editar? ")
        input2 = int(input1)
        if input2 <= len(param_lista):
            var1 = input("Escribe el nuevo texto de la tarea: ")
            param_lista[input2 - 1] = var1
            print("Elemento editado")
            print()
            return param_lista
        else:
            print("Elemento inválido, intenta de nuevo")
            print()

def eliminar_tarea(param_lista):
        input1 = input("¿Cuál número de elemento deseas eliminar? ")
        input2 = int(input1)
        if input2 <= len(param_lista):
            param_lista.pop(input2 - 1)
            print("Elemento eliminado")
            print()
            return param_lista
        else:
            print("Elemento inválido, intenta de nuevo")
            print()

# Ciclo principal
input1 = 0
lista_principal = ["Test A", "Test B", "Test C"]
while 1:
    print("Lista de to-dos")
    print("Elige el número de la acción deseada:")
    print("\t[1] - Mostrar tareas")
    print("\t[2] - Agregar tarea")
    print("\t[3] - Editar tareaa")
    print("\t[4] - Eliminar tarea")
    print("\t[5] - Salir")
    input1 = input()
    print("Selección:", input1)
    if input1 == "1":
        # Mostrar lista
        mostrar_tareas(lista_principal)
    elif input1 == "2":
        # Agregar elemento
        lista_principal = agregar_tarea(lista_principal)
    elif input1 == "3":
        # Editar elemento
        mostrar_tareas(lista_principal)
        lista_principal = editar_tarea(lista_principal)
    elif input1 == "4":
        # Eliminar elemento
        mostrar_tareas(lista_principal)
        lista_principal = eliminar_tarea(lista_principal)
    elif input1 == "5":
        print("Salir")
        exit()
    else:
        print("Acción no reconocida, intenta de nuevo")
        print()