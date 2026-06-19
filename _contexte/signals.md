# Signals — crea_zik   (MAJ 2026-06-19)

## Actions ouvertes
- [P1|ouvert] Décider si Docker reste ou est retiré (prématuré sans backend)

## Actions fermées (session 2026-06-19)
- [P1|fermé] Passage au rack multi-pistes (kick + snare + hihat) ✓
- [P1|fermé] Bouton mute par piste ✓
- [P1|fermé] Volume par piste (QDial) ✓
- [P1|fermé] Save / Load pattern JSON avec dossier SAV par défaut ✓
- [P1|fermé] Panneau réglages instrument par piste (temps réel) ✓
- [P1|fermé] Correction saturation audio (tanh soft clip + MASTER_GAIN) ✓

## Questions ouvertes

## Échéances

## Blocages

## Contexte chaud
- Audio : flux WASAPI persistant + mixage par callback (UI/audio.py). Ne PAS revenir à sd.play().
- MASTER_GAIN = 0.35 — calibré pour éviter la compression tanh sur 3 voix simultanées.
- Samples pré-calculés à l'init, régénérés sous lock via update_kick/snare/hihat() au changement de param.
- Code UI dans UI/, backend FastAPI/librosa pas encore amorcé.
- Dossier de sauvegarde : D:\ServOMorph\crea_zik_electro_IA\SAV

## Dernière session (2026-06-19)
# Session du 2026-06-19

## Décisions prises
- Passage au rack multi-pistes : kick, snare, hihat (synthèse bruit blanc pour snare/hihat)
- Correction saturation : hard clip remplacé par tanh + MASTER_GAIN=0.35
- Réglages instrument exposés en temps réel via panneaux collapsibles par piste

## Livrables produits ou modifiés
- UI/audio.py : ajout synth_snare, synth_hihat, update_kick/snare/hihat, MASTER_GAIN=0.35, soft clip tanh
- UI/main.py : rack multi-pistes, mute, volume (QDial), save/load JSON, panneaux réglages instrument
- SAV/ : dossier créé, dossier par défaut des dialogues save/load

## Hypothèses validées / invalidées
- VALIDE : hard clip = source de saturation audible sur voix simultanées
- VALIDE : MASTER_GAIN=0.35 + tanh supprime la compression inter-pistes
- INVALIDE : MASTER_GAIN=0.6 -> perte de 0.146 sur la snare quand kick simultané

## Prochaine étape exacte
Tester les réglages instrument en conditions réelles (run.py).
Décider de la prochaine feature : swing, effets (reverb/delay), ou amorçage backend IA.

## Question bloquante pour la session suivante
Aucune
