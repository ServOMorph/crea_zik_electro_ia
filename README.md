# Crea Zik - Step Sequencer Electro IA

**Sequencer drum open source avec synthese audio temps reel et interface PyQt6**

Crea Zik est un drum machine logiciel avec sequenceur 16 pas, synthese sonore en temps reel (numpy + sounddevice via WASAPI), et interface graphique desktop (PyQt6). Le projet est en developpement actif, concu pour evoluer vers la composition musicale assistee par IA.

## A quoi ca sert

Lancer un sequencer drum capable de jouer des kicks, snares et hi-hats avec des reglages de synthese per instrument (frequence, duree, decay, volume, mute) — le tout en temps reel, sans latence perceptible.

## Prerequis

- Python 3.10+
- Windows (synthese audio via WASAPI)
- Carte son compatible WASAPI

## Installation

```bash
git clone https://github.com/ServOMorph/crea_zik_electro_IA.git
cd crea_zik_electro_IA
pip install -r requirements.txt
```

## Usage

```bash
python run.py
```

`run.py` lance `UI/main.py` avec hot-reload (watchdog) : toute modification d'un fichier `.py` dans `UI/` relance automatiquement l'application.

### Interface

- **3 pistes** : kick, snare, hi-hat
- **Sequenceur 16 pas** : cliquer sur les steps pour activer/desactiver
- **Transport** : play / stop avec curseur de lecture visuel
- **BPM** : reglage entre 60 et 300 (defaut 120)
- **Par piste** : bouton mute, dial volume, panneau de reglages de synthese (frequence de depart/fin pour le kick, duree, amplitude de decay)
- **Sauvegarde/chargement** : export/import de patterns au format JSON

## Comment ca marche

- `run.py` — Lanceur avec hot-reload via watchdog. Lance `UI/main.py` et surveille les changements.
- `UI/main.py` — Interface PyQt6. Construit la grille de sequenceur, gere le transport avec QTimer, les parametres par piste, et le save/load JSON.
- `UI/audio.py` — Moteur de synthese audio. Genere des echantillons (sine sweep pour le kick, bruit blanc filtre pour snare/hi-hat), les joue via sounddevice en callback WASAPI, avec soft clipping et voix multiples.

## Stack technique

Python, PyQt6, numpy, sounddevice, watchdog

## Architecture

```
crea_zik_electro_IA/
├── run.py                 # Lanceur avec hot-reload
├── UI/
│   ├── main.py            # Interface PyQt6 (sequencer, transport, parametres)
│   └── audio.py           # Synthese audio temps reel (numpy + sounddevice)
├── _contexte/             # Contexte de session (protocole vibecoding)
├── _docs/                 # Documentation interne
├── requirements.txt       # Dependance Python
├── pyproject.toml         # Metadata du package
├── .claude/               # Instructions et commandes Claude Code
└── .gitignore
```

## Etat actuel

v0.1.0 — Sequencer drum fonctionnel avec 3 pistes, 16 pas, synthese temps reel et reglages par instrument.

## Licence

Ce projet est sous licence **MIT** — Voir [LICENSE](./LICENSE) pour plus de details.

## Support

- [Issues GitHub](https://github.com/ServOMorph/crea_zik_electro_IA/issues)
- [Discussions](https://github.com/ServOMorph/crea_zik_electro_IA/discussions)
