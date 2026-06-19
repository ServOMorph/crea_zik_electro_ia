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
Première UI desktop produite dans UI/ : channel rack PyQt6 (bouton Kick synthétisé,
séquenceur 16 steps, transport play/BPM). Moteur audio temps réel via flux WASAPI
persistant + mixage par callback. Lanceur run.py avec auto-reload (watchdog).
Backend FastAPI/librosa pas encore amorcé. Docker toujours en suspens.

## Décisions structurantes (append only — 10 entrées max, archiver au-delà)
- 2026-06-19 : Initialisation du protocole vibecoding avec licence MIT pour open source.
- 2026-06-19 : Docker conservé dans la structure mais jugé prématuré sans code source.
- 2026-06-19 : UI desktop en PyQt6 (vs web), son synthétisé (vs samples).
- 2026-06-19 : Moteur audio = flux de sortie persistant + mixage par callback, sortie WASAPI low-latency.
