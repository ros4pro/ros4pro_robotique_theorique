# robotique_theorique

## Géométrie
### Modèle direct

Lancez la commande `roslaunch ros4pro_robotique_theorique scara_fake_direct.launch` pour lancer une *simu* de SCARA. Une fenêtre avec des sliders permet de bouger le bras.

Modifiez le script `src/geometrique_direct.py` en y mettant votre modèle géométrique direct. Il calcul la position de l'effecteur à partir des angles des articulations.

Lancez la coommande `rosrun ros4pro_robotique_theorique geometrique_direct.py` pour exécuter le script de test du modèle géométrique direct.

### Modèle direct

Lancez la commande `roslaunch ros4pro_robotique_theorique scara_fake_inverse.launch` pour lancer une *simu* de SCARA.

Modifiez le script `src/geometrique_inverse.py` en y mettant votre modèle géométrique inverse. Il calcul les angles et la position des articulations pour que l'effecteur sooit à la position voulue.

Lancez la coommande `rosrun ros4pro_robotique_theorique geometrique_inverse.py` pour exécuter le script de test du modèle géométrique inverse.

## Probabilités
Installez les biblioothèques nécessaires à l'exécution des démonstrations de probabilité pour la robotiique, dans un terminal exécutez les coommandes suivantes :

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip3 install matplotlib
pip3 install scipy
python3 histogram_filter.py
```

Pour lancer les démonstrations de probabilité allez dans le dossier `proba` et utilisez `python3` pour exécuter les fichiers, ex: `python3 extended_kalman_filter.py`.

