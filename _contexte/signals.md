# Signals — crea_zik   (MAJ 2026-06-19)

## Actions ouvertes
- [P1|ouvert] Décider : rester mono-piste (Kick) ou passer à un rack multi-pistes
- [P2|ouvert] Décider si Docker reste ou est retiré (prématuré sans backend)

## Actions fermées (session 2026-06-19)
- [P2|fermé] Renommer remote git en `origin` ✓
- [P1|fermé] Première UI : bouton son + séquenceur 16 steps + transport ✓

## Questions ouvertes
- Une seule piste (Kick) ou vrai rack multi-pistes maintenant ?

## Échéances

## Blocages

## Contexte chaud
- Audio : flux WASAPI persistant + mixage par callback (UI/audio.py). Ne PAS revenir à sd.play() par appel (latence + clics).
- Fréquence imposée par le device (48000 sur cette machine), le kick est régénéré à cette fréquence.
- Code UI dans UI/, pas dans src/. Le backend FastAPI/librosa du contexte n'est pas encore amorcé.

## Dernière session (2026-06-19)
# Session du 2026-06-19

## Décisions prises
- UI desktop en PyQt6 (vs web) ; son synthétisé (pas de samples)
- Moteur audio temps réel : flux de sortie persistant + mixage additif par callback
- Sortie audio via WASAPI low-latency (repli auto sur défaut)

## Livrables produits ou modifiés
- UI/audio.py : créé — synth kick + moteur audio (WASAPI, mixage voix)
- UI/main.py : créé — channel rack (bouton Kick, 16 steps, transport play/BPM, playhead)
- run.py : créé — lanceur avec auto-reload (watchdog) du dossier UI/
- requirements.txt : ajout sounddevice, PyQt6, watchdog

## Hypothèses validées / invalidées
- VALIDE : WASAPI low-latency = 22 ms (vs 104 ms en MME)
- INVALIDE : sd.play() par déclenchement -> pivot flux persistant + callback mixant
- INVALIDE : ouverture à 44100 Hz -> pivot fréquence native du device (48000)

## Prochaine étape exacte
Tester l'enchaînement séquenceur en conditions réelles (run.py). Puis décider
de l'extension : multi-pistes, contrôles (volume/swing), ou amorçage backend.

## Question bloquante pour la session suivante
Rester mono-piste (Kick) ou passer à un vrai rack multi-pistes maintenant ?
