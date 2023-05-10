#!/usr/bin/env python
# coding: utf-8

# In[9]:


# 1.STRUCTURE ITERATIVE
  # Elles permettent de répéter une certaine opération autant de fois que nécessaire
  #En outre, les boucles peuvent permettre de parcourir certaines séquences comme les chaînes de caractères pour, par exemple, en extraire chaque caractère.
  # avec la boucle POUR(FOR)
    #L'instruction for travaille sur des séquences. Elle est en fait spécialisée dans le parcours d'une séquence de plusieurs données
    #table de multiplication
n=int(input("entrez la valeur de n: "))
print ("voici la table de multiplication de ", n)
for i in range(1,11):
    print(i,"x",n," = ",i*n)


# In[118]:


# BOUCLE WHILE
#La syntaxe de while est : while condition: 
        # instruction 1  
        # instruction 2 
        # instruction N
        #Exemple:
n=int(input("entrez la valeur de n: "))
print("voici la table de multiplication de ", n)
i=0
while i<10:
    print(i+1,"x",n," = ",(i+1)*n)
    i+=1


# In[119]:


#PROGRAMME D'ENVOI D'ARGENT AIRTEL MONEY, AVEC LES STRUCTURES CONDITIONNELLES
code= input("entrez le code client: ")
if (code=='*501#'):
    a=int(input("choisissez votre devise:\n1.USD\n2.CDF \n3.Bureau de Change \n4.1GB 48h-100u \n5.Achat Unites/Forfait \n6.Balance \n 100u a 20350 FC. Des unites et forfaits au meilleur prix \n "))
    if (a==1 or a==2):
        b=int(input("choisissez: \n1.Envoi Argent\n2.Retrait d'argent \n3.Paiement \n4.Achat Forfaits \n5.Achat Unites \n6.Mon compte \n7.Services Financiers \n8.Surprise Bonus \n9.Aides  \n#Retour \n "))
        if b== 1:
            c=int(input("\n1.Entrer numero/Surnom \n2.Numeros favoris \n3.Annuler la transaction \n#Retour \n"))
            if c==1:
                d=int(input("\n Entrer numero/Surnom \n#Retour \n"))
                e=int(input("\n Entrer montant en CDF \n#Retour \n"))
                Pin=int(input("Entrer votre PIN pour confirmer que vous voulez envoyer CDF"))
                if Pin==2029:
                    print("Vous avez envoyé ", e , "CDF à ", d)
                else:
                    print("code incorrect")


# In[108]:


#2.LISTE DE DONNEES EN PYTHON
# exemple
i= 5
a=[i,'Germain']
a


# In[4]:


a[1]='Hermann' # si je veux modifier la valeur de l'indice1 de cette liste
a


# In[6]:


a[0]+25 # si je veux additionner une valeur avec une autre de la liste


# In[25]:


a[1]+' Lumbila lusuna' # on peut modifier ou faire des ajouts meme sur les chaines de caracteres 


# In[59]:


#3.  FONCTION
#Les fonctions permettent de regrouper plusieurs instructions dans un bloc qui sera appelé grâce à un nom
#On crée une fonction selon le schéma suivant :def nom_de_la_fonction(parametre1 , parametre2 , parametre3 , parametreN):
                                    # Bloc d'instructions
#Exemple
#Le code pour mettre notre table de multiplication par 7 dans une fonction serait donc :

n=int(input("entrez la valeur de n: "))
def table_multiplication():
   print(n) 
i=0
while i<10:
    print(i+1,"x",n," = ",(i+1)*n)
    i+=1

    



# In[81]:


def calcul_nbr(nbr1,nbr2):
    return nbr1-nbr2
reste=calcul_nbr(56,7)
print(reste)


# In[87]:


# fonction Lambda:généralement utilisée dans un certain contexte, pour lequel défnir une fonction à l'aide de def serait plus long et moins pratique.

f = lambda x: x * x #on a stoqué la fonction lambda dans une variable pour bien l'appeler. le resultat sera le carré du nombre

f(5)


# In[88]:


f(-18) # autrement, c'est (-18)*(-18)


# In[89]:


#4. MODULE

#Un module est grossièrement un bout de code que l'on a enfermé dans un fichier.Ils permettent de regrouper plusieurs fonctions selon le même principe. 
#Toutes les fonctions mathématiques, par exemple, peuvent être placées dans un module dédié aux mathématiques.
#exemple
import math
math.sqrt(16)# pour trouver la racine carrée de 16


# In[99]:


# ou encore:
import math as mathematiques
mathematiques.sqrt(25)


# In[94]:


from math import fabs
fabs(-33)# pour donner la valeur absolue d'un nombre


# In[ ]:


from math import * #Vous pouvez appeler toutes les variables et fonctions d'un module en tapant * à la place du nom de la fonction à importer
from math import * 
sqrt(4) 


# In[102]:


fabs(-90)


# In[106]:


#5.ORIENTE OBJET
# un objet est une structure de données, comme les variables, qui peut contenir elle-même d'autres variables et fonctions.
#un objet est issu d'une classe.
#Une classe est un modèle qui servira à construire un objet; c'est dans la classe qu'on va définir les méthodes propres à l'objet.
# Les développeurs de Python ont créé la classe str qui est utilisée pour créer des chaînes de caractères
prenom = "Hermann Germain" 
nom = "Lumbila"
age = 24
print("Je m'appelle {0} {1} et j'ai {2} ans.".format (prenom , nom, age)) 


# In[ ]:


# MODULE NUMPY


# In[32]:


# Dès que l’installation est finie, on peut importer ces deux modules. Pour cela, on utilise les instructions:import numpy as np
# Opérations de basessur les tableaux3
# Après avoir importé numpy, on peut commencer à créer nos premiers tableaux. Pour cela, il suffit d’utiliser l’instruction np.array, qui prend en paramètre la liste des nombres qui seront contenus dans le tableau.
# Par exemple si on veut initialiser un tableau avec les valeurs 23, 5, 12,45 et 76:
import numpy as np 
tableau = np.array([23, 5, 12,45,76]) 
tableau
#Les différences majeures entre les listes proposées par Python et les tableaux de Numpy sont: 
# — dans un tableau, tous les éléments doivent être du même type;
# — il y a un gain élevé de performance avec les tableaux.




# In[42]:


# on peut parcourir le tableau avec une boucle for, comme pour une liste
tableau = np.array([23, 5, 12,45,76]) 
for i in tableau:
    print(i) 


# In[45]:


#On peut aussi accéder manuellement à un élément du tableau (comme avec les listes, on commence à compter à partir de 0) et connaitre le nombre d’objet contenu dans le tableau:
tableau = np.array([23, 5, 12,45,76])
tableau[0]


# In[47]:


tableau[2]


# In[48]:


len(tableau)


# In[49]:


#UTILISATION DE SLICE 
#On on peut utiliser les slices pour sélectionner une partie du tableau 
#Exemples
tableau = np.array([23, 5, 12,45,76]) 
tableau[0:2] # de 0 inclu à 2 exclu


# In[33]:


tableau[1:] 


# In[34]:


tableau[:-1]


# In[35]:


#Nous avons aussi la possibilité d’ajouter, de supprimer et d’insérer des éléments dans les tableaux.
tableau = np.array([23, 5, 12,45,76]) 
np.append(tableau, 2) # Ajoute l'élément 2 à la fin du tableau 


# In[53]:


np.delete(tableau, 1) # Supprime l'élément à l'index 1 (ici l'entier 5)


# In[54]:


np.insert(tableau, 3, 14) # Insère l'élément 14 à l'index 3 


# In[56]:


#Les formules mathématiques s’utilisent directement sur les tableaux, celles-ci seront alors appliquées à tous les éléments du tableau:
tableau = np.array([23,  5, 12, 14, 45, 76])
tableau ** 2  # Met au carré les elements du tableau


# In[59]:


#Numpy permet aussi de créer un tableau avec des données aléatoires, en utilisant la fonction np.random.rand
#exemple
a=np.random.randint(1,5, size=(4,4))
a


# In[62]:


# Il y a aussi la fonction np.random.randint(max, size=n) qui retourne un tableau avec n valeurs comprises entre 0 et max (exclu).
a=np.random.randint(8, size=6) # retourne 6 elements compris entre 0 et 8 
a


# In[69]:


#fonction biens pratiques pour générer des tableaux:
np.zeros(5) # Un tableau de longueur 3 avec que le chiffre 0 


# In[71]:


np.ones(5) # Un tableau de longueur 4 avec que le chiffre 1 


# In[74]:


#Rechercher dans un tableau
#La fonction np.where prend en paramètre une condition sur les valeurs d’un tableau et va retourner l’index des éléments qui vérifient la condition. 
#La fonction np.extract renvoie les éléments qui vérifient la condition.
tableau=np.arange(1, 25) # Tableau avec les nombres entiers de 1 à 24 2 
np.where(tableau % 5 == 0) # L'index des nombres divisibles par 5 


# In[75]:


np.extract(tableau % 5 == 0, tableau) # Les nombres divisibles par 5 


# In[31]:


import numpy as np # pour importer la librairie NUMPY
np.ones(shape=5) # pour créer un tableau à une dimension, contenant 5 elements


