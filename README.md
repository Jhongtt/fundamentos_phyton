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

# **Sección 4 – Variables**

# **Variables – cajas con forma de datos**

Es justo que Python nos permita codificar literales las cuales contengan valores numéricos y cadenas.

Ya hemos visto que se pueden hacer operaciones aritméticas con estos números: sumar, restar, etc. Esto se hará una infinidad de veces en un programa.

Pero es normal preguntar como es que se pueden **almacenar los resultados** de estas operaciones, para poder emplearlos en otras operaciones, y así sucesivamente.

¿Cómo almacenar los resultados intermedios, y después utilizarlos de nuevo para producir resultados subsecuentes?

Python ayudará con ello. Python ofrece "cajas" (o "contenedores") especiales para este propósito, estas cajas son llamadas **variables** ‒ el nombre mismo sugiere que el contenido de estos contenedores puede variar en casi cualquier forma.

¿Cuáles son los componentes o elementos de una variable en Python?

- Un nombre;
- Un valor (el contenido del contenedor)

Comencemos con lo relacionado al nombre de la variable.

Las variables no aparecen en un programa automáticamente. Como desarrollador, tu debes decidir cuantas variables deseas utilizar en tu programa.

También las debes de nombrar.

# **Nombres de Variables**

Si se desea **nombrar una variable**, se deben seguir las siguientes reglas:

- El nombre de la variable debe de estar compuesto por MAYÚSCULAS, minúsculas, dígitos, y el carácter _ (guion bajo)
- El nombre de la variable debe comenzar con una letra;
- El carácter guion bajo es considerado una letra;
- Las mayúsculas y minúsculas se tratan de forma distinta (un poco diferente que en el mundo real - *Alicia* y *ALICIA* son el mismo nombre, pero en Python son dos nombres de variable distintos, subsecuentemente, son dos variables diferentes);
- El nombre de las variables no pueden ser igual a alguna de las palabras reservadas de Python (las palabras clave - explicará más de esto pronto).

Nota que la misma restricción aplica a los nombres de funciones.

Python no impone restricciones en la longitud de los nombres de las variables, pero eso no significa que un nombre de variable largo sea mejor que uno corto.

Aquí se muestran algunos nombres de variable que son **correctos**, pero que no siempre son convenientes:

- **`MyVariable`**
- **`i`**
- **`l`**
- **`t34`**
- **`Exchange_Rate`**
- **`counter`**
- **`days_to_christmas`**
- **`TheNameIsTooLongAndHardlyReadable`**
- **`_`**

Estos nombres de variables también son **correctos**:

- **`Adiós_Señora`**
- **`sûr_la_mer`**
- **`Einbahnstraße`**
- **`переменная`**.

Python te permite usar no solo letras latinas sino también caracteres específicos de idiomas que usan otros alfabetos.

Ahora veamos algunos **nombres incorrectos**:

- **`10t`** (no comienza con una letra)
- **`!important`** (no comienza con una letra)
- **`exchange rate`** (contiene un espacio).

**Note**

El [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) recomienda la siguiente convención de nomenclatura para variables y funciones en Python:

- Los nombres de las variables deben estar en minúsculas, con palabras separadas por guiones bajos para mejorar la legibilidad (por ejemplo, var, my_variable)
- Los nombres de las funciones siguen la misma convención que los nombres de las variables (por ejemplo, fun, my_function)
- También es posible usar letras mixtas (por ejemplo, myVariable), pero solo en contextos donde ese ya es el estilo predominante, para mantener la compatibilidad retroactiva con la convención adoptada.

## Palabras Clave

Observa las palabras que juegan un papel muy importante en cada programa de Python.

**`['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']`**

Son llamadas **palabras clave** o (mejor dicho) **palabras clave reservadas**. Son reservadas porque **no se deben utilizar como nombres**: ni para variables, ni para funciones, ni para cualquier otra cosa que se desee crear.

El significado de la palabra reservada está **predefinido**, y no debe cambiar.

Afortunadamente, debido al hecho de que Python es sensible a mayúsculas y minúsculas, cualquiera de estas palabras se pueden modificar cambiando una o varias letras de mayúsculas a minúsculas o viceversa, creando una nueva palabra, la cual no esta reservada.

Por ejemplo - **no se puede nombrar** a la variable así:

**`import`**

No se puede tener una variable con ese nombre - esta prohibido. pero se puede hacer lo siguiente:

**`Import`**

Estas palabras podrían parecer un misterio ahorita, pero pronto se aprenderá acerca de su significado.

# **Cómo crear una variable**

¿Qué se puede poner dentro de una variable?

Cualquier cosa.

Se puede utilizar una variable para almacenar cualquier tipo de los valores que ya se han mencionado, y muchos mas de los cuales aun no se han explicado.

El valor de la variable en lo que se ha puesto dentro de ella. Puede variar tanto como se necesite o requiera. El valor puede ser entero, después flotante, y eventualmente ser una cadena.

Hablemos de dos cosas importantes - **como son creadas las variables**, y **como poner valores dentro de ellas** (o mejor dicho, como dar o **pasarles valores**).

**RECUERDA**

**Una variable se crea cuando se le asigna un valor**. A diferencia de otros lenguajes de programación, no es necesario declararla.

Si se le asigna cualquier valor a una variable no existente, la variable será **automáticamente creada**. No se necesita hacer algo más.

La creación (o su sintaxis) es muy simple: **solo utiliza el nombre de la variable deseada, después el signo de igual (=) y el valor que se desea colocar dentro de la variable.**

Observa el fragmento en el editor:

```python
var = 1
print(var)
```

Consiste de dos simples instrucciones:

- La primera crea una variable llamada **`var`**, y le asigna un literal con un valor entero de **`1`**.
- La segunda imprime el valor de la variable recientemente creada en la consola.

Como puedes ver, **`print()`** tiene otro lado: también puede manejar variables. ¿Sabes cuál será el resultado del fragmento? Ejecuta el código para verificar.

# **Cómo emplear una variable**

Se tiene permitido utilizar cuantas declaraciones de variables sean necesarias para lograr el objetivo del programa, por ejemplo:

```python
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)
```

Sin embargo, **no se permite utilizar una variable que no exista**, (en otras palabras, una variable a la cual no se le ha dado un valor).

Este ejemplo **ocasionará un error**:

```python
var = 1
print(Var)
```

Se ha tratado de utilizar la variable llamada **`Var`**, la cual no tiene ningún valor (nota: **`var`** y **`Var`** son entidades diferentes, y no tienen nada en común dentro de Python).

**RECUERDA**

Se puede utilizar **`print()`** para combinar texto con variables utilizando el operador **`+`** para mostrar cadenas con variables, por ejemplo:

```python
var = "3.8.5"
*print*("Python version: " + var)
```

¿Puedes predecir la salida del fragmento de código?

# **Cómo asignar un nuevo valor a una variable ya existente**

¿Cómo se le asigna un valor nuevo a una variable que ya ha sido creada? De la misma manera. Solo se necesita el signo de igual.

El signo de igual es de hecho un **operador de asignación**. Aunque esto suene un poco extraño, el operador tiene una sintaxis simple y una interpretación clara y precisa.

Asigna el valor del argumento de la derecha al de la izquierda, aún cuando el argumento de la derecha sea una expresión arbitraria compleja que involucre literales, operadores y variables definidas anteriormente.

Observa el siguiente código:

```python
var = 1
print(var)
var = var + 1
print(var)
```

El código envía dos líneas a la consola:

```python
Output

12
```

La primer línea del código **crea una nueva variable** llamada **`var`** y le asigna el valor de **`1`**.

La sentencia se lee de la siguiente manera: asigna el valor de **`1`** a una variable llamada **`var`**.

De manera más corta: asigna **`1`** a **`var`**.

Algunos prefieren leer el código así: **`var`** se convierte en **`1`**.

La tercera línea **le asigna a la misma variable un nuevo valor** tomado de la variable misma, sumándole **`1`**.Al ver algo así, un matemático probablemente protestaría - ningún valor puede ser igualado a si mismo más uno. Esto es una contradicción. Pero Python trata el signo **`=`** no como *igual a*, sino como *asigna un valor*.

Entonces, ¿Cómo se lee esto en un programa?

Toma el valor actual de la variable **`var`**, sumale **`1`** y guárdalo en la variable **`var`**.

En efecto, el valor de la variable **`var`** ha sido **incrementado** por uno, lo cual no está relacionado con comparar la variable con otro valor.

¿Puedes predecir cuál será el resultado del siguiente fragmento de código?

```python
var = 100
var = 200 + 300
*print*(var)
```

# **Resolviendo problemas matemáticos simples**

Ahora deberías poder construir un programa corto que resuelva problemas matemáticos simples como el teorema de Pitágoras:

*El cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos.*

El siguiente código evalúa la longitud de la hipotenusa (es decir, el lado más largo de un triángulo rectángulo, el opuesto al ángulo recto) usando el teorema de Pitágoras:

```python
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
*print*("c =", c)
```

Nota: necesitamos hacer uso del operador ** para evaluar la raíz cuadrada como:

√ (x)  = x(½)

y

c = √ a2 + b2

¿Puedes adivinar la salida del código?

[**LAB  Variables**](https://www.notion.so/LAB-Variables-2414671e02a180c09de7db9f8e7e656b?pvs=21)

# **Operadores Abreviados**

Es tiempo de explicar el siguiente conjunto de operadores que harán la vida del programador/desarrollador más fácil. Muy seguido, se desea utilizar la misma variable al lado derecho y al lado izquierdo del operador **`=`** operator.

Por ejemplo, si se necesita calcular una serie de valores sucesivos de la potencia de 2, se puede usar el siguiente código:

```python
x = x * 2
```

También, puedes utilizar una expresión como la siguiente si no puedes dormir y estas tratando de resolverlo con alguno de los métodos tradicionales:

```python
sheep = sheep + 1
```

Python ofrece una manera más corta de escribir operaciones como estas, lo cual se puede codificar de la siguiente manera:

```python
x *= 2
sheep += 1
```

A continuación se intenta presentar una descripción general para este tipo de operaciones. Si op es un operador de dos argumentos (esta es una condición muy importante) y el operador es utilizado en el siguiente contexto...:

**`variable = variable op expresión`**

...entonces se puede simplificar y mostrar de la siguiente manera:

**`variable op= expresión`**

Observa los siguientes ejemplos. Asegúrate de entenderlos todos.

![Captura de pantalla 2025-07-31 a las 9.55.07 a. m..png](attachment:7108b487-f2f6-4c15-99d5-88851bff5d5c:Captura_de_pantalla_2025-07-31_a_las_9.55.07_a._m..png)

[**LAB  Variables: un convertidor simple**](https://www.notion.so/LAB-Variables-un-convertidor-simple-2414671e02a1805483b6ed204bcd9c0f?pvs=21)

[**LAB  Operadores y expresiones**](https://www.notion.so/LAB-Operadores-y-expresiones-2414671e02a1800a8112e0bbf39617b1?pvs=21)

[LAB - Ejercicios de Algoritmos. ](https://www.notion.so/LAB-Ejercicios-de-Algoritmos-2414671e02a1802ca10ae53facae877e?pvs=21)

# **RESUMEN DE SECCIÓN**

1. Una **variable** es una ubicación nombrada reservada para almacenar valores en la memoria. Una variable es creada o inicializada automáticamente cuando se le asigna un valor por primera vez. (2.1.4.1)
2. Cada variable debe de tener un nombre único - un **identificador**. Un nombre válido debe ser aquel que no contiene espacios, debe comenzar con un guion bajo(**`_`**), o una letra, y no puede ser una palabra reservada de Python. El primer carácter puede estar seguido de guiones bajos, letras, y dígitos. Las variables en Python son sensibles a mayúsculas y minúsculas.
3. Python es un lenguaje **de tipo dinámico**, lo que significa que no se necesita *declarar* variables en él. Para asignar valores a las variables, se utiliza simplemente el operador de asignación, es decir el signo de igual (**`=`**), por ejemplo, **`var = 1`**.
4. También es posible utilizar **operadores de asignación compuesta** (operadores abreviados) para modificar los valores asignados a las variables, por ejemplo: **`var += 1`**, o **`var /= 5 * 2`**.
5. Se les puede asignar valores nuevos a variables ya existentes utilizando el operador de asignación o un operador abreviado, por ejemplo:

```python
var = 2
*print*(var) 

var = 3
*print*(var) 

var += 1
*print*(var)
```

Puedes combinar texto y variables usando el operador + y emplear la función print() para generar cadenas y variables, por ejemplo:

```python
var = "007"
*print*("Agent " + var)
```


# **RESUMEN DE SECCIÓN**

1. Una **variable** es una ubicación nombrada reservada para almacenar valores en la memoria. Una variable es creada o inicializada automáticamente cuando se le asigna un valor por primera vez. (2.1.4.1)
2. Cada variable debe de tener un nombre único - un **identificador**. Un nombre válido debe ser aquel que no contiene espacios, debe comenzar con un guion bajo(**`_`**), o una letra, y no puede ser una palabra reservada de Python. El primer carácter puede estar seguido de guiones bajos, letras, y dígitos. Las variables en Python son sensibles a mayúsculas y minúsculas.
3. Python es un lenguaje **de tipo dinámico**, lo que significa que no se necesita *declarar* variables en él. Para asignar valores a las variables, se utiliza simplemente el operador de asignación, es decir el signo de igual (**`=`**), por ejemplo, **`var = 1`**.
4. También es posible utilizar **operadores de asignación compuesta** (operadores abreviados) para modificar los valores asignados a las variables, por ejemplo: **`var += 1`**, o **`var /= 5 * 2`**.
5. Se les puede asignar valores nuevos a variables ya existentes utilizando el operador de asignación o un operador abreviado, por ejemplo:

```python
var = 2
*print*(var) 

var = 3
*print*(var) 

var += 1
*print*(var)
```

Puedes combinar texto y variables usando el operador + y emplear la función print() para generar cadenas y variables, por ejemplo:

```python
var = "007"
*print*("Agent " + var)
```