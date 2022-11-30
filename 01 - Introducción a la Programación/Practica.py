# print('Hola Mundo!')

print('-----------1--------------')
# def ListaDivisibles(numero, tope):
#     '''
#     Esta función devuelve una lista ordenada de menor a mayor con los números divisibles 
#     por el parámetro número entre uno (1) y el valor del parámetro "tope"
#     Recibe dos argumentos:
#         numero: Numero entero divisor
#         tope: Máximo valor a evaluar a partir de uno (1)
#     Ej:
#         ListaDivisibles(6,30) debe retornar [6,12,18,24,30]
#         ListaDivisibles(10,5) debe retornar []
#         ListaDivisibles(7,50) debe retornar [7,14,21,28,35,42,49]
#     '''
#     #Tu código aca:
#     funcion = []
#     for i in range(numero, tope + 1, numero):
#         resultado = i
#         funcion.append(resultado)
#     # print(funcion)

#     return funcion

# resultado = ListaDivisibles(6, 30)
# print(resultado)


print('-----------2--------------')
# def Exponente(numero, exponente):
#     '''
#     Esta función devuelve el resultado de elevar el parámetro "numero" al parámetro "exponente"
#     Recibe dos argumentos:
#         numero: El número base en la operación exponencial
#         exponente: El número exponente en la operación exponencial
#     Ej:
#         Exponente(10,3) debe retornar 1000
#     '''
#     #Tu código aca:
#     return numero**exponente

# resultado2 = Exponente(10, 3)
# print(resultado2)


print('-----------3--------------')
def ListaDeListas(lista):
    '''
    Esta función recibe una lista, que puede contener elementos que a su vez sean listas y
    devuelve esos elementos por separado en una lista única. 
    En caso de que el parámetro no sea de tipo lista, debe retornar nulo.
    Recibe un argumento:
        lista: La lista que puede contener otras listas y se convierte a una 
        lista de elementos únicos o no iterables.
    Ej:
        ListaDeListas([1,2,['a','b'],[10]]) debe retornar [1,2,'a','b',10]
        ListaDeListas(108) debe retornar el valor nulo.
        ListaDeListas([[1,2,[3]],[4]]) debe retornar [1,2,3,4]
    '''
    # Tu código aca:

    if type(lista) != list:
      return None

    Result = []
    for e in lista:
      if type(e)==list:
        Result.extend(ListaDeListas(e))
      else:
        Result.append(e)
    return Result
            
result = ListaDeListas([[1,2,[3]],[4],6,['A', 'B','X']])
print(result)


# New_Vec = []
# vec = [[1,2,3], [,4,5,6], [7,8,9], 'a', 'b']

# if type(vec)== list:
#     for elem in vec: 
#         for num in elem:
#             result = New_Vec.append(num) 
# print(New_Vec)


print('-----------4--------------')
# def Factorial(numero):
#     '''
#     Esta función devuelve el factorial del número pasado como parámetro.
#     En caso de que no sea de tipo entero y/o sea menor que 0, debe retornar nulo.
#     Recibe un argumento:
#         numero: Será el número con el que se calcule el factorial
#     Ej:
#         Factorial(4) debe retornar 24
#         Factorial(-2) debe retornar nulo
#         Factorial(0) debe retornar 1
#     '''
#     #Tu código aca:
#     if numero < 0 or type(numero) != int:
#       return None
#     if numero == 0:
#         return 1
#     if (numero > 1):
#         numero = numero * Factorial(numero - 1)
#     return numero

# resultado = Factorial(4)
# print(resultado)


print('-----------5--------------')
# def ListaPrimos(desde, hasta):
#   '''
#   Esta función devuelve una lista con los números primos entre los valores "desde" y "hasta"
#   pasados como parámetro, siendo ambos inclusivos.
#   En caso de que alguno de los parámetros no sea de tipo entero y/o no sea mayor a cero, debe retornar nulo.
#   En caso de que el segundo parámetro sea mayor al primero, pero ambos mayores que cero,
#   debe retornar una lista vacía.
#   Recibe un argumento:
#       desde: Será el número a partir del cual se toma el rango
#       hasta: Será el número hasta el cual se tome el rango
#   Ej:
#       ListaPrimos(7,15) debe retornar [7,11,13]
#       ListaPrimos(100,99) debe retornar []
#       ListaPrimos(1,7) debe retonan [1,2,3,5,7]

#       https://www.youtube.com/watch?v=0Ky_-O4GYZM
#   '''
#   #Tu código aca: 
#   N_Primos = []
#   if desde < 0 or hasta < 0:
#         return N_Primos
#   if desde < hasta:  
#     for i in range(desde, hasta + 1):
#       # N_Primos.append(i)
#       contador = 2
#       es_primo = True
#       while es_primo and contador < i:
#         if i % contador == 0:
#           es_primo = False
#         else:
#           contador += 1
#       if es_primo:
#         N_Primos.append(i)
#   else:
#     return N_Primos  
#   return N_Primos

# resultado5 = ListaPrimos(10, 30)
# print(resultado5)




print('-----------6--------------')
# def ListaRepetidos(lista):
#   '''
#   Esta función recibe como parámetro una lista y devuelve una lista de tuplas donde cada 
#   tupla contiene un valor de la lista original y las veces que se repite. Los valores 
#   de la lista original no deben estar repetidos. 
#   Debe respetarse el orden original en el que aparecen los elementos.
#   En caso de que el parámetro no sea de tipo lista debe retornar nulo.
#   Recibe un argumento:
#       lista: Será la lista que se va a evaluar.
#   Ej:
#       ListaRepetidos([]) debe retornar []
#       ListaRepetidos(['hola', 'mundo', 'hola', 13, 14]), debe retornar [('hola',2),('mundo',1),(13,1),(14,1)]
#       ListaRepetidos([1,2,2,4]) debe retornar [(1,1),(2,2),(4,1)]
#   '''
#   #Tu código aca:
#   counts = {}
#   for x in lista:
#     counts[x] = counts.get(x,0) + 1
#   return [*counts.items()]

# result = ListaRepetidos([1,2,2,4,4,'a', 'a', 'a'])
# print(result)



print('-----------7--------------')
# def ClaseVehiculo(tipo, color):
#     '''
#     Esta función devuelve un objeto instanciado de la clase Vehiculo, 
#     la cual debe tener los siguientes atributos:
#         Tipo:       Un valor dentro de los valores posibles: ['auto','camioneta','moto']
#         Color:      Un valor de tipo de dato string.
#         Velocidad:  Un valor de tipo de dato float, que debe inicializarse en cero.
#     y debe tener el siguiente método:
#         Acelerar(): Este método recibe un parámetro con el valor que debe incrementar a la
#                     propiedad Velocidad y luego retornarla.
#                     Si la propiedad Velocidad cobra un valor menor a cero, debe quedar en cero.
#                     Si la propiedad Velocidad cobra un valor mayor a cien, debe quedar en cien.
#     Recibe dos argumento:
#         tipo: Dato que se asignará al atributo Tipo del objeto de la clase Vehiculo
#         color: Dato que se asignará al atributo Color del objeto de la clase Vehiculo
#     Ej:
#         a = ClaseVehículo('auto','gris')
#         a.Acelerar(10) -> debe devolver 10
#         a.Acelerar(15) -> debe devolver 25
#         a.Acelerar(-10) -> debe devolver 15
#     '''
#     #Tu código aca:
#     class vehiculo(object):
#         def __init__(self, tipo, color):
#             self.tipo = tipo
#             self.color = color
#             self.velocidad = 0

#         def Acelerar(self, vel):
#             if vel < 0:
#                 return 0
#             self.velocidad += vel
#             return self.velocidad
#     return vehiculo(tipo, color)

# a = ClaseVehiculo('auto','gris')
# b = a.Acelerar(10)
# print(b)


print('-----------8--------------')
def OrdenarDiccionario(diccionario_par, clave, descendente=True):
    '''
    Esta función recibe como parámetro un diccionario, cuyas listas de valores tienen el mismo
    tamaño y sus elementos enésimos están asociados. Y otros dos parámetros que indican
    la clave por la cual debe ordenarse y si es descendente o ascendente.
    La función debe devolver el diccionario ordenado, teniendo en cuenta de no perder la
    relación entre los elementos enésimos.
    Recibe tres argumentos:
        diccionario:    Diccionario a ordenar.
        clave:          Clave del diccionario recibido, por la cual ordenar.
        descendente:    Un valor booleano, que al ser verdadero indica ordenamiento ascendente y 
                        descendente si es falso. 
                        Debe tratarse de un parámetro por defecto en True.
    Si el parámetro diccionario no es un tipo de dato diccionario ó el parámetro clave no 
    se encuentra dentro de las claves del diccionario, debe devolver nulo.
    Ej:
        dicc = {'clave1':['c','a','b'],
                'clave2':['casa','auto','barco'],
                'clave3':[1,2,3]}
        OrdenarDiccionario(dicc, 'clave1')          debe retornar {'clave1':['a','b','c'],
                                                                'clave2':['auto','barco','casa'],
                                                                'clave3':[2,3,1]}
        OrdenarDiccionario(dicc, 'clave3', False)   debe retornar {'clave1':['b','a','c'],
                                                                'clave2':['barco','auto','casa'],
                                                                'clave3':[3,2,1]}
    '''
    #Tu código aca:
  






'''
HENRY CHALLENGE - Matemática
Cómo responder:

Cuando se pida una respuesta numérica, redondear al primer decimal. Ejemplo: 1.342 -> 1.3; 3 -> 3.0.
Cuando no exista solución, responder NULL. Ejemplo: Cuál es el mayor número natural? -> NULL

Una pizzería de moda está diseñando una caja para llevar pizza por porción. En primera instancia, crearon un modelo con un ángulo de 40 grados que contiene una porción de pizza de 250 gr, a venderse por 5 $. Sin embargo, el gerente remarcó que el margen de ganancia no era suficiente, por lo que habría que disminuir la porción a 200 gr.
1-a) ¿Cuánto disminuyó, en porcentaje, el peso de la porción?
1-b) ¿Cuál debería ser el nuevo precio para que el cliente pague lo mismo el gramo de pizza?
1-c) ¿Cuál debería ser el nuevo ángulo de la caja?
1-d) Si fabrico un triángulo rectángulo con el ángulo de la respuesta c) y su cateto opuesto mide 1. ¿Cuánto mide su cateto adyacente?
1-e) Entre 0 y 360 grados, ¿ cuántos ángulos tienen cos=0?

Una fábrica produce cajas de 10 tornillos, y la cantidad de tornillos (T) en función del tiempo (min) está dada por la fórmula T(min) = 4*min + 3
2-a) ¿Cuántas horas le lleva producir 12 cajas?
2-b) Si sobran tornillos, ¿cuántos?

Para la siguiente función, con dominio -360 grados<=a<=360 grados, marcar Verdadero ó Falso.

f(a) = cos(a) + 1

3-a) Es continua.
3-b) No tiene ningún mínimo local.
3-c) Tiene un mínimo local, donde la función toma el valor de -1.
3-d) Tiene más de un mínimo local, donde la función toma el valor de 0

Dada una recta de ordenada al origen 50 y pendiente -3
4-a) Qué valor toma cuando su variable independiente es igual a 6?
'''