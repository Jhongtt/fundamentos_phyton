# fundamentos_phyton
------------------------------------------------------------------------------------------------------------
 seccion 1 lo que se hizo fue aprender sobre la funcion print ya que este se usa para todo es lo que se va a mostrar en pantalla ya sean operaciones basicas o complejas tambien se puede agregar texto en esta primera seccion apredi sobre, poner un hola mundo o diferentes tipos de funciones print para que muestres un texto en la pantalla de la consola y tambien hacer espacios para que se vea mas organizado y mejor implementado agregar funciones como end y sed para jugar con el resultado 
---------------------------------------------------------------------------------------------------------------
# ## Escenario
# 1 laboratorio LAB  Trabajando con la función print()

lo que pasa lo primero que hice fue el hola mundo junto y despues un print con mi nombre
y ahora lo que hice fue quitarle las comullas el error que me da es traceback (most recent)
call last y me dice en que linea junto al file y me muestra print subrayado en rojo
ahora al poner de nuevos las comillas y elimar los parentesis me sale el siguiente error name jhonata is not defined y le agrege nuevos print


---------------------------------------------------------------------------------------------------------------
# 2 laboratorio LAB  La función print() y sus argumentos


Modifica la primera línea de código en el editor, usando las palabras claves reservadas sep y end, para que se obtenga la salida esperada. Emplea dos funciones print() en el editor.

No cambies nada en la segunda invocación del print().

# solucion
print ("¡Output!", sep=" ", end="\n")
print ("¡Programing!", "Essentials", "in..python", sep="***")

se agrego el primer print lo que hace es que colocamos el output que es lo que se va a mostrar y despues el sep donde se va poner lo que se va haber al inicio pero lo deje en blanco solo puse en el end la \n para separar la linea.

y en el otro print lo que hice fue poner el texto como dice el enunciado que lo dejara igual y simplemente puse el sep para que lo se viera al inicio las comillas y listo facil.

---------------------------------------------------------------------------------------------------------------
# 3 laboratorio LAB  Dando formato a la salida

hice lo primero que fue coger la flecha y pegarla despues cree varios print con \n y hice que la flecha se viera mas grande le agrege mas asteriscos y simplemente se viera proporcionada duple las flechas con string * 2
esto lo que hace es duplicar lo que esta al lado

al eliminar algunas comillas lo que hace es que el sisteme muestra un error que dice ps c:\users\raton.....
file ...... y print(**"string *2) se muestra una flecha en rojo debajo de lo que falta y aparece unterminated string literal detectado en la linea 94 danonos a entender que tenemos un error hay de sitanxis muy sencillo 

Al cambiar por letras mayusculas muestra un error ya que si o si por obligacion se tiene que escribir lo que 
vendria hacer en minusculas el print para que funcione correctamente y igual ta va a dar a entender que Print is not defined. Did you mean: 'print'? danos a entender como lo debemos escribir

lo unico que pasa al cambiar asterico por coma o apostrofes lo que hace es cambiarlo por eso no hay ningun error  

---------------------------------------------------------------------------------------------------------------
# Sección 2 – Literales de Python

lo que estamos viendo es literlas o datos basicos como enteros como seria pues en el ejercicio se ve print("2") y lo ve como un texto porqeu el sistema ve que tiene comillas pero si se poner print(2) lo detecta como numero entero automaticamente como se puede ver lo que pasa es que hay diferentes tipos de funciones aqui se puede ver como los numero se ingresan de diferentes maneras 

## Enteros

Quizá ya sepas un poco acerca de como las computadoras hacen cálculos con números. Tal vez has escuchado del **sistema binario**, y como es que ese es el sistema que las computadoras utilizan para almacenar números y como es que pueden realizar cualquier tipo de operaciones con ellos.

No exploraremos las complejidades de los sistemas numéricos posicionales, pero se puede afirmar que todos los números manejados por las computadoras modernas son de dos tipos:

- **enteros**, es decir, aquellos que no tienen una parte fraccionaria,
- y números **punto-flotantes** (o simplemente **flotantes**), los cuales contienen (o son capaces de contener) una parte fraccionaría.

Esta definición no es tan precisa, pero es suficiente por ahora. La distinción es muy importante, y la frontera entre estos dos tipos de números es muy estricta. Ambos tipos difieren significativamente en como son almacenados en una computadora y en el rango de valores que aceptan.

La característica del valor numérico que determina el tipo, rango y aplicación se denomina el **tipo**.

Si se codifica un literal y se coloca dentro del código de Python, la forma del literal determina la representación (tipo) que Python utilizará para **almacenarlo en la memoria**.

Por ahora, dejemos los números flotantes a un lado (regresaremos a ellos pronto) y analicemos como es que Python reconoce un número entero.

El proceso es casi como usar lápiz y papel - es simplemente una cadena de dígitos que conforman el número. pero hay una condición - no se deben insertar caracteres que no sean dígitos dentro del número.

Tomemos por ejemplo, el número *once millones ciento once mil ciento once*. Si tomaras ahorita un lápiz en tu mano, escribirías el siguiente número: **`11,111,111`**, o así: **`11.111.111`**, incluso de esta manera: **`11 111 111`**.

Es claro que la separación hace que sea más fácil de leer, especialmente cuando el número tiene demasiados dígitos. Sin embargo, Python no acepta estas cosas, está **prohibido**. ¿Qué es lo que Python permite?. El uso de **guion bajo** en los literales numéricos.*

Por lo tanto, el número se puede escribir ya sea así: **`11111111`**, o como sigue: **`11_111_111`**.

**Nota** *Python 3.6 ha introducido el guion bajo en los literales numéricos, permitiendo colocar un guion bajo entre dígitos y después de especificadores de base para mejorar la legibilidad. Esta característica no está disponible en versiones anteriores de Python.

¿Cómo se codifican los números negativos en Python? Como normalmente se hace, agregando un signo de **menos**. Se puede escribir: **`-11111111`**, o **`-11_111_111`**.

Los números positivos no requieren un signo positivo antepuesto, pero es permitido, si se desea hacer. Las siguientes líneas describen el mismo número: **`+11111111`** y **`11111111`**.

## Números octales y hexadecimales

Existen dos convenciones adicionales en Python que no son conocidas en el mundo de las matemáticas. El primero nos permite utilizar un número en su representación **octal**.

Si un número entero esta precedido por un código 0O o 0o (cero-o), el número será tratado como un valor octal. Esto significa que el número debe contener dígitos en el rango del [0..7] únicamente.

0o123 es un número **octal** con un valor (decimal) igual a 83.

La función print() realiza la conversión automáticamente. Intenta esto: lo que hace esto es que crea numeros octales que son decimales 
print(0o123) como se puede ver aca 

y despues esta el hexagonal lo que hace es tirar numeros decimales de la siguiente manera 
print(0x123) como se ve aca en pantalla

## Flotantes

Ahora es tiempo de hablar acerca de otro tipo, el cual esta designado para representar y almacenar los números que (como lo diría un matemático) tienen una **parte decimal no vacía**.

Son números que tienen (o pueden tener) una parte fraccionaria después del punto decimal, y aunque esta definición es muy pobre, es suficiente para lo que se desea discutir.

Cuando se usan términos como *dos y medio* o *menos cero punto cuatro*, pensamos en números que la computadora considera como números **punto-flotante**:

Enteros vs Flotantes
4
4.0

Se puede pensar que son idénticos, pero Python los ve de una manera completamente distinta.

4 es un número **entero** mientras que 4.0 es un número **punto-flotante**.

El punto decimal es lo que determina si es flotante.

Por otro lado, no solo el punto hace que un número sea flotante. Se puede utilizar la letra **`e`**.

Cuando se desea utilizar números que son muy pequeños o muy grandes, se puede implementar la **notación científica**.

Por ejemplo, la velocidad de la luz, expresada en *metros por segundo*. Escrita directamente se vería de la siguiente manera: **`300000000`**.

Para evitar escribir tantos ceros, los libros de texto emplean la forma abreviada, la cual probablemente hayas visto: **`3 x 108`**.

Se lee: tres por diez elevado a la octava potencia.

En Python, el mismo efecto puede ser logrado de una manera similar - observa lo siguiente:

Codificando Flotantes

Veamos ahora como almacenar números que son muy pequeños (en el sentido de que están muy cerca del cero).

Una constante de física denominada *La Constante de Planck* (denotada como *h*), de acuerdo con los libros de texto, tiene un valor de: **6.62607 x 10-34**.

Nota: el hecho de que se haya escogido una de las posibles formas de codificación de un valor flotante no significa que Python lo presentará de la misma manera.

Python podría en ocasiones elegir una **notación diferente**.

Python siempre elige la presentación más corta del número, y esto se debe de tomar en consideración al crear literales.

## **Cadenas**

Las cadenas se emplean cuando se requiere procesar texto (como nombres de cualquier tipo, direcciones, novelas, etc.), no números.

Ya conoces un poco acerca de ellos, por ejemplo, que **las cadenas requieren comillas** así como los flotantes necesitan punto decimal.

Este es un ejemplo de una cadena: **`"Yo soy una cadena."`**

Sin embargo, hay una cuestión. Cómo se puede codificar una comilla dentro de una cadena que ya está delimitada por comillas.

Supongamos que se desea mostrar un muy sencillo mensaje:

Me gusta "Monty Python"

¿Cómo se puede hacer esto sin generar un error? Existen dos posibles soluciones.

La primera se basa en el concepto ya conocido del **carácter de escape**, el cual recordarás se utiliza empleando la **diagonal invertida**. La diagonal invertida puede también escapar de la comilla. Una comilla precedida por una diagonal invertida cambia su significado - no es un limitador, simplemente es una comilla.

## Codificando Cadenas

Ahora, la siguiente pregunta es: ¿Cómo se puede insertar un apóstrofe en una cadena la cual está limitada por dos apóstrofes?

A estas alturas ya se debería tener una posible respuesta o dos.

Valores Booleanos

ro es más grande que otro, el resultado es la creación de un tipo de dato muy específico - un valor **booleano**.

El nombre proviene de George Boole (1815-1864), el autor de *Las Leyes del Pensamiento*, las cuales definen el **Álgebra Booleana** - una parte del álgebra que hace uso de dos valores: **`True`** y **`False`**, denotados como **`1`** y **`0`**.

Un programador escribe un programa, y el programa hace preguntas. Python ejecuta el programa, y provee las respuestas. El programa debe ser capaz de reaccionar acorde a las respuestas recibidas.

Afortunadamente, las computadoras solo conocen dos tipos de respuestas:

- Si, esto es verdad.
- No, esto es falso.

Nunca habrá una respuesta como: *No lo sé* o *probablemente si, pero no estoy seguro*.

Python, es entonces, un reptil **binario**.
# **RESUMEN DE SECCIÓN**

1. Los **literales** son notaciones para representar valores fijos en el código. Python tiene varios tipos de literales - es decir, un literal puede ser un número por ejemplo, **`123`**), o una cadena (por ejemplo, "Yo soy un literal.").

2. El **sistema binario** es un sistema numérico que emplea *2* como su base. Por lo tanto, un número binario está compuesto por 0s y 1s únicamente, por ejemplo, **`1010`** es *10* en decimal.

Los sistemas de numeración Octales y Hexadecimales son similares pues emplean *8* y *16*

como sus bases respectivamente. El sistema hexadecimal utiliza los números decimales más seis letras adicionales.

3. Los **enteros** (o simplemente **int**) son uno de los tipos numéricos que soporta Python. Son números que no tienen una parte fraccionaria, por ejemplo, **`256`**, o **`-1`** (enteros negativos).

4. Los números **punto-flotante** (o simplemente **flotantes**) son otro tipo numérico que soporta Python. Son números que contienen (o son capaces de contener) una parte fraccionaria, por ejemplo, **`1.27`**.

5. Para codificar un apóstrofe o una comilla dentro de una cadena se puede utilizar el carácter de escape, por ejemplo, **`'I\'m happy.'`**, o abrir y cerrar la cadena utilizando un conjunto de símbolos distintos al símbolo que se desea codificar, por ejemplo, **`"I'm happy."`** para codificar un apóstrofe, y **`'El dijo "Python", no "typhoon"'`** para codificar comillas.

6. Los **valores booleanos** son dos objetos constantes **`True`** y **`False`** empleados para representar valores de verdad (en contextos numéricos **`1`** es **`True`**, mientras que **`0`** es **`False`**.

**Extra**

Existe un literal especial más utilizado en Python: el literal **`None`**. Este literal es llamado un objeto de **`NoneType`**, y puede ser utilizado para representar **la ausencia de un valor**. Pronto se hablará más acerca de ello.

---------------------------------------------------------------------------------------------------------------

# **Python como una calculadora**

Ahora, se va a mostrar un nuevo lado de la función print(). Ya se sabe que la función es capaz de mostrar los valores de los literales que le son pasados por los argumentos.

De hecho, puede hacer algo más.

Tomando esto más seriamente, nos estamos adentrado en el terreno de los operadores y expresiones.
# **Operadores Básicos**

Un **operador** es un símbolo del lenguaje de programación, el cual es capaz de realizar operaciones con los valores.

Por ejemplo, como en la aritmética, el signo de + (más) es un operador el cual es capaz de **sumar** dos números, dando el resultado de la suma.

Sin embargo, no todos los operadores de Python son tan simples como el signo de más, veamos algunos de los operadores disponibles en Python, las reglas que se deben seguir para emplearlos, y como interpretar las reglas que realizan.

+-*///%**

El orden en el que aparecen no es por casualidad. Hablaremos más de ello cuando se hayan visto todos.

Exponenciación

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

Nota: En los ejemplos, los dobles asteriscos están rodeados de espacios, no es obligatorio hacerlo pero hace que el código sea mas **legible**.

Los ejemplos muestran una característica importante de los **operadores numéricos** de Python.

Ejecuta el código y observa cuidadosamente los resultados que arroja. ¿Puedes observar algo?

**Recuerda**: Es posible formular las siguientes reglas con base en los resultados:

- Cuando **ambos** **`*`** argumentos son enteros, el resultado es entero, también;
- Cuando **al menos un `*`** argumento es flotante, el resultado también es flotante.

Esta es una distinción importante que se debe recordar.

## Multiplicación

Un símbolo de **`*`** (asterisco) es un operador de **multiplicación**.

Ejecuta el código y revisa si la regla de *entero vs flotante* aún funciona.

## División

Un símbolo de **`/`** (diagonal) es un operador de **división**.

El valor después de la diagonal es el **dividendo**, el valor antes de la diagonal es el **divisor**.
Deberías de poder observar que hay una excepción a la regla.

**El resultado producido por el operador de división siempre es flotante**, sin importar si a primera vista el resultado es flotante: **`1 / 2`**, o si parece ser completamente entero: **`2 / 1`**.

¿Esto ocasiona un problema? Sí, en ocasiones se podrá necesitar que el resultado de una división sea entero, no flotante.

Afortunadamente, Python puede ayudar con eso.

## División entera

Un símbolo de **`//`** (doble diagonal) es un operador de **división entera**. Difiere del operador estándar **`/`** en dos detalles:

- El resultado carece de la parte fraccionaria, está ausente (para los enteros), o siempre es igual a cero (para los flotantes); esto significa que **los resultados siempre son redondeados**;
- Se ajusta a la regla *entero vs flotante*.

Como se puede observar, *una división de entero entre entero* da un **resultado entero**. Todos los demás casos producen flotantes.

Hagamos algunas pruebas mas avanzadas.

magina que se utilizó **`/`** en lugar de **`//`** - ¿Podrías predecir los resultados?

Si, sería **`1.5`** en ambos casos. Eso está claro.

Pero, ¿Qué resultado se debería esperar con una división **`//`**?

Ejecuta el código y observa por ti mismo.

Lo que se obtiene son dos unos, uno entero y uno flotante.

El resultado de la división entera siempre se redondea al valor entero inferior mas cercano del resultado de la división no redondeada.

Esto es muy importante: **el redondeo siempre va hacia abajo**.

## Residuo (módulo)

El siguiente operador es uno muy peculiar, porque no tiene un equivalente dentro de los operadores aritméticos tradicionales.

Su representación gráfica en Python es el símbolo de **`%`** (porcentaje), lo cual puede ser un poco confuso.

Piensa en el como una diagonal (operador de división) acompañado por dos pequeños círculos.

El resultado de la operación es el **residuo que queda de la división entera**.

En otras palabras, es el valor que sobra después de dividir un valor entre otro para producir un resultado entero.

Nota: el operador en ocasiones también es denominado **módulo** en otros lenguajes de programación.

Observa el fragmento de código – intenta predecir el resultado y después ejecútalo:

Como puedes observar, el resultado es dos. Esta es la razón:

- **`14 // 4`** da como resultado un **`3`** → esta es la parte entera, es decir el **cociente**;
- **`3 * 4`** da como resultado **`12`** → como resultado de **la multiplicación entre el cociente y el divisor**;
- **`14 - 12`** da como resultado **`2`** → este es el **residuo**.

El siguiente ejemplo es un poco más complicado:

## Como no dividir

Como probablemente sabes, la **división entre cero no funciona**.

**No** intentes:

- Dividir entre cero;
- Realizar una división entera entre cero;
- Encontrar el residuo de una división entre cero.

## Suma

El símbolo del operador de **suma** es el **`+`** (signo de más), el cual esta completamente alineado a los estándares matemáticos.

## El operador de resta, operadores unarios y binarios

El símbolo del operador de **resta** es obviamente **`-`** (el signo de menos), sin embargo debes notar que este operador tiene otra función - **puede cambiar el signo de un número**.

Esta es una gran oportunidad para mencionar una distinción muy importante entre operadores **unarios** y **binarios**.

En aplicaciones de resta, el **operador de resta espera dos argumentos**: el izquierdo (un **minuendo** en términos aritméticos) y el derecho (un **sustraendo**).

Por esta razón, el operador de resta es considerado uno de los operadores binarios, así como los demás operadores de suma, multiplicación y división.

# **Operadores y sus prioridades**

Hasta ahora, se ha tratado cada operador como si no tuviera relación con los otros. Obviamente, dicha situación tan simple e ideal es muy rara en la programación real.

También, muy seguido encontrarás más de un operador en una expresión, y entonces esta presunción ya no es tan obvia.

Considera la siguiente expresión:

`2 + 3 * 5`

Probablemente recordarás de la escuela que las **multiplicaciones preceden a las sumas**.

Seguramente recordarás que primero se debe multiplicar 3 por 5, mantener el 15 en tu memoria y después sumar el 2, dando como resultado el 17.

El fenómeno que causa que algunos operadores actúen antes que otros es conocido como **la jerarquía de prioridades**.

Python define la jerarquía de todos los operadores, y asume que los operadores de mayor jerarquía deben realizar sus operaciones antes que los de menor jerarquía.

Entonces, si se sabe que la * tiene una mayor prioridad que la +, el resultado final debe de 


## Operadores y sus enlaces

El **enlace** de un operador determina el orden en que se computan las operaciones de los operadores con la misma prioridad, los cuales se encuentran dentro de una misma expresión.

La mayoría de los operadores de Python tienen un enlazado hacia la izquierda, lo que significa que el cálculo de la expresión es realizado de izquierda a derecha.

Este simple ejemplo te mostrará como funciona. Observa:

`*print*(9 % 6 % 2)`

Existen dos posibles maneras de evaluar la expresión:

- De izquierda a derecha: primero 9 % 6 da como resultado 3, y entonces 3 % 2 da como resultado 1;
- De derecha a izquierda: primero 6 % 2 da como resultado 0, y entonces 9 % 0 causa **un error fatal**.

# Operadores y paréntesis

Por supuesto, se permite hacer uso de **paréntesis**, lo cual cambiará el orden natural del cálculo de la operación.

De acuerdo con las reglas aritméticas, **las sub-expresiones dentro de los paréntesis siempre se calculan primero**.

Se pueden emplear tantos paréntesis como se necesiten, y seguido son utilizados para **mejorar la legibilidad** de una expresión, aun si no cambian el orden de las operaciones.