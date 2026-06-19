# Guide de Contribution

Merci de l'intérêt que vous portez à Crea Zik ! Les contributions de la communauté sont essentielles pour le succès de ce projet.

## Code de conduite

Veuillez lire et respecter notre [Code de conduite](./CODE_OF_CONDUCT.md).

## Comment contribuer

### Signaler un bug

1. Vérifiez que le bug n'a pas déjà été signalé sur [Issues](https://github.com/ServOMorph/crea_zik_electro_IA/issues)
2. Ouvrez une nouvelle issue avec le titre `[BUG] Description courte`
3. Décrivez :
   - Le comportement attendu
   - Le comportement observé
   - Étapes pour reproduire
   - Votre environnement (OS, Python version, dépendances)
   - Logs/stacktrace si disponible

### Proposer une amélioration

1. Vérifiez qu'une discussion similaire n'existe pas
2. Ouvrez une discussion ou issue avec le titre `[FEATURE] Description`
3. Expliquez :
   - Pourquoi cette amélioration est utile
   - Cas d'usage
   - Solutions envisagées
   - Alternatives considérées

### Soumettre un Pull Request

#### Préparation

1. **Fork** le projet
2. **Clonez** votre fork
   ```bash
   git clone https://github.com/VOTRE_USERNAME/crea_zik_electro_IA.git
   cd crea_zik_electro_IA
   ```
3. **Créez une branche** pour votre contribution
   ```bash
   git checkout -b feature/ma-feature
   ```
   ou
   ```bash
   git checkout -b fix/mon-bug
   ```

#### Développement

1. Installez les dépendances de développement
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Effectuez vos modifications

3. Écrivez ou mettez à jour les tests
   ```bash
   pytest tests/
   ```

4. Vérifiez la qualité du code
   ```bash
   flake8 src/
   black src/
   mypy src/
   ```

5. Committez vos changements
   ```bash
   git add .
   git commit -m "type(scope): description"
   ```
   
   Types de commit :
   - `feat` : nouvelle fonctionnalité
   - `fix` : correction de bug
   - `refactor` : refactoring de code
   - `test` : ajout/modification de tests
   - `docs` : documentation
   - `chore` : maintenance, mise à jour de dépendances

6. Poussez vers votre fork
   ```bash
   git push origin feature/ma-feature
   ```

7. Ouvrez un **Pull Request** sur le repository principal

#### Critères d'acceptation du PR

- [ ] Tests passants (`pytest`)
- [ ] Qualité de code OK (`flake8`, `black`, `mypy`)
- [ ] Documentation mise à jour
- [ ] Pas de dépendances non-essentielles ajoutées
- [ ] Message de commit clair et descriptif
- [ ] Réduction de la surface de risque

## Conventions de code

### Python

```python
# Nomenclature
class MusicComposer:  # PascalCase pour les classes
    def generate_composition(self):  # snake_case pour les fonctions
        pass

# Docstrings
def process_audio(signal: np.ndarray) -> np.ndarray:
    """Traiter un signal audio.
    
    Args:
        signal: Array audio brut
        
    Returns:
        Signal traité
        
    Raises:
        ValueError: Si le signal est vide
    """
    pass

# Type hints (recommandé)
from typing import List, Dict, Optional
def compose(prompt: str, style: Optional[str] = None) -> Dict[str, any]:
    pass
```

### Git

- Branches descriptives : `feature/nom-feature`, `fix/description-bug`
- Messages de commit : `type(scope): description courte`
- Pas de commits vides ou cosmétiques

## Structure pour les tests

```
tests/
├── test_composer.py
├── test_audio_processing.py
└── fixtures/
    ├── sample_audio.wav
    └── expected_outputs.json
```

## Documentation

- READMEs : Markdown clair, structuré
- Docstrings : Format Google ou NumPy
- Exemples : Code fonctionnel et testable

## Protocole vibecoding

Ce projet utilise le protocole vibecoding pour la collaboration IA. Si vous modifiez `_contexte/`, `CLAUDE.md` ou `.claude/commands/`, respectez le protocole documenté dans [`_docs/protocole_vibecoding.md`](./_docs/protocole_vibecoding.md).

## Questions / Aide

- 💬 [Discussions GitHub](https://github.com/ServOMorph/crea_zik_electro_IA/discussions)
- 📧 servomorph14@gmail.com
- 🐛 [Issues](https://github.com/ServOMorph/crea_zik_electro_IA/issues)

---

Merci de contribuer à Crea Zik ! 🎶

