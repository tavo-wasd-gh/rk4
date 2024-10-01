#!/usr/bin/env python

import numpy as np

def dyn_generator(oper, state):
    """Generador de dinámica para un sistema de ecuaciones diferenciales.

    Esta función define la evolución temporal de un sistema en base a un
    operador lineal `oper` y un estado inicial `state`. Específicamente, esta es una
    ecuación de movimiento que sigue la conmutación entre el operador y el estado,
    multiplicada por un factor imaginario.

    Examples:
        >>> import numpy as np
        >>> oper = np.array([[0, 1], [1, 0]])  # Operador
        >>> state = np.array([[1, 0], [0, 0]]) # Estado inicial
        >>> dyn_generator(oper, state)
        [[0.-0.j 0.+1.j]
         [0.-1.j 0.-0.j]]

    Args:
        oper (np.array): Un operador que influye en la dinámica del sistema.
        state (np.array): El estado actual del sistema.

    Returns:
        (np.array): El cambio en el estado del sistema.
    """
    return -1j * (np.dot(oper, state) - np.dot(state, oper))

def rk4(func, oper, state, h):
    """Método de integración Runge-Kutta de cuarto orden para resolver EDOs.

    Esta función calcula el siguiente estado del sistema utilizando el método
    RK4, dados los datos correspondientes a la función que genera la dinámica,
    un operador lineal y su estado inicial.

    Examples:
        >>> import numpy as np
        >>> rk4(dyn_generator, np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]), 0.1)
        [[0.99003333+0.j         0.        +0.09933333j]
         [0.        -0.09933333j 0.00996667+0.j        ]]

    Args:
        func (callable): Una función que representa el sistema de ecuaciones diferenciales.
        oper (np.array): Un parámetro utilizado por la función `func` para influir en la dinámica del sistema.
        state (np.array): El estado actual del sistema.
        h (float): El tamaño del paso para la integración.

    Returns:
        (np.array): El estado estimado del sistema después de un paso temporal `h` utilizando el método RK4.
    """
    k1 = h * func(oper, state)
    k2 = h * func(oper, state + k1 / 2)
    k3 = h * func(oper, state + k2 / 2)
    k4 = h * func(oper, state + k3)

    return state + (k1 + 2*k2 + 2*k3 + k4) * (1 / 6)
