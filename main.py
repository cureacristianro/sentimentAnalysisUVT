from textblob import TextBlob
from collections import Counter

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
with open(r'2024_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

blob = TextBlob(text)
propozitii = blob.sentences

# Selecție propoziții care conțin cuvintele căutate
propozitii_relevante = [str(propozitie) for propozitie in propozitii if contine_cuvinte(str(propozitie), cuvinte_cautate)]

# Analiză sentimente pentru fiecare propoziție relevantă
sentimente = [TextBlob(propozitie).sentiment.polarity for propozitie in propozitii_relevante]

# Calcul sentiment mediu al propozițiilor relevante
sentiment_mediu = sum(sentimente) / len(sentimente)
print(sentiment_mediu)

#Maxim: 0.012146371661370017 (2014)
#Minim: 0.004263412329224124 (2020)
#Media: 0.0083

#1996: 0.007844319520260011
#1997: 0.007186541195944326
#1998: 0.00885524112966407
#1999: 0.009023727987419882
#2000: 0.006528895052137276
#2001: 0.005384541944874378
#2002: 0.0050758923351224795
#2003: 0.008281018869153127
#2004: 0.005696710406329729
#2005: 0.008406694541684101
#2006: 0.00859404304272723
#2007: 0.007767573660811504
#2008: 0.005258070773734858
#2009: 0.00884718966279453
#2010: 0.009087572730672969
#2011: 0.010206017252647803
#2012: 0.00596903307270964
#2013: 0.011059690176685262
#2014: 0.012146371661370017
#2015: 0.01146160276945489
#2016: 0.004581905586227716
#2017: 0.008206858733905456
#2018: 0.010423992159513664
#2019: 0.00983022275317268
#2020: 0.004263412329224124
#2021: 0.008989262293036687
#2022: 0.011617570920561746
#2023: 0.010653018584936657
#2024: 0.00941097021419701


