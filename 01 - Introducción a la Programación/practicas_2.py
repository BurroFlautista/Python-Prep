import operator

clientes = {"Adriana": 5.2, "Pablo": 8.49, "Camila": 9.79, "Cristian": 8.53, "Margarita": 0.43}
clientes_sort = sorted(clientes.items(), key=operator.itemgetter(1), reverse=True)
print(clientes_sort)
print('----------------------------------------------------------------------')
clientes2 = {"Adriana": "Cali", "Pablo": "Medellin", "Camila": "Bogota", "Cristian": "Barranquilla",
             "Margarita": "Caracas"}
clientes_sort2 = sorted(clientes2.items(), key=operator.itemgetter(1), reverse=True)
print(clientes_sort2)