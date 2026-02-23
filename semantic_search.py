import numpy as np
import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

document = [
    "Toute personne a droit au respect de sa vie privée et familiale.",
    "Nul ne peut être arbitrairement détenu ou emprisonné.",
    "Les droits de l'homme doivent être protégées.",
    "Le climat change, il est temps d'agir."
]

def docs(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as file:
        documents = [line.strip() for line in file if line.strip()]
    return documents

def similaritees_methode_cosinus(vecteur1, vecteur2):
    # petit check pour éviter division par 0
    denom = (np.linalg.norm(vecteur1) * np.linalg.norm(vecteur2))
    if denom == 0:
        return 0
    return np.dot(vecteur1, vecteur2) / denom

def recherche(x):
    vect_x = model.encode([x])[0]
    return vect_x

def main():
    nom_fichier = input("Nom du fichier à analyser (ex: legal_corpus.txt) ? Tapez 'None' pour le document par défaut : ")
    x = input("Que cherchez-vous ? ")

    if nom_fichier == "None":
        documents = document
    else:
        documents = docs(nom_fichier)

    # on calcule les embeddings
    document_vect = model.encode(documents)

    # on prépare ce qu'on va sauvegarder
    vect_data = []
    for i in range(len(documents)):
        vect_data.append({
            "id": i,
            "text": documents[i],
            "embedding": document_vect[i].tolist()
        })

    # sauvegarde (optionnel mais utile)
    with open("corpus_embeddings.json", "w", encoding="utf-8") as outfile:
        json.dump(vect_data, outfile, indent=4, ensure_ascii=False)

    # recherche (sans relire le json)
    query_vec = recherche(x)

    similaires = []
    for doc in vect_data:
        score = similaritees_methode_cosinus(query_vec, np.array(doc["embedding"]))
        similaires.append((doc["text"], score))

    similaires = sorted(similaires, key=lambda t: t[1], reverse=True)

    print("\nDocuments les plus pertinents :")
    for text, score in similaires[:3]:
        print(f"Document: {text} | Similarité: {score*100:.2f}%")

main()

