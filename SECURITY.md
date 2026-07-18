# Politique de Securite

## Signaler une vulnerabilite

Si vous decouvrez une vulnerabilite, ne l'ouvrez pas publiquement sur les Issues.

1. **Email** : servomorph14@gmail.com
   - Objet : `[SECURITY] Crea Zik Vulnerability`
   - Decrivez la vulnerabilite et fournissez un PoC si possible

2. **Timeline**
   - Reponse sous 48h
   - Correctif en 1-2 semaines selon la severite
   - Divulgation coordonnee apres publication du correctif

## Bonnes pratiques

- Ne jamais commiter de cles API ou de donnees sensibles
- Utiliser des fichiers `.env` (ignores par `.gitignore`)
- Maintenir les dependances a jour (`pip-audit`)
- Toujours utiliser des environnements virtuels
