# Copy

streamlit run main.py


## Requirements
- pandas
- numpy
- matplotlip
### oder
- `pip install -r requirements.txt`

## Verwendung

- Clonen sie das Github-Repository auf Ihren PC.
    - Dazu Git Bash öffnen und zum gewünschten Ordner navigieren
    - Führen sie folgende Befehl aus: `git clone <Link des Repositorys>` 
    - Öffnen Sie den Ordner in VS-Code
- starten sie das Virtual Environment
- führen Sie den Befehl `python main.py` aus
- das programm erstellt nun einen Ordner *figures*. In diesem befindet sich nun die Leistungskurve als *.jpg*. Zusätzlich zeigt es diese in einer Vorschau an.

## Befehle um Virtual Environment zu erstellen
### Windows:
- `python -m venv <Name des venv Ordners>`
### Linux: 
- `python3 -m venv <Name des venv Ordners>`
    - funktioniert nur auf Systemfestplatte
    
## Befehle um Virtual Environment zu aktivieren
### Windows:
- `.\[Name des venv Ordners]\Scripts\activate`
    - wenn es sich nicht aktivieren lässt
        - Powershell als Admin ausführen
        - ausführen um zu sehen was erlaubt ist `Get-ExecutionPolicy -Lis`    
        - Erlaubt alles zu installieren `Set-ExecutionPolicy Unrestricted -Scope CurrentUser`
### Linux:
- `source <Name des venv Ordners>/bin/activate`
