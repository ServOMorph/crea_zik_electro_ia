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
Structure complète initialisée (22 fichiers). Repo GitHub créé et pushé.
Aucun code source produit. Prochaine étape : définir l'architecture src/ et le premier module.
Docker présent mais prématuré — à réévaluer quand le code existera.

## Décisions structurantes (append only — 10 entrées max, archiver au-delà)
- 2026-06-19 : Initialisation du protocole vibecoding avec licence MIT pour open source.
- 2026-06-19 : Docker conservé dans la structure mais jugé prématuré sans code source.
