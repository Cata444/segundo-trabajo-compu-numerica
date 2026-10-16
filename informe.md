# La raíz que se esconde — Comparación de métodos de búsqueda de raíces

Laboratorio evaluado 2 — Iteración funcional para ecuaciones (búsqueda de raíces y análisis de convergencia).
Universidad Católica del Maule.

## Objetivo

Implementar y comparar seis métodos de búsqueda de raíces sobre funciones de distinta naturaleza, y mostrar con datos y gráficos en qué se diferencian al converger:

- Métodos cerrados: **bisección** y **falsa posición**.
- Métodos abiertos: **punto fijo**, **secante**, **Newton-Raphson** y **Newton-Raphson modificado**.
- Funciones: polinómica, logarítmica, exponencial, trigonométrica, mixta y una con **raíz doble** que toca el eje x sin cruzarlo.
- Se registra para cada método: iteraciones, raíz encontrada y error.

> **Nota sobre el criterio de parada:** se usa `|f(x)| < tol` o `|x − x₋₁| < tol`, con `tol = 1e-6` y un tope de `100` iteraciones (`TOLERANCIA` y `MAX_ITER` en el código).

## Ambiente controlado

| # | Categoría | f(x) | Intervalo [a, b] | x₀ | x₁ (secante) | f(a)·f(b) | ¿Cambio de signo? |
|---|---|---|---|---|---|---|---|
| 1 | Polinómica | x³ − x − 2 | [1, 2] | 1.5 | 2.0 | −8.0000 | Sí |
| 2 | Raíz doble | (x − 2)² | [1, 3] (solo gráfico) | 1.2 | 1.5 | 1.0000 | **No** (tangencia en x = 2) |
| 3 | Logarítmica | ln(x) + x − 4 | [2, 3] | 2.5 | 3.0 | −0.1289 | Sí |
| 4 | Exponencial | e⁻ˣ − x | [0, 1] | 0.5 | 1.0 | −0.6321 | Sí |
| 5 | Trigonométrica | cos(x) − x | [0, 1] | 0.5 | 1.0 | −0.4597 | Sí |
| 6 | Mixta | √x − cos(x) | [0.1, 1] | 0.5 | 1.0 | −0.3120 | Sí |

- En las funciones 1, 3, 4, 5 y 6 se cumple f(a) x f(b) < 0, por lo que, por el **teorema de Bolzano**, existe al menos una raíz en [a, b].
- En la función 2 se cumple `f(2) = 0` y `f'(2) = 0`: la curva **toca** el eje x sin cruzarlo, por lo que no hay cambio de signo aunque sí hay raíz.

Gráficos de cada función con su raíz marcada:


### Funciones de punto fijo g(x)

Para punto fijo se despeja x de f(x) = 0 y se itera x = g(x). Converge si |g'(x)| < 1 cerca de la raíz.

| # | g(x) | Despeje |
|---|---|---|
| 1 | ∛(x + 2) | x³ = x + 2 |
| 2 | (x² + 4) / 4 | x² − 4x + 4 = 0 → 4x = x² + 4 |
| 3 | 4 − ln(x) | x = 4 − ln(x) |
| 4 | e⁻ˣ | x = e⁻ˣ |
| 5 | cos(x) | x = cos(x) |
| 6 | cos²(x) | √x = cos(x) → x = cos²(x) |

## Métodos implementados

| Método | Tipo | Fórmula | Orden de convergencia |
|---|---|---|---|
| Bisección | Cerrado | c = (a + b) / 2 | Lineal |
| Falsa posición | Cerrado | c = b − f(b)(b − a) / (f(b) − f(a)) | Lineal |
| Punto fijo | Abierto | xₙ₊₁ = g(xₙ) | Lineal |
| Secante | Abierto | xₙ₊₁ = xₙ − f(xₙ)(xₙ − xₙ₋₁) / (f(xₙ) − f(xₙ₋₁)) | Superlineal (≈ 1.618) |
| Newton-Raphson | Abierto | xₙ₊₁ = xₙ − f(xₙ) / f'(xₙ) | Cuadrático (raíz simple) |
| Newton-Raphson modificado | Abierto | xₙ₊₁ = xₙ − f(xₙ)f'(xₙ) / (f'(xₙ)² − f(xₙ)f''(xₙ)) | Cuadrático (también en raíz doble) |

Las derivadas f'(x) y f''(x) los calculamos a mano y están en "src/scripts/funciones.py"

## Resultados


## Preguntas de convergencia

### 1. ¿Qué método convergió en menos iteraciones en cada función? ¿Por qué?


### 2. ¿Qué orden de convergencia tiene cada método y cómo se refleja en el gráfico |error| vs iteración?



### 3. ¿Qué métodos requieren un intervalo con cambio de signo y cuáles no?


### 4. En la raíz doble: ¿qué métodos fallan o no aplican y cuál se comporta mejor? ¿Por qué?


### 5. ¿Cómo influyen el intervalo inicial y la estimación inicial en las iteraciones y en la convergencia?


### 6. ¿Qué método recomiendan según el tipo de función (velocidad vs robustez)?



## Conclusión

