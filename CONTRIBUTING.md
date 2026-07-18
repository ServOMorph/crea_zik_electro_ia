# Guide de Contribution

Merci de l'interet porte a Crea Zik.

## Code de conduite

Veuillez lire et respecter notre [Code de conduite](./CODE_OF_CONDUCT.md).

## Signaler un bug

1. Verifier que le bug n'a pas deja ete signale sur [Issues](https://github.com/ServOMorph/crea_zik_electro_IA/issues)
2. Ouvrir une issue avec le titre `[BUG] Description courte`
3. Decrire : comportement attendu, comportement observe, etapes pour reproduire, environnement (OS, Python version)

## Proposer une amelioration

1. Verifier qu'une discussion similaire n'existe pas
2. Ouvrir une discussion ou issue avec le titre `[FEATURE] Description`
3. Expliquer : pourquoi c'est utile, cas d'usage, solutions envisagees

## Soumettre un Pull Request

1. Fork le projet
2. Creer une branche : `feature/ma-feature` ou `fix/mon-bug`
3. Installer les dependances : `pip install -r requirements.txt`
4. Committer avec un message clair : `type(scope): description`
   - `feat` : nouvelle fonctionnalite
   - `fix` : correction
   - `refactor` : refactoring
   - `docs` : documentation
   - `chore` : maintenance
5. Pousser et ouvrir un PR

## Conventions de code

- Python 3.10+, snake_case pour les fonctions/variables, PascalCase pour les classes
- Type hints recommandes
- Docstrings format Google ou NumPy
- Pas d'emojis dans le code

## Protocole vibecoding

Si vous modifiez `_contexte/`, `CLAUDE.md` ou `.claude/commands/`, respectez le protocole documente dans [`_docs/protocole_vibecoding.md`](./_docs/protocole_vibecoding.md).
