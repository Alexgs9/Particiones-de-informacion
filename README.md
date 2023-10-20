# Particiones-de-informacion
Alexandro Gutierrez Serna

Practica de particiones de informacion para seminario de sistemas basados en conocimientos.

Funcionamiento:

  1 - El programa inicia particionando en dos conjuntos, uno de prueba y uno que podrá seguir siendo particionando.
  
  2 - Se ingresa la cantidad de particiones de un mismo tipo y después el porcentaje que será particionado con este tipo de metodo.
  
  3 - El programa permite seguir eligiendo la cantidad de particiones y porcentajes hasta que el usuario lo necesite o sea posible seguir particionando.
  
  4 - Cada particion es graficada.
  


Resultado:

  El programa genera una lista de dataframes con todas las particiones que se realizaron.
  
  Ej. =
  
  #conjuntos iniciales     #Para 3 particiones de un mismo tipo         #Para 1 particion de un mismo tipo
  
  [ 
  [particionable, prueba], [[particionable],[particion1],[particion2]], [[particionable, particion3]], ...,
  ]
  




  5 Metodos de partición:
  
  (Identifiqué que el dataset es para la clasificacion de flores iris).
  
  
Partición aleatoria:

Este método divide el conjunto de datos en dos conjuntos de manera aleatoria. Es útil cuando se desea una partición simple y aleatoria de los datos.
    
  
Partición por especie: 

En este enfoque, los datos se dividen en conjuntos manteniendo proporciones de cada especie de flor presente en el conjunto de datos original. Es útil para problemas de clasificación cuando deseas mantener una distribución equitativa de clases en las particiones.
    

Partición estratificada por especie:

Es parecido al metodo anterior, pero utiliza una función de estratificación para garantizar que las particiones mantengan la proporción de especies en el conjunto de datos original. Esto es útil para problemas de clasificación donde la distribución de clases es desigual.
    

Partición basada en características: 

Los datos se dividen utilizando características específicas o columnas del conjunto de datos. Se puede seleccionar las columnas que se desean usar. Es útil cuando se desea trabajar con un subconjunto específico de características.
    

Partición temporal:

Este enfoque divide los datos en conjuntos de manera secuencial, utilizando filas pares e impares, lo que es útil en datos temporales o secuenciales. Cada conjunto representa un intervalo de tiempo diferente en la secuencia de datos.
    
