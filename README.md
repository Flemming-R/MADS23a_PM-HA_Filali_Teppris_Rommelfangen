# MADS23a_PM-HA_Filali_Teppris_Rommelfangen
## Installation
### Voraussetzungen
Stellen Sie sicher, dass Sie `poetry` installiert haben. Sie können `poetry` über den folgenden Befehl installieren:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Weitere Informationen finden Sie in der offiziellen [Poetry-Dokumentation](https://python-poetry.org/docs/#installation).
### Installation mit Poetry
Wenn Sie `poetry` installiert haben, können Sie das Projekt wie folgt installieren:
1. Klonen Sie das Repository:
```bash
git clone https://github.com/Flemming-R/MADS23a_PM-HA_Filali_Teppris_Rommelfangen
cd MADS23a_PM-HA_Filali_Teppris_Rommelfangen
```
2. Installieren Sie die Abhängigkeiten:
```bash
poetry install
```
3. Aktivieren Sie die virtuelle Umgebung:
```bash
poetry shell
```
### Alternative Installation mit `pip`
Falls Sie `poetry` nicht verwenden möchten, können Sie die Abhängigkeiten auch direkt mit `pip` installieren:
1. Klonen Sie das Repository:
```bash
git clone https://github.com/Flemming-R/MADS23a_PM-HA_Filali_Teppris_Rommelfangen
cd MADS23a_PM-HA_Filali_Teppris_Rommelfangen
```
2. Erstellen und aktivieren Sie eine virtuelle Umgebung:
```bash
python3 -m venv venv
source venv/bin/activate # Bei Windows: venv\Scripts\activate
```
3. Installieren Sie die Abhängigkeiten aus der `pyproject.toml`-Datei:
```bash
pip install -r <(poetry export -f requirements.txt --without-hashes)
```
**Hinweis:** Wenn Sie keinen Zugriff auf `poetry` haben, um die `requirements.txt`-Datei zu generieren, können Sie diese Datei aus der `pyproject.toml` selbst erstellen und dann `pip install -r requirements.txt` ausführen.
