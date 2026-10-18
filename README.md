# La raíz que se esconde — Búsqueda de raíces y convergencia
 
Laboratorio evaluado 2 de Computación Numérica · Universidad Católica del Maule.
 
Se implementan seis métodos numéricos para encontrar raíces de ecuaciones y se compara, con datos y gráficos, **cuánto le cuesta a cada uno** llegar a la raíz: cuántas iteraciones necesita, con qué error y en qué casos falla.
 
## Integrantes
 
| Integrante | Rama | Github |
|---|---|---|
| Catalina | `Catalina` | Cata444 |
| Carlos | `CarlosGranda` | Korexplayer |
 
El código evaluado es el que está en `main`. trabajamos cada uno en una rama particular y los cambios se integraron mediante pull requests.

## Métodos implementados
 
| Método | Tipo | Necesita | Orden de convergencia |
|---|---|---|---|
| Bisección | Cerrado | Intervalo con cambio de signo | Lineal |
| Falsa posición | Cerrado | Intervalo con cambio de signo | Lineal |
| Punto fijo | Abierto | x₀ y una g(x) con \|g'(x)\| < 1 cerca de la raíz | Lineal |
| Secante | Abierto | Dos puntos iniciales x₀ y x₁ | Superlineal (≈ 1.618) |
| Newton-Raphson | Abierto | x₀ y la derivada f'(x) | Cuadrático en raíces simples |
| Newton-Raphson modificado | Abierto | x₀, f'(x) y f''(x) | Cuadrático, también en raíces múltiples |

## Estructura

```
segundo-trabajo-compu-numerica/
├── README.md               # entorno (Docker) y qué hace cada script
├── informe.md              # respuestas a las preguntas de convergencia y conclusión
├── requirements.txt        # numpy, matplotlib
├── Docker/
    └──  Dockerfile              # imagen con Python 3.12 para ejecutar el proyecto
├── .gitignore              # archivos que no se suben a GitHub (__pycache__, venv)
└── src/
    ├── scripts/
    │   ├── funciones.py        # 6 funciones, derivadas, g(x), intervalos, x0/x1, tolerancia
    │   ├── iteraciones.py      # 6 métodos: bisección, falsa posición, punto fijo, secante, Newton-Raphson y Newton-Raphson modificado
    │   ├── main.py             # archivo de ejecucion principal                    
    │   ├── datos.py            # genera los CSV de cada función y el resumen de convergencia            
    │   └── graficos.py         # genera los gráficos de funciones, convergencia y resumen
    ├── data/
    │   ├── funcion_<nombre>.csv
    │   ├── iteraciones_<nombre>.csv
    │   ├── ...
    │   └── resumen_convergencias.csv
    └── assets/
        ├── convergencia_<nombre>.png
        ├── Curva_<nombre>.png
        ├── ...
        └── resumen_iteraciones.png
```

## Instalación y ejecución

### Con Docker (recomendado)

Requisito: tener Docker Desktop instalado y abierto.

```
docker build -t busqueda-raices -f Docker/Dockerfile .     # construye la imagen (solo la primera vez)
docker run --rm -v "${PWD}/src:/app/src" busqueda-raices   # ejecuta main.py
```

Los CSV se generan en `src/data/` y los gráficos en `src/assets/`.

### Sin Docker (local) para Python ≥ 3.12

```
pip install -r requirements.txt       # numpy, matplotlib

python src/scripts/main.py            # Verifica si los metodos tienen raices (Bolzano y Tangencia) genera los CSV y los Graficos.       
```

Todos los cálculos usan `numpy`. Las derivadas f'(x) y f''(x) se calcularon a mano y están en `src/scripts/funciones.py`. La tolerancia (`1e-6`) y el tope de iteraciones (`100`) se definen en `TOLERANCIA` y `MAX_ITER`.

## Resultados rápidos (tol = 1e-6, máx. 100 iteraciones)

| Pregunta | Resultado clave |
|---|---|
| **Método más rápido** | Raíces simples: Newton y Newton modificado (`[...]` iteraciones) > secante (`[...]`) > punto fijo / falsa posición > bisección (`[...]`) |
| **Orden de convergencia** | Bisección, falsa posición y punto fijo: lineal · Secante: superlineal (≈ 1.618) · Newton: cuadrático |
| **Cambio de signo** | Bisección y falsa posición lo exigen; punto fijo, secante, Newton y Newton modificado no |
| **Raíz doble (x − 2)²** | `f(a)·f(b) = 1 > 0` → bisección y falsa posición no aplican · Newton: `[...]` iter (lineal) · Newton modificado: `[...]` iter → **el mejor** |
| **Sensibilidad al inicio** | Intervalo `[1, 2]`: `[...]` iter vs `[0, 10]`: `[...]` iter · x₀ cercano: `[...]` iter vs x₀ lejano: `[...]` iter |
| **Recomendación** | Robustez → bisección · Velocidad con derivada → Newton · Sin derivada → secante · Raíz múltiple → Newton modificado |

Ver detalle, gráficos y tablas en `informe.md` y `src/data/`.

## Gráficos

- `src/assets/funcion_1.png` … `funcion_6.png`: cada función con su raíz marcada (en la raíz doble, la tangencia con el eje x).
- `src/assets/convergencia_1.png` … `convergencia_6.png`: |error| vs iteración en escala log, comparando los 6 métodos en cada función.
- `src/assets/resumen_iteraciones.png`: barras con las iteraciones de cada método en cada función.
