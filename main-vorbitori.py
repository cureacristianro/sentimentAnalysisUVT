from textblob import TextBlob
from collections import Counter, defaultdict
import re

# Lista de cuvinte cheie
cuvinte_cautate = []
with open(r'cuvinte_cheie.txt', 'r', encoding='utf-8') as file:
    cuvinte_cautate = [line.strip() for line in file]
print("Cuvinte căutate:", cuvinte_cautate)

# Verificare propozitii
def contine_cuvinte(propozitie, cuvinte):
    for cuvant in cuvinte:
        if cuvant in propozitie:
            return True
    return False

# Citire text
with open(r'1996_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Găsirea vorbitorilor și a propozițiilor aferente
def extrage_propozitii_vorbitori(text):
    pattern = r'([A-Z][a-z]+ [A-Z][a-z]+):'
    matches = re.split(pattern, text)
    vorbitori_propozitii = defaultdict(list)

    # Gruparea numelor vorbitorilor cu propozițiile respective
    for i in range(1, len(matches), 2):
        vorbitor = matches[i]
        propozitii_text = matches[i + 1]
        blob = TextBlob(propozitii_text)
        propozitii = blob.sentences
        vorbitori_propozitii[vorbitor].extend(propozitii)

    return vorbitori_propozitii

vorbitori_propozitii = extrage_propozitii_vorbitori(text)

# Cele mai frecvente cuvinte de mediu
def cuvinte_frecvente(propozitii, cuvinte):
    counter = Counter()
    for propozitie in propozitii:
        for cuvant in cuvinte:
            counter[cuvant] += propozitie.lower().split().count(cuvant.lower())
    return counter.most_common()

# Analiză sentimente și cuvinte frecvente pentru fiecare vorbitor
rezultate_vorbitori = {}
for vorbitor, propozitii in vorbitori_propozitii.items():
    propozitii_relevante = [str(propozitie) for propozitie in propozitii if
                            contine_cuvinte(str(propozitie), cuvinte_cautate)]

    # Analizăm sentimentele pentru fiecare propoziție relevantă
    sentimente = [TextBlob(propozitie).sentiment.polarity for propozitie in propozitii_relevante]
    sentiment_mediu = sum(sentimente) / len(sentimente)

    # Obținem cele mai frecvente cuvinte din propozițiile relevante
    frecvente = cuvinte_frecvente(propozitii_relevante, cuvinte_cautate)

    rezultate_vorbitori[vorbitor] = {
        'sentiment_mediu': sentiment_mediu,
        'cuvinte_frecvente': frecvente
    }

# Rezultatele pentru fiecare vorbitor
for vorbitor, rezultate in rezultate_vorbitori.items():
    print(f"Vorbitor: {vorbitor}")
    print(f"Sentiment mediu: {rezultate['sentiment_mediu']}")
    print(f"Cuvinte frecvente: {rezultate['cuvinte_frecvente']}")
    print()