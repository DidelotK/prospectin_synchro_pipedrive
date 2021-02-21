# Synchronisation des contacts pipedrive dans pipedrive

## 1. Prérequis: Sur son pc
- Avoir python 3 d'installé (normalement présent sur tous les nouveaux PC)

## 2. Prérequis: Positionner ses données de configuration

Dans le fichier `conf.py` situé dans le dossier `utils` remplacez les valeur XXXXXX par les bonnes valeurs

Le contenu du fichier ressemble initialement à cela
```python
# PIPEDRIVE
PIPEDRIVE_COMPANE_NAME = 'XXXXXXXX'
PIPEDRIVE_API_TOKEN = 'XXXXXXXX'
PIPEDRIVE_LINKEDIN_PERSONFIELD_NAME = 'LinkedIn'

# PROSPECTIN
PROSPECTIN_API_TOKEN = 'XXXXXXXX'
PROSPECTIN_CURRENT_CAMPAIN = 'XXXXXXXX'
```

## Lancer la synchronisation

```bash
python main.py
```

## Configurer un synchronisation automatique avec votre crontab
```bash
crontab -e

# Ajouter cette ligne à la fin du fichier afin de synchroniser toutes les 2h vos contacts
0 */2 * * * python <PATH du fichier>/main.py
```
