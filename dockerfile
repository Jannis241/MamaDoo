# Verwende das offizielle Python-Image als Basis
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Abhängigkeiten und den Code in das Arbeitsverzeichnis
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere das gesamte Projekt in das Arbeitsverzeichnis
COPY . .

# Optional: Wenn du spezielle Einstellungen oder Befehle für die AI-Skripte hast, kannst du sie hier ausführen

# CMD-Befehl, der deine Anwendung startet (start.py in diesem Fall)
CMD ["python", "start.py"]
