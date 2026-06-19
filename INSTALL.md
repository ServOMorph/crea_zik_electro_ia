# Guide d'installation

## Installation rapide (5 min)

### Option 1 : Avec pip (recommandé pour développement)

```bash
# Cloner le projet
git clone https://github.com/ServOMorph/crea_zik_electro_IA.git
cd crea_zik_electro_IA

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
```

### Option 2 : Avec Docker (recommandé pour production)

```bash
# Builder l'image
docker build -t crea-zik .

# Lancer un conteneur
docker run -it --rm crea-zik
```

### Option 3 : Développement avec installation éditable

```bash
git clone https://github.com/ServOMorph/crea_zik_electro_IA.git
cd crea_zik_electro_IA

python3 -m venv venv
source venv/bin/activate

# Installation en mode développement
pip install -e ".[dev]"

# Lancer les tests
pytest
```

## Configuration

### 1. Variables d'environnement

Créer un fichier `.env` à la racine du projet :

```env
# Claude API (optionnel si vous utilisez Ollama)
ANTHROPIC_API_KEY=sk-xxx

# Configuration Ollama (optionnel)
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma3:4b

# Configuration générale
LOG_LEVEL=INFO
DEBUG=false
```

> ⚠️ **Important** : Ne committez jamais `.env` (il est dans `.gitignore`)

### 2. Configuration Ollama (optionnel, pour modèle local)

```bash
# Installer Ollama : https://ollama.ai
# Ou sur Ubuntu/Debian :
curl -fsSL https://ollama.com/install.sh | sh

# Télécharger un modèle
ollama pull gemma3:4b

# Lancer le service
ollama serve
# Accessible sur http://localhost:11434
```

## Vérification de l'installation

```bash
# Vérifier Python
python3 --version  # 3.10+

# Vérifier les dépendances
pip list | grep librosa
pip list | grep fastapi

# Lancer un test simple
python3 -c "import crea_zik; print('✅ Import OK')"

# Lancer la suite de tests
pytest -v
```

## Dépannage

### Erreur : "No module named librosa"

```bash
pip install librosa
```

### Erreur : "Cannot connect to Ollama"

```bash
# Vérifier que Ollama est lancé
ollama serve
# Ou vérifier sur http://localhost:11434/api/tags
curl http://localhost:11434/api/tags
```

### Erreur : "ANTHROPIC_API_KEY not found"

```bash
# Créer .env ou définir la variable
export ANTHROPIC_API_KEY="sk-xxx"
```

### Problème avec les dépendances audio

Sur Linux/Debian :
```bash
sudo apt-get install libsndfile1 ffmpeg
pip install --upgrade librosa pydub
```

Sur macOS :
```bash
brew install libsndfile ffmpeg
pip install --upgrade librosa pydub
```

## Installation des dépendances optionnelles

### Pour deep learning avec PyTorch

```bash
pip install ".[torch]"
# ou
pip install torch>=2.1.1
```

### Pour TensorFlow

```bash
pip install ".[tensorflow]"
# ou
pip install tensorflow>=2.14.0
```

## Structure après installation

```
crea_zik_electro_IA/
├── venv/                    # Environnement virtuel
├── src/
│   └── crea_zik/           # Code source
├── tests/                  # Tests
├── examples/               # Exemples
├── .env                    # Variables (à créer)
└── ... (fichiers de config)
```

## Prochaines étapes

1. Consulter [README.md](./README.md)
2. Lancer `/start crea_zik` pour utiliser le protocole vibecoding
3. Voir [examples/](./examples/) pour des tutoriels
4. Contribuer : voir [CONTRIBUTING.md](./CONTRIBUTING.md)

## Support

Problèmes lors de l'installation ?

- 📧 Email: servomorph14@gmail.com
- 🐛 [Issues](https://github.com/ServOMorph/crea_zik_electro_IA/issues)
- 💬 [Discussions](https://github.com/ServOMorph/crea_zik_electro_IA/discussions)

