# Contexte — crea_zik

## Objectif (immuable sauf décision explicite)
Créer un environnement de création musicale assistée par IA. Plateforme open source, gratuite, permettant aux compositeurs et musiciens d'explorer de nouvelles possibilités créatives avec l'intelligence artificielle.

## Stack / contraintes techniques (stable, rarement modifié)
- Python 3.10+
- FastAPI / Flask (backend REST)
- LLM (Claude API ou Ollama local)
- Audio Processing (librosa, pydub, scipy)
- TensorFlow / PyTorch (optionnel pour modèles custom)
- React/Vue (frontend optionnel)
- Docker (déploiement)

## État actuel (réécrit intégralement à chaque /close)
Channel rack 3 pistes (kick/snare/hihat) avec séquenceur 16 steps, transport, mute,
volume (QDial), réglages instrument temps réel (panneaux collapsibles), save/load JSON
vers SAV/. Moteur audio WASAPI persistant, soft clip tanh, MASTER_GAIN=0.35.
Backend FastAPI/librosa pas encore amorcé. Docker toujours en suspens.

## Décisions structurantes (append only — 10 entrées max, archiver au-delà)
- 2026-06-19 : Initialisation du protocole vibecoding avec licence MIT pour open source.
- 2026-06-19 : Docker conservé dans la structure mais jugé prématuré sans code source.
- 2026-06-19 : UI desktop en PyQt6 (vs web), son synthétisé (vs samples).
- 2026-06-19 : Moteur audio = flux de sortie persistant + mixage par callback, sortie WASAPI low-latency.
- 2026-06-19 : Rack multi-pistes kick/snare/hihat, mute, volume, réglages instrument temps réel.
- 2026-06-19 : Saturation corrigée — hard clip remplacé par tanh + MASTER_GAIN=0.35.
