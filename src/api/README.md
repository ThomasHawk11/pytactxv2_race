# Turbo Vroum

# Description

Ce jeu est un jeu de course en vue du dessus s'inspirant du principe de la série de jeux vidéo [TrackMania](https://fr.wikipedia.org/wiki/TrackMania).

# 🎲 Règles du jeu

Le jeu consiste à déplacer une voiture sur un plateau de jeu définit par un circuit. Le but étant de réaliser le tour le plus rapide dans le temps impartit. Vous serez en concurrence avec d'autres joueurs avec qui vous vous batterez pour la première place. 

![Maquette](../../res/maquette.png)

# 🎮 Use cases

| N°  | Actions                                                                                                                  |
| --- | ------------------------------------------------------------------------------------------------------------------------ | 
| 1   | En tant que joueur, je peux participer à des courses multijoueurs et défier d'autres joueurs.                            | 
| 2   | En tant que joueur, je peux contrôler le déplacement d'un véhicule (accélération, freinage, direction)                   | 
| 3   | En tant que joueur, je peux voir mes statistiques de course (chrono, classement, meilleur temps personnel) en temps réel.| 
| 4   | En tant que joueur, je peux recommencer le circuit en plein mileu de la course.                                          | 
| 5   | En tant que joueur, je peux changer la couleur de mon véhicule                                                           |

**Fonctions utilisables** :
- ```update()``` : Récupérer les dernières valeurs des capteurs du robot sur le serveur et envoyer les requêtes tamponnées en une seule fois pour limiter la bande passante. A appeler dans la boucle principale au moins toutes les 10 msecs.
- ```accelerate(ax,ay)``` : Ajouter une force d'accélération à appliquer sur l'agent. La requête sera envoyée lors du prochain appel à update().
- ```move(dx,dy)``` : Demande un déplacement relatif sur la grille autour de la position précédente de l'agent en fonction des valeurs dx, dy spécifiées. La demande sera envoyée lors du prochain appel à update().
- ```moveTowards(x,y)``` : Demande un déplacement d'un pas vers la direction absolue x,y spécifiée sur la grille. La demande sera envoyée lors du prochain appel à update().
- ```lookAt(dir)``` : Demande une rotation de l'agent sur la grille. Dir doit être un nombre entier allant de 0 (est) à 3 (sud). La demande sera envoyée lors du prochain appel à update().

# ✅ Pré-requis
- Un ordinateur relié à Internet avec un navigateur web Chrome ou Firefox installé
- Environnement de développement ([VSCode](https://code.visualstudio.com/) ou [Replit](https://replit.com/))
- Installer [Python](https://www.python.org/downloads/)

# ⚙️ Installation
 - Ouvrir un invite de commandes
- Cloner le projet
```
git clone https://github.com/ThomasHawk11/pytactxv2_race.git
```
- Ouvrez le projet dans votre IDE préféré.
- Faites chauffer la gomme sur le [circuit](https://play.jusdeliens.com/tactx/)
- 3...2...1...Développez !
# 🧑‍💻 Auteurs
**Thomas PLANTAIS, Mathieu ORDONNAUD, Mylan MEGARD, Romain LESIEUR**
# ⚖️ License [CC BY-NC 4.0 Deed](https://creativecommons.org/licenses/by-nc/4.0/)
