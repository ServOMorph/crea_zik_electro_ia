# Guide d'installation

## Prerequis

- Python 3.10+
- Windows (synthese audio via WASAPI)
- Carte son compatible WASAPI

## Installation

```bash
git clone https://github.com/ServOMorph/crea_zik_electro_IA.git
cd crea_zik_electro_IA

# Creer un environnement virtuel (recommande)
python3 -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Linux/macOS

# Installer les dependances
pip install -r requirements.txt
```

## Lancement

```bash
python run.py
```

`run.py` lance l'interface dans `UI/main.py` avec hot-reload : toute modification d'un fichier `.py` dans `UI/` relance automatiquement l'application.

## Verification

```bash
python -c "import PyQt6; import numpy; import sounddevice; print('OK')"
```

## Depannage

### "No module named PyQt6"

```bash
pip install PyQt6
```

### Problèmes audio

Verifiez que votre carte son supporte WASAPI (standard sur Windows 10+). Si l'audio ne fonctionne pas, consultez les sorties de debug dans le terminal au lancement.

## Support

- [Issues GitHub](https://github.com/ServOMorph/crea_zik_electro_IA/issues)
- [Discussions](https://github.com/ServOMorph/crea_zik_electro_IA/discussions)
