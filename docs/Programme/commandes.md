# Les commandes exigibles du programme officiel



## 1. Opérateurs arithmétiques de base

|  Commande | Signification | Exemple | Commentaires |
|-----|----|----|----|
| ```+``` | addition | ```>>> 5 + 2``` <br /> ```7``` | |  
| ```-``` | soustraction | ```>>> 5 - 2``` <br /> ```3``` | |  
| ```*``` | multiplication | ```>>> 5 * 2``` <br /> ```10``` | |  
| ```/``` | division | ```>>> 7 / 2``` <br /> ```3.5``` <br />  ```>>> 10 / 2``` <br /> ```5.0```| Attention, le nombre renvoyé par cette division est toujours un nombre à virgule.|  
| ```**``` | puissance | ```>>> 10 ** 3``` <br /> ```1000``` | Attention, ce n'est pas le symbole ```^```.|  


## 2. Opérateurs logiques

Python possède deux mots-clés réservés ```True``` et ```False``` (appelés *booléens*).  

|  Commande | Signification | Exemple | Commentaires |
|-----|----|----|----|
| ```and``` | et | ```>>> True and False``` <br /> ```False``` | |  
| ```or``` | ou | ```>>> True or False``` <br /> ```True``` | | 
| ```not``` | négation | ```>>> not(True)``` <br /> ```False``` | | 


## 3. Opérateurs de comparaison

Ces opérateurs de comparaison renvoient systématiquement soit ```True```, soit ```False```.  

|  Commande | Signification | Exemple | Commentaires |
|-----|----|----|----|
| ```==``` | test d'égalité | ```>>> 4 + 3 == 8 - 1``` <br /> ```True``` | Attention à ne pas confondre avec le symbole ```=``` <br /> qui ne sert qu'à l'affectation|  
| ```>``` | test de supériorité | ```>>> 4 > 7``` <br /> ```False``` | | 
| ```>=``` | test de supériorité large | ```>>> 7 >= 7``` <br /> ```True``` | |
| ```<``` | test d'infériorité | ```>>> 4 < 7``` <br /> ```True``` | | 
| ```<=``` | test d'infériorité large | ```>>> 4 <= 4``` <br /> ```True``` | |
| ```!=``` | test de différence | ```>>> 3 + 2 != 4``` <br /> ```True``` | |



## 4. Structures de contrôle
|  Commande | Signification | Exemple | Commentaires |
|-----|----|----|----|
| ```nom = expression```  | affectation | ```>>> a = 1 + 3``` <br /> ```>>> a``` <br /> ```4``` | La 1ère  opération effectuée <br />est l'évaluation de la partie à droite du ```=```. | 
| ```if```  | si | ```if age >= 18: ``` <br /> &nbsp; &nbsp; &nbsp;    ```print("majeur")```  | Attention aux ```:``` en fin de ligne, <br />attention à l'indentation sous le ```if```.  | 
| ```else```  | sinon | ```if age >= 18: ``` <br /> &nbsp; &nbsp; &nbsp;    ```print("majeur")``` <br />  ```else: ``` <br /> &nbsp; &nbsp; &nbsp;    ```print("mineur")```| Attention à l'indentation. | 
| ```elif```  | sinon si| ```if age >= 18: ``` <br /> &nbsp; &nbsp; &nbsp;    ```print("adulte")``` <br />  ```elif age >= 14: ``` <br /> &nbsp; &nbsp; &nbsp;    ```print("ado")```<br />  ```else: ``` <br /> &nbsp; &nbsp; &nbsp;    ```print("enfant")```|```elif``` est une contraction<br /> d'un ```else``` et d'un ```if```. <br />Il permet de simplifier parfois les tests mais n'est jamais obligatoire.| 
| ```for ... in ...```  | boucle for | ```for n in [3, 5, 9]: ``` <br /> &nbsp; &nbsp; &nbsp;    ```print("gagné !")``` | La structure de boucle sert à répéter une instruction, <br/> lorsqu'une variable parcourt un ensemble énumérable.|
| ```while```  | boucle tant que | ```while points < 10 : ``` <br /> &nbsp; &nbsp; &nbsp;    ```print("continuez !")``` | Attention, il faut s'assurer qu'on puisse  <br/> bien sortir de cette boucle.| 
| ```def```  |  fonction | ```def welcome(): ``` <br /> &nbsp; &nbsp; &nbsp;    ```print("bonjour !")``` | Une fonction peut prendre aucun ou plusieurs paramètre(s).| 
| ```return```  |  renvoi | ```def affine(x): ``` <br /> &nbsp; &nbsp; &nbsp;    ```return 3*x + 2``` | À utiliser lorsque la fonction doit renvoyer une valeur. | 

## 5. Librairie ```numpy``` 


### 5.0 Importation

La librairie de calcul scientifique ```numpy``` peut s'importer de deux manières :


#### Méthode  1 (déconseillée)
```python
from numpy import *
```

Cette méthode est à déconseiller car elle importe la totalité de la bibliothèque.

#### Méthode  2 (à priviégier)
```python
import numpy as np
```

Toutes les commandes de ```numpy``` devront donc être préfixées par ```np.``` 

### 5.1 Commandes de base

|  Commande | Signification | Exemple | Commentaires |
|-----|----|----|----|
| ```np.e```  | constante d'euler | ```>>> np.e``` <br /> ```2.718281828459045```| | 
| ```np.pi```  | pi | ```>>> np.pi``` <br /> ```3.141592653589793```| | 
| ```np.exp()```  | fonction exponentielle | ```>>> np.exp(1)``` <br /> ```2.718281828459045```| | 
| ```np.log()```  | fonction logarithme | ```>>> np.log(np.e)``` <br /> ```1.0```| Logarithme de base ```e``` | 
| ```np.sqrt()```  | fonction racine carrée | ```>>> np.sqrt(2)``` <br /> ```1.4142135623730951```| | 
| ```np.abs()```  | fonction valeur absolue | ```>>> np.abs(-2)``` <br /> ```2```| | 
| ```np.floor()```  | fonction partie entière | ```>>> np.floor(4.2)``` <br /> ```4.0```| |

### 5.2 Opérations sur les matrices

|  Commande | Signification | Exemple | Commentaires |
|-----|----|----|----|
| ```np.array()```  | création d'une matrice | ```>>> np.array([[1,3],[0,5]])``` <br /> ```array([[ 1,  3],``` <br />  &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;```[0,  5]])``` | | 


Les opérateurs ```+```, ```-```, ```/```, ```*``` et ```**``` sont acceptées mais ne font que des opérations **terme à terme**. En particulier, le produit ```*``` n'effectue **pas** un produit matriciel classique. Il faut pour cela utiliser :

|  Commande | Signification | Exemple | Commentaires |
|-----|----|----|----|
| ```np.dot()```  | produit matriciel | ```>>> np.dot(A, B)```| Renvoie le produit matriciel des matrices A et B. | 
| ```np.sum()```  | somme | ```>>> np.sum([[1,3],[0,5]])``` <br /> ```2```| Somme des éléments d'une matrice. | 
| ```np.min()```  | minimum | ```>>> np.min([[1,3],[0,5]])``` <br /> ```0```| Mininum des éléments d'une matrice. | 
| ```np.max()```  | minimum | ```>>> np.max([[1,3],[0,5]])``` <br /> ```5```| Maximum des éléments d'une matrice. | 
| ```np.mean()```  | moyenne | ```>>> np.mean([[1,3],[0,5]])``` <br /> ```2.25```| Moyenne des éléments d'une matrice. | 
| ```np.cumsum()```  | somme cumulée | ```>>> np.cumsum([1, 3, 2, 4])``` <br /> ```array([ 1,  4,  6, 10])```| Somme cumulée des éléments d'une matrice. <br/> (ici d'un vecteur) | 
| ```np.median()```  | médiane | ```>>> np.median([1, 3, 2, 4])``` <br /> ```2.5```| Valeur médiane des éléments d'une matrice. <br/> (ici d'un vecteur) | 
| ```np.var()```  | variance | ```>>> np.var([1, 3, 2, 4])``` <br /> ```1.25```| Variance des éléments d'une matrice. <br/> (ici d'un vecteur) |
| ```np.std()```  | écart-type | ```>>> np.std([1, 3, 2, 4])``` <br /> ```1.118033988749895```| Écart-type (*standard deviation*) des éléments d'une matrice. <br/> (ici d'un vecteur) |


### 5.3 Sous-librairie ```random``` 

La partie du programme «Simulation de lois» utilisera la sous-librairie ```random``` de ```numpy```.

Elle sera importée par :

```python
import numpy.random as rd
```

|  Commande | Signification | Exemple | Commentaires |
|-----|----|----|----|
| ```rd.random()```  | nombre aléatoire dans [0;1[ | ```>>> rd.random()``` <br /> ```0.942591321534259 ```    | |


## 6. Librairie ```pandas``` 

La librairie ```pandas``` sera importée par :

```python
import pandas as pd
```

|  Commande | Signification | Exemple | Commentaires |
|-----|----|----|----|
| ```mean()```  | moyenne | ```>>> df = pd.DataFrame([2,4,10,3])``` <br /> ```>>> df.mean()``` <br /> ```0    4.75``` <br /> ```dtype: float64```  | Attention, ```mean()``` s'applique sur une ```dataframe```.   |
| ```std()```  | écart-type | ```>>> df = pd.DataFrame([2,4,10,3])``` <br /> ```>>> df.std()``` <br /> ```0    3.593976``` <br /> ```dtype: float64```  | Attention, ```std()``` s'applique sur une ```dataframe```.   |

## 7. Librairie ```matplotlib.pyplot``` 

La sous-librairie ```matplotlib.pyplot``` sera importée par :

```python
import matplotlib.pyplot as plt
```

|  Commande | Signification | Exemple | Commentaires |
|-----|----|----|----|
| ```plt.plot()```  | construction d'un graphique | ```>>> plt.plot([1,2,3], [15,12,17])``` | Crée un graphique (mais ne l'affiche pas) <br/> contenant les points (1,15), (2,12) et (3, 17).   |
| ```plt.show()```  | affichage | ```>>> plt.show()``` | Affiche un graphique précédemment créé.   |