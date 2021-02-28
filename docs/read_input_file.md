# Cómo leer los datos del archivo de entrada

El paquete `ghc` proporciona una función denominada `read_input_file`. Esta 
función permite cargar los datos de entrada a un diccionario para ser
procesados después. El propósito de esta función es ahorrarle al programador
tener que escribir una función diferente para leer los datos de entrada cada
vez que participa en una nueva edición de la competencia, lo que puede
consumir valioso tiempo. Para ello, `read_input_file` se diseño como una 
función de propósito general, de tal forma que pueda adaptarse a cualquier
formato de datos de entrada. 

Para ello, `read_input_file` requiere que se proporcione como entrada lo que
se denomina como un _descriptor de datos_, el cual consiste de un diccionario
que describe cómo se debe organizar el contenido del archivo de entrada
en un diccionario resultante. El resto de este documento describirá cómo se 
debe llenar este descriptor de datos. 

## El problema de las pizzas

Partiendo del clásico problema "Even more pizza" que se ha utilizado como
un problema de práctica en varias ediciones de Google Hash Code, el archivo 
de entrada de este problema contenía lo sig.:

- En el primer renglón, se tenían cuatro núm. enteros separados por espacios:
  - La cantidad de pizzas disponibles en la pizzería (denotado como _M_).
  - La cantidad de equipos conformados por dos personas.
  - La cantidad de equipos conformados por tres personas.
  - La cantidad de equipos conformados por cuatro personas.
- Los siguientes _M_ renglones contenían los sig. valores separados por 
espacios:
  - La cantidad de ingredientes (denotado como _I_).
  - Una secuencia de _I_ cadenas que contienen los nombres de dichos 
  ingredientes. 

## Secciones 

Se puede ver que, de forma implícita, el archivo de entrada está dividido en 
dos _secciones_. La primera sección contiene valores generales del problema,
mientras que la segunda sección contiene datos específicos para los diferentes
tipos de pizzas que se ofrecen. De esta forma, se puede comenzar a escribir
el descriptor de datos para este archivo de la sig. manera:

```python
pizza_data_desc = [
  # sección 1
  {
    'name': 'general',
    # ...
  },
  # sección 2
  {
    'name': 'pizzas',
    # ...
  }
]
```

En el diccionario resultante, cada sección se representa como un campo
en dicho diccionario. Es decir, después de leer los datos del archivo de 
entrada, se podría acceder a cada sección utilizando la etiqueta asignada
en el campo `'name'` de la sig. manera:

```python
pizza_data = ghc.read_input_file(in_filename, pizza_data_desc)
pizza_data['general'] # la sección de datos generales
pizza_data['pizzas']  # la sección de los datos de cada pizza
```

## Columnas

Cada sección puede consistir de uno o varios renglones en el archivo, pero por
ahora podemos concentrarnos únicamente en aquellas secciones que consisten de 
un solo renglón, como es el caso de la primera sección del archivo del problema
de las pizzas. En este caso, el renglón correspondiente a esta sección 
contiene varios valores numéricos separados por espacios. Cada uno de estos
valores se denominan _columnas_. Normalmente, una sección contiene varias
columnas. Las columnas de una sección se definen de la sig. manera:

```python
pizza_data_desc = [
  # sección 1
  {
    'name': 'general',
    'columns': [
      # la cantidad de pizzas (M)
      { 'name': 'num_pizzas', 'type': int },
      # ...
    ]
  },
  # sección 2
  {
    'name': 'pizzas',
    # leer el valor 'num_pizzas' de la sección 'general';
    # esto es, el valor M
    'row_count': 'general num_pizzas',
    # ...
  }
]
```

Con esta descripción, los valores correspondientes a esta sección se podrán
leer de la sig. manera:

```python
pizza_data['general']['num_pizzas']
pizza_data['general']['num_2teams']
pizza_data['general']['num_3teams']
pizza_data['general']['num_4teams']
```

## Secciones con múltiples renglones

Como se mencionó anteriormente, una sección puede consister de varios renglones.
Para definir el número de renglones se agrega el campo `'row_count'` en la
sección correspondiente. Normalmente, el número de renglones de una sección
se especifica numéricamente en una sección anterior en el archivo. En el 
caso del problema de las pizzas, por ejemplo, la segunda sección consiste de
_M_ renglones, donde _M_ es un valor numérico incluído en la sección anterior. 
Debido a esto, el valor del campo `'row_count'` consiste del nombre de la
sección seguido del nombre del campo que contiene el valor numérico que se
debe leer para conocer el número de renglones de esta sección. Por ejemplo:

```python
pizza_data_desc = [
  # sección 1
  {
    'name': 'general',
    'columns': [
      # la cantidad de pizzas (M)
      { 'name': 'num_pizzas', 'type': int },
      # ...
    ]
  },
  
]
```

## Secciones con una cantidad indeterminada de columnas

De igual forma, una sección puede consistir de una cantidad indeterminada
de columnas. En este caso, se puede agregar el campo `'repeat'` al descriptor
de la columna correspondiente. Si el valor de este campo es un asterisco, 
entonces se le instruye al programa que leerá todas las columnas restantes
en el renglón correspondiente a ese campo. Por ejemplo:

```python
pizza_data_desc = [
  # sección 1
  {
    'name': 'general',
    # ...
  },
  # sección 2
  {
    'name': 'pizzas',
    'row_count': 'general num_pizzas',
    'columns' : [
      # un número entero que describe la cantidad de ingredientes
      { 'name': 'num_ingredients', 'type': int },
      # el resto de los valores del renglon contiene los nombres de los 
      # ingredientes
      { 'name': 'ingredients', 'type': str, 'repeat': '*' }
    ]
  }
]
```

En ocasiones, el número de valores correspondientes a una misma columna se 
describe en esa misma columna pero en un valor anterior. En este caso, se puede
especificar el nombre de la columna que contiene dicho valor dentro en el 
campo `'repeat'` en lugar de usar un asterisco. Por ejemplo:

```python
pizza_data_desc = [
  # sección 1
  {
    'name': 'general',
    # ...
  },
  # sección 2
  {
    'name': 'pizzas',
    'row_count': 'general num_pizzas',
    'columns' : [
      # un número entero (I) que describe la cantidad de ingredientes
      { 'name': 'num_ingredients', 'type': int },
      # los siguientes I valores contienen los nombres de los ingredientes
      { 'name': 'ingredients', 'type': str, 'repeat': 'num_ingredients' }
    ]
  }
]
```

Cuando se tratan de secciones o columnas de varios valores, estos normalmente
se representan como un arreglo en el diccionario resultante. Por ejemplo,
suponiendo que se lee el archivo utilizando el descriptor del ejemplo anterior,
se podría acceder a los datos de la sig. manera:

```python
pizza_data['general']['num_pizzas'] # ún solo valor numérico
pizza = pizza_data['pizzas'][0]     # varias pizzas en un arreglo
pizza['ingredients'][0]             # varios ingredientes en una pizza
```

## Poniendo todo en conjunto

Con esto se concluye la explicación de cómo llenar el descriptor de datos para
la función `ghc.read_input_file`. Como un último ejemplo, se muestra cómo 
definir el descriptor de datos para el problema de las pizzas.

Suponiendo que el archivo de entrada contiene lo siguiente:

```
5 1 2 1
3 onion pepper olive
3 mushroom tomato basil
3 chicken mushroom pepper
3 tomato mushroom basil
2 chicken basil
```

El descriptor se definiría como:

```python
pizza_data_desc = [
  # seccion 1
  {
    'name': 'general',
    'columns': [
      { 'name': 'num_pizzas', 'type': int },
      { 'name': 'num_2teams', 'type': int },
      { 'name': 'num_3teams', 'type': int },
      { 'name': 'num_4teams', 'type': int }
    ],
  },
  # seccion 2
  {
    'name': 'pizzas',
    'row_count': 'general num_pizzas',
    'columns': [
      { 'name': 'num_ingredients', 'type': int },
      { 'name': 'ingredients', 'type': str, 'repeat': 'num_ingredients' }
    ]
  }
]
```

Así, leer el archivo de entrada se puede lograr con sólo una función:

```python
pizza_data = gch.read_input_file(in_filename, pizza_data_desc)
```

El diccionario resultante, contenido en `pizza_data`, sería equivalente a 
declarar lo sig.:

```python
pizza_data = {
  'general': {
    'num_pizzas': 5,
    'num_2teams': 1,
    'num_3teams': 2,
    'num_4teams': 1
  },
  'pizzas': [
    {
      'num_ingredients': 3,
      'ingredients': [ 'onion', 'pepper', 'olive' ]
    },
    {
      'num_ingredients': 3,
      'ingredients': [ 'mushroom', 'tomato', 'basil' ]
    },
    {
      'num_ingredients': 3,
      'ingredients': [ 'chicken', 'mushroom', 'pepper' ]
    },
    {
      'num_ingredients': 3,
      'ingredients': [ 'tomato', 'mushroom', 'basil' ]
    },
    {
      'num_ingredients': 2,
      'ingredients': [ 'chicken', 'basil' ]
    }
  ]
}
```

Una vez cargados los datos al diccionario, se pueden procesar de cualquier
manera en el resto del programa. 
