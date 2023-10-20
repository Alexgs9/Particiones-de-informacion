import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Cargar el dataset sin nombres de columnas
data = pd.read_csv("irisbin.csv", header=None)

# Método 1: Partición aleatoria
def random_partition(data, train_percent):
    train_set, test_set = train_test_split(data, train_size=train_percent / 100)
    return train_set, test_set

# Método 2: Partición por especie
def species_partition(data, train_percent):
    species = data[4].unique()  # La columna 4 se asume como la columna de especies
    train_set = pd.DataFrame()
    test_set = pd.DataFrame()
    
    for sp in species:
        sp_data = data[data[4] == sp]
        sp_train, sp_test = train_test_split(sp_data, train_size=train_percent / 100)
        train_set = pd.concat([train_set, sp_train])  # Usar concat en lugar de append
        test_set = pd.concat([test_set, sp_test])  # Usar concat en lugar de append
    
    return train_set, test_set

# Método 3: Partición estratificada por especie
def stratified_species_partition(data, train_percent):
    train_set, test_set = train_test_split(data, train_size=train_percent / 100, stratify=data[4])
    return train_set, test_set

# Método 4: Partición basada en características
def feature_partition(data, train_percent, features=[0, 1]):  # Selección de columnas por índice
    X = data[features]
    y = data[4]  # La columna 4 se asume como la columna de especies
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_percent / 100)
    train_set = pd.concat([X_train, y_train], axis=1)
    test_set = pd.concat([X_test, y_test], axis=1)
    return train_set, test_set

# Método 5: Partición temporal (usando filas pares e impares)
def temporal_partition(data, train_percent):
    train_set = data.iloc[::2]
    test_set = data.iloc[1::2]
    return train_set, test_set

# Realizar particiones y mostrar gráficos
def do_partition(num_partitions, train_percent, data_partible, method):
    name =""
    data = data_partible
    dataframes_list = []
    for i in range(num_partitions):

        if (data.shape[0] == 1):
            print("No se puede particionar más")
            return dataframes_list

        if method == '1':
            name = "Metodo random"
            train_set, test_set = random_partition(data, train_percent)
        elif method == '2':
            name = "Método por especie"
            train_set, test_set = species_partition(data, train_percent)
        elif method == '3':
            name = "Método estratificado por especie"
            train_set, test_set = stratified_species_partition(data, train_percent)
        elif method == '4':
            name = "Método basado en características"
            train_set, test_set = feature_partition(data, train_percent, features=[0, 1])
        elif method == '5':
            name = "Método temporal"
            train_set, test_set = temporal_partition(data, train_percent)
        else:
            name = "Método random (por defecto)"
            train_set, test_set = random_partition(data, train_percent)

        #print(f"Partición {i + 1} usando {name}")

        arreglo_numerico1 = list(range(len(train_set)))
        arreglo_numerico2 = list(range(len(test_set)))

        #print("arreglo_numerico1", arreglo_numerico1)
        #print("arreglo_numerico2", arreglo_numerico2)
        
        # Gráfico de ejemplo
        plt.figure(figsize=(8, 6))
        plt.scatter(arreglo_numerico1, train_set[0], label='Conjunto de entrenamiento')
        plt.scatter(arreglo_numerico2, test_set[0], label='Conjunto de prueba')
        plt.xlabel('Característica 1')
        plt.ylabel('Característica 2')
        plt.title(f'Partición {i + 1} usando {name}')
        plt.legend()
        plt.show()
        

        dataframes_list.append([train_set, test_set])
        #print("Tamaño del conjunto de entrenamiento: ", train_set.shape[0])
        #print("Tamaño del conjunto de prueba: ", test_set.shape[0])
        data = train_set
    
    return dataframes_list


# Parámetros
lista_particiones = []
percent = input("Ingrese el numero de porcentaje para particionar para el total del dataset [1-99] (Ej. 70 para 70%): ")
percent = int(percent)

print("Seguirá particionando el conjunto con el "+ str(percent) +"% de los datos, el resto serán de prueba")
print("\n")

data_partible, data_prueba = train_test_split(data, train_size=percent / 100)

lista_particiones.append([data_partible, data_prueba])

while True:

    if (data_partible.shape[0] == 1):
            print("No se puede particionar más")
            break

    num_partitions = input("Ingrese el numero de particiones del mismo tipo que quiere hacer: ")
    num_partitions = int(num_partitions)
    partition_percent = input("Ingrese el numero de porcentaje [1-99]: ")
    partition_percent = int(partition_percent)

    print("Seleccione el método de partición:")
    print("1. Partición aleatoria")
    print("2. Partición por especie")
    print("3. Partición estratificada por especie")
    print("4. Partición basada en características")
    print("5. Partición temporal (usando filas pares e impares)")
    method = input("Ingrese el número del método: ")
    print("\n")
    
    particiones = do_partition(num_partitions, partition_percent, data_partible, method)
    # Iterar a través de la lista
    for elemento in particiones:
        if isinstance(elemento, list):
            i=1
            for df in elemento:
                if isinstance(df, pd.DataFrame):
                    tamaño = df.shape
                    print(f"Tamaño del conjunto{i}:")
                    print(tamaño[0])
                    i+=1
        print("\n")

    lista_particiones.append(particiones)
    data_partible = particiones[-1][0]

    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() == 'n':
        break

print("Se ha generado una lista de particiones llamada lista_particiones")

ans = input("Imprimir lista? (s/n): ")
if ans.lower() == 's':
    print(lista_particiones)