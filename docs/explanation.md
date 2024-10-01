# Explicación

El método de Runge-Kutta de cuarto orden es un esquema numérico para aproximar soluciones de ecuaciones diferenciales de la forma:

$$
\frac{dy}{dt}=f(t,y(t))
$$

donde $f(t,y)$ describe cómo cambia el sistema a lo largo del tiempo, y $y(t)$ es el estado del sistema en el tiempo $t$.

> **Nota:** Este módulo asume que estamos resolviendo específicamente el caso $f(t, \mathbf{y}) = −i[\mathbf{O}, \mathbf{y}(t)]$, en el cual tenemos que no existe dependencia explícita temporal en la función $f(t, \mathbf{y})$.

El método RK4 mejora la precisión de la solución en cada paso de tiempo utilizando cuatro pasos intermedios ($k_1$, $k_2$, $k_3$ y $k_4$) para estimar la solución en el siguiente paso temporal, las cuales son calculadas de la siguiente manera:

$$
k_1 = h \cdot f(t_n, y_n)
$$

$$
k_2 = h \cdot f\left(t_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right)
$$

$$
k_3 = h \cdot f\left(t_n + \frac{h}{2}, y_n + \frac{k_2}{2}\right)
$$

$$
k_4 = h \cdot f\left(t_n + h, y_n + k_3\right)
$$

Una vez calculadas las derivadas, la nueva estimación se obtiene como:

$$
y_{n+1} = y_n + \frac{1}{6} \left(k_1 + 2k_2 + 2k_3 + k_4\right)
$$
