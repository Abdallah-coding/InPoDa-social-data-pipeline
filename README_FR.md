# InPoDa – Semantic Search on Legal Documents

## Contexte

Ce projet a été initialement réalisé il y a environ deux ans dans le cadre d’un travail académique en traitement de données.  
Il a récemment été relu et légèrement refactorisé afin d’améliorer la lisibilité du code, la cohérence des noms de fichiers et la structure générale du projet.

L’objectif était de mettre en place un système simple de recherche sémantique sur un corpus de textes (articles de loi), en utilisant des embeddings et la similarité cosinus.

---

## Objectif du projet

Le programme permet de :

- Charger un corpus de documents (un document par ligne dans un fichier `.txt`)
- Transformer chaque document en vecteur numérique (embedding)
- Transformer une requête utilisateur en vecteur
- Calculer la similarité cosinus entre la requête et chaque document
- Afficher les documents les plus pertinents

Il s’agit d’un mini moteur de recherche sémantique basé sur des représentations vectorielles.

---

## Fonctionnement

1. Les documents sont chargés depuis un fichier texte (ou un corpus par défaut).
2. Le modèle SentenceTransformer génère un embedding pour chaque document.
3. L'utilisateur entre une requête.
4. La similarité cosinus est calculée entre la requête et chaque document.
5. Les documents sont triés par score de similarité décroissant.
6. Les 3 documents les plus pertinents sont affichés.

Les embeddings sont également sauvegardés dans un fichier corpus_embeddings.json.

---

## Technologies utilisées

- Python  
- SentenceTransformers (paraphrase-MiniLM-L6-v2)  
- NumPy  
- JSON  

---

## Installation

Installer les dépendances :

```bash
pip install -r requirements.txt

Exécution:

Lancer le programme :
python semantic_search.py

Puis :

- Indiquer le nom du fichier .txt contenant le corpus ou taper None pour utiliser le corpus par défaut
- Entrer la requête à rechercher

```
---

## Structure du projet

InPoDa/
│

├── semantic_search.py

├── legal_corpus.txt

├── corpus_embeddings.json

├── requirements.txt

└── README.md


**Ce projet illustre :**
- l'utilisation d'embeddings pour la recherche sémantique
- la transformation de texte en représentations vectorielles
- le calcul de similarité cosinus
- une première approche du NLP appliqué
