# Crea Zik - Création Musicale Assistée par IA

<div align="center">

**Plateforme open source gratuite pour la création musicale avec l'intelligence artificielle**

[Documentation](#documentation) • [Installation](#installation) • [Contribution](#contribution) • [License](#licence)

</div>

## À propos

Crea Zik est un environnement complet pour explorer et créer de la musique avec l'assistance d'IA. Notre mission est de démocratiser les outils créatifs avancés en les rendant accessibles, gratuits et open source.

### Caractéristiques principales

- 🎵 **Génération musicale** — Composition assistée par IA
- 🎛️ **Processing audio** — Manipulation et traitement du son
- 🔄 **Workflows flexibles** — Adaptez le système à votre créativité
- 🖥️ **Interface simple** — Facile à utiliser, puissant sous le capot
- 📦 **Complètement open source** — Licence MIT, modifiable et déployable

## Installation

### Prérequis

- Python 3.10+
- pip / conda
- (Optionnel) GPU CUDA/ROCm pour accélération

### Installation rapide

```bash
git clone https://github.com/ServOMorph/crea_zik_electro_IA.git
cd crea_zik_electro_IA
pip install -r requirements.txt
```

### Avec Docker (recommandé)

```bash
docker build -t crea-zik .
docker run -it crea-zik
```

## Documentation

Consultez la [documentation complète](./docs/) pour :
- [Guide de démarrage](./docs/getting-started.md)
- [API Reference](./docs/api.md)
- [Exemples d'utilisation](./docs/examples/)
- [Architecture du projet](./docs/architecture.md)

## Protocole de développement

Ce projet utilise le **protocole vibecoding** pour la gestion des contextes et sessions Claude AI. Consultez [`_docs/protocole_vibecoding.md`](./_docs/protocole_vibecoding.md) pour les commandes `/start` et `/close`.

## Contribution

Les contributions sont bienvenues ! Consultez [CONTRIBUTING.md](./CONTRIBUTING.md) pour :
- Comment signaler les bugs
- Comment proposer des améliorations
- Processus de Pull Request
- Code de conduite

## Structure du projet

```
crea_zik_electro_IA/
├── README.md                    # Ce fichier
├── LICENSE                      # Licence MIT
├── CLAUDE.md                    # Instructions IA
├── CONTRIBUTING.md              # Guide de contribution
├── CODE_OF_CONDUCT.md           # Code de conduite
├── requirements.txt             # Dépendances Python
├── Dockerfile                   # Configuration Docker
├── _contexte/                   # Gestion de contexte (vibecoding)
├── _docs/                       # Documentation
├── src/                         # Code source
├── tests/                       # Tests unitaires
├── examples/                    # Exemples d'utilisation
└── .claude/commands/            # Commandes Claude Code (/start, /close)
```

## Utilisation rapide

```python
from crea_zik import MusicComposer

composer = MusicComposer()
composition = composer.generate(prompt="Musique électronique ambient")
composition.save("output.wav")
```

## Modèles supportés

- **Claude API** (défaut) — Recommandé pour la qualité
- **Ollama local** — Pour confidentialité/hors-ligne
- **OpenAI** (optionnel)

## Roadmap

- [ ] Phase 1 : Core API et génération basique
- [ ] Phase 2 : Interface web
- [ ] Phase 3 : Intégration DAW (FL Studio, Ableton)
- [ ] Phase 4 : Modèles fine-tuned

## Support

- 🐛 [Issues GitHub](https://github.com/ServOMorph/crea_zik_electro_IA/issues)
- 💬 [Discussions](https://github.com/ServOMorph/crea_zik_electro_IA/discussions)
- 📧 Contact : servomorph14@gmail.com

## Licence

Ce projet est sous licence **MIT** — Entièrement gratuit et open source.

Voir [LICENSE](./LICENSE) pour plus de détails.

## Remerciements

- [Anthropic](https://anthropic.com) — Claude API
- [Librosa](https://librosa.org) — Audio processing
- Tous nos contributeurs ❤️

---

**Rejoignez la communauté et créez la musique de demain !** 🎶

