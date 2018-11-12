# MetodoDeBiseccion

Este método consiste en obtener una mejor aproximación de la raíz a partir de un intervalo inicial (a,b) en el cual hay un cambio de signo en la función.
Hay que encontrar un intervalo donde haya un cambio de signo. Después hay que dividir este intervalo por mitad hasta el error deseado.
Pasos a seguir: 
1. Localizar un intervalo que contenga al menos una raíz.
2. Dividir el intervalo en dos partes iguales reteniendo la mitad en donde f(x) cambia de signo, para conservar al menos una raíz.
3. Repetir el procesó varias veces hasta cumplir con la tolerancia deseada.

Para obtener el error porcentual se debe de restar el valor absoluto del valor nuevo menos el anterior, sobre el valor nuevo y multiplicar eso por 100

Características:
+ Es siempre convergente; sin embargo, converge muy lento
+ Es óptimo para resolver una ecuación f(x)=0 cuando no se sabe nada de f, excepto calcular su signo.
+ Permite encontrar solo una raíz, aunque existan más en el intervalo.
+ Requiere que f sea continua en el intervalo especificado.
+ Se puede establecer el límite de error.
+ No puede determinar raíces complejas.
