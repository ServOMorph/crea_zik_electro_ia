# Politique de Sécurité

## Signaler une vulnérabilité

Si vous découvrez une vulnérabilité de sécurité, **ne l'ouvrez pas publiquement** sur les Issues. À la place :

1. **Email** : servomorph14@gmail.com
   - Objet : `[SECURITY] Crea Zik Vulnerability`
   - Décrivez la vulnérabilité
   - Fournissez un PoC si possible

2. **Timeline**
   - Nous répondrons dans les 48h
   - Correctif attendu en 1-2 semaines selon la sévérité
   - Divulgation coordonnée : après publication du correctif

## Bonnes pratiques de sécurité

### Utilisation d'API

- Ne commitez jamais vos clés API
- Utilisez des fichiers `.env` (ajoutés à `.gitignore`)
- Définissez les variables via des secrets CI/CD
- Rotez régulièrement vos clés

### Données sensibles

- N'envoyez pas de données personnelles aux modèles cloud
- Utilisez Ollama local pour les données sensibles
- Chiffrez les données au repos si stockage local

### Dépendances

- Garder les dépendances à jour
- Utiliser `pip-audit` pour vérifier les vulnérabilités
- Auditer les dépendances transitives

```bash
pip install pip-audit
pip-audit
```

### Installation sécurisée

- Toujours utiliser des environnements virtuels
- Installer depuis PyPI officiel ou GitHub
- Vérifier les hash des releases
- Ne pas exécuter de scripts d'installation non vérifiés

## Support des versions

| Version | Support | EOL |
|---------|---------|-----|
| 1.x | ✅ Actif | 2025-12-31 |
| 0.x | ❌ Fin | 2026-06-30 |

Les versions reçoivent les correctifs critiques de sécurité pendant 12 mois.

---

Merci de nous aider à maintenir Crea Zik sécurisé ! 🔒

