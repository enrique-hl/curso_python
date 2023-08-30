def suma_lista (input):
    print("En la función")
    resultado = 0
    for valor in input:
        if isinstance(valor, int):
            print("\tSumando valor:", valor)
            resultado += valor
        else:
            print("\tOmitiendo no numérico:", valor)
    return resultado

la_lista = [ 1 , "d" , 'a' , 4 ]
print("Lista:", la_lista)
print("Resultado:", suma_lista(la_lista))