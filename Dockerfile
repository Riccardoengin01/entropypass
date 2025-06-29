# --- Fase 1: Base Image ---
# Partiamo da un'immagine Python ufficiale e "slim" per ridurre le dimensioni finali.
FROM python:3.10-slim

# --- Fase 2: Configurazione Ambiente ---
# Impostiamo una directory di lavoro all'interno del container.
WORKDIR /app

# Impedisce a Python di bufferizzare l'output, rendendo i log visibili in tempo reale.
ENV PYTHONUNBUFFERED 1

# --- Fase 3: Installazione Dipendenze ---
# Copiamo prima il file delle dipendenze.
# Questo sfrutta il caching di Docker: se requirements.txt non cambia, questo strato non verrà ricostruito.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Fase 4: Copia dell'Applicazione ---
# Copiamo tutto il resto del codice sorgente nella directory di lavoro.
COPY . .

# --- Fase 5: Esecuzione ---
# Esponiamo la porta su cui Gunicorn ascolterà all'interno del container.
EXPOSE 8000

# Comando per avviare l'applicazione usando Gunicorn.
# Ascolta su tutte le interfacce (0.0.0.0) sulla porta 8000 con 4 processi "worker".
# app:app significa: nel file app.py, trova l'oggetto Flask chiamato app.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:app"]