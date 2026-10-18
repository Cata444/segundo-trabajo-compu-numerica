FROM python:3.12-slim

# curl como herramienta del sistema (no es una libreria de pip)
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instalar dependencias de Python definidas en requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Backend sin interfaz grafica para matplotlib (guardar figuras con savefig)
ENV MPLBACKEND=Agg

# src se monta como volumen al ejecutar:
#   docker run -it --rm -v "$(pwd)/src:/app/src" computacion-numerica
VOLUME ["/app/src"]
WORKDIR /app

CMD ["python", "src/scripts/main.py"]