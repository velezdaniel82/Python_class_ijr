
#Primero definiré una función que permita contar el total de elementos ingresados.
def number_of_elements(separator_int):
 lenght = len(separator_int)
 return lenght

#Luego, se definirá una función que devuela los números ingresados.
def elements(separator_int):
    elements_v = separator_int
    return elements_v

#Ahora, se definirá una función que permita ordenar los números de menor a mayor.
def organized_elements(separator_int):
    organized_elements_v = sorted(separator_int)
    return organized_elements_v

#Posteriormente, se define la suma de los datos ingresados.
def sum(separator_int):
    suma = 0
    for x in separator_int:
        suma += x
    return suma

#Se define la función que brinda el promedio de los datos ingresados.
def mean(sum, number_of_elements):
    mean_v = sum / number_of_elements
    return mean_v

#Se define la función que otorga la mediana. Debe tener condicionales, en el caso de que sea un conjunto par o impar.
def median(list):
    lenght = number_of_elements(list)
    lista_ordenada = organized_elements(list)
    if lenght % 2 != 0: 
        median_v = lista_ordenada[int((len(lista_ordenada)-1)/2)]
    else:
        median_v = (lista_ordenada[int((len(lista_ordenada)-1)/2)] + lista_ordenada[int((len(lista_ordenada)-1)/2)+1])/2
    return median_v

#Ahora se definirá la moda del conjunto de datos.
def moda(list):
    lista_ordenada = sorted(list)
    mode = lista_ordenada[0]
    mode_times = 0
    checking_value = lista_ordenada[0]
    checking_times = 0
    for i in range(0, len(lista_ordenada)):
        if checking_value == lista_ordenada[i]:
            checking_times+=1
        else:
            if checking_times > mode_times:
                mode = checking_value
                mode_times = checking_times
                checking_value = lista_ordenada[i]
                checking_times = 1

            else:
                checking_value = lista_ordenada[i]
    if checking_times > mode_times:
        mode = checking_value
        mode_times = checking_times
    return mode, mode_times

#Ahora se definirá una función para conocer el valor máximo de la lista.
def max(list):
    lista_ordenada = sorted(list)
    contador = lista_ordenada[0]
    maximo = 0
    for i in range(0, len(lista_ordenada)):
        if contador >= lista_ordenada[i]:
            maximo = contador
        else:
            maximo = lista_ordenada[i]
    return maximo

#Ahora se definirá una función para conocer el valor mínimo de la lista.
def min(list):
    lista_ordenada = sorted(list)
    contador = lista_ordenada[0]
    minimo = 0
    for i in range(0, len(lista_ordenada)):
        if contador <= lista_ordenada[i]:
            minimo = contador
        else:
            minimo = lista_ordenada[i]
    return minimo

#Ahora, se definirá el rango de la lista.
def rango(min, max):
    rango_v = (min, max)
    return rango_v

#Se procederá con la varianza
def var(lista):
    n = number_of_elements(lista)
    mean_v = mean(sum(lista), number_of_elements(lista))
    numero = 0
    for i in lista:
        numero += (i - mean_v)**2
        var_v = numero/n
    return var_v

#Se definirá ahora la desviación estándar:
def std_dev(lista):
   var_v = var(lista)
   std_dev_v = (var_v)**(1/2)
   return std_dev_v

#Se desarrollará una fución que arroje la media geométrica:
def med_geo(lista):
    n = number_of_elements(lista)
    producto = 1
    for i in lista:
        producto = (producto * i)
        med_geo_v = producto**(1/n)
    return med_geo_v

def menu():

    listaStr = input("Type a list of numbers separated by comas: ")

    #Se utiliza el comando split para que vuelva el string ingresado en list una lista de elementos.

    separator = (listaStr.split(","))

    #Se convierten a integers los valores que se encuentran dentro de separator, para poder realizar operaciones matemáticas con ellos.
    separator_int = [int(x) for x in separator]
    print(f'''El numero de elementos de la lista es {number_of_elements(separator_int)} 
            Los elemenos de la lista son {elements(separator_int)}
            Los elementos de la lista ordenados de menos a mayor son {organized_elements(separator_int)}
            La suma de todos los elementos de la lista es {sum(separator_int)}
            La media de la lista es {mean(sum(separator_int), number_of_elements(separator_int))}
            La mediana de la lista es {median(separator_int)}
            La moda de la lista y la cantidad de veces que se repite es {moda(separator_int)}
            El valor máximo de la lista es {max(separator_int)}
            El valor mínimo de la lista es {min(separator_int)}
            El rango de la lista es {rango(min(separator_int),max(separator_int))}
            La varianza de la lista es {var(separator_int)}
            La desviación estándar de la lista es {std_dev(separator_int)}
            La media geométrica de la lista es {med_geo(separator_int)}''')
    return separator_int

menu()
