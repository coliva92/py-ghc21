[ghc]: https://codingcompetitions.withgoogle.com/hashcode

# Py-GHC

Plantilla para crear un programa de interfaz de línea de comandos en el 
lenguaje Python para competir en diferentes ediciones de 
[Google Hash Code][ghc]. También se incluyen algunas funciones que podrían
servir de apoyo.

El objetivo de esta base de código es disminuir la cantidad de tiempo que se
requiere para codificar los algoritmos que se proponen durante la competencia,
aprovechando código pre-existente. Para ello, se recomienda que todo código 
de propósito general que se haya utilizado en ediciones anteriores de la 
competencia se agreguen a este repositorio. Así, en ediciones futuras, se
puede copiar este repositorio y partir desde ahí, en lugar de escribir 
código completamente nuevo.

Dado que el código proporcionado en este repositorio es sólo una plantilla, el
programa resultante no hace nada. Para ver instrucciones sobre cómo ejecutar
el programa por la interfaz de la línea de comandos, se puede ejecutar el
sig. comando:

```
python -m ghc --help
```

Tras copiar este repositorio, se recomienda que todo el código específico 
para resolver el problema de la competencia se escriba en el archivo 
`competition.py`, para no contaminar las otros módulos de propósito general. 
