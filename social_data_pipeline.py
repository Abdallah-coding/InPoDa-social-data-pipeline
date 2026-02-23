import numpy as np
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

document = ["Toute personne a droit au respect de sa vie privée et familiale.",
             "Nul ne peut-être arbitrairement détenu ou emprisonné.",
             "Les droits de l'homme doivent être protégées.",
             " Le climat change, il est temps d'agir."]


def docs(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as file:
        documents = [line.strip() for line in file]
    return documents


def similaritees_methode_cosinus(vecteur1, vecteur2):

    similarite = np.dot(vecteur1, vecteur2) / (np.linalg.norm(vecteur1) * np.linalg.norm(vecteur2))

    return similarite


def recherche(x):
    vect_x = model.encode([x])[0]

    return vect_x


def main():

    nom_fichier = str(input("Quel est le nom du fichier à analyser (nom_du_fichier.txt) ? Tapez 'None' si vous voulez un document par défaut "))
    x = str(input("Que cherchez-vous ? "))
    if nom_fichier == "None":
        documents = document
    else:
        documents = docs(nom_fichier)


    document_vect = model.encode(documents)
    vect_data = [{"id": i, "text": doc, "embedding": embedding.tolist()} for i, (doc, embedding) in enumerate(zip(documents, document_vect))]

    with open("document_vect.json", "w") as infile:
        json.dump(vect_data, infile, indent=4)

    with open("document_vect.json", "r") as inf:
        vect_data = json.load(inf)

    similaires = [(doc["text"], similaritees_methode_cosinus(recherche(x), np.array(doc["embedding"]))) for doc in vect_data]
    similaires = sorted(similaires, key=lambda x: x[1], reverse=True)

    print("Documents les plus pertinents:")
    for text, score in similaires[:3]:
        print(f"Document: {text}, Similarité en %: {score*100:.2f}")


main()


