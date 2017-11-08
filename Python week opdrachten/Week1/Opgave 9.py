# DNA en Genome applicatie

genome = """ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC
CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC
CTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG
AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCC
CTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG
TTTAATTACAGACCTGAA""".replace('\n','')
# A)
# Doorloop de sequence in een lus en zoek hierbij op de triplets ATG. Druk op het scherm de index af van de
# letter die volgt op een triplet ATG. Dit zijn 5 waarden 9, 111, 279, 337 en 341. Met behulp van slicing kun je
# triplets uit de sequence halen, bijvoorbeeld met s[i : i + 3] waarbij s de sequence en i een lopende variabele.

for i in range(len(genome) - 3):
    triplet = genome[i : i + 3]
    if triplet == "ATG":
        print(i + 4)

# B)
# Een gen is een sub-string van het genoom die begint na een triplet ATG en eindigt voor een triplet TAG, TAA
# of TGA. Bovendien is de lengte van een gen-string een veelvoud van 3 en het gen zelf bevat niet een van de
# triplets ATG, TAG, TAA of TGA. Schrijf een programma dat alle genen uit onderstaande sequence toont.
# Controleer je antwoord met: assert (len(gene) == 42 or len(gene) == 12)"""

found = False
start = -1
for i in range(len(genome) - 2):
    triplet = genome[i : i + 3]
    if triplet == "ATG":
        # possible start of gene
        start = i + 3
    elif (triplet == "TAG" or triplet == "TAA" or triplet == "TGA") and start != -1:
        # possible end of gene
        gene = genome[start : i]
        if len(gene) > 1 and len(gene) % 3 == 0:
            # gene is found
            found = True
            assert (len(gene) == 42 or len(gene) == 12)
            print(gene)
            start = -1 # find the next gene in the genome

if not found:
    print("no gene is found")

assert (len(gene) == 42 or len(gene) == 12)