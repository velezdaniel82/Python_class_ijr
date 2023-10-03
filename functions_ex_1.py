#En primer lugar se define la función
def indice_corporal(altura, peso):
    #Luego, se define la operación que se realizará con los parámetros establecidos en la función:
    indice = peso / (altura*altura)
    #Por último, se llama el resultado de la función
    return indice


def indice_corporal_normal(lim_inferior, lim_superior, indice_corporal):
    if indice_corporal > lim_inferior and indice_corporal < lim_superior:
        print(f'''Su índice de masa corporal está entre los rangos normales''')
    else:
        print(f'''No estás entre los rangos normales''')
    return indice_corporal_normal

#Posteriormente, se debe llamar a la(s) función(es) que se creó ateriormente para que se ejecute:
altura_usuario = float(input("Escriba su altura en metros: "))
peso_usuario = float(input("Escriba su peso en Kilogramos: "))
lim_inferior_1 = 18.5
lim_superior_1 = 24.9

#En este paso se definen los valores específicos dentro de las funciones
indice_determinado = indice_corporal(altura_usuario, peso_usuario)

#Finalmente, se imprimen las funciones con las variables que contienen los valores específicos
print(f'''Su indíce de masa corporal es {indice_corporal(altura_usuario, peso_usuario)}''')
print(indice_corporal_normal(lim_inferior_1,lim_superior_1,indice_determinado))