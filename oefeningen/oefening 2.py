# In deze oefening moet een genoom uit een string aangewezen worden.
# Er zijn 4 stukken dna die uit de DNA string gehaald moeten worden. Dit wordt gedaan via replace.
# Replace vervangt de waarde welke beschreven staan in de variabelen met de dnaReplace variabele

dna = 'ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA'

def ondekDNA(arg):
    dna = arg
    dna1 = 'ATG'
    dna2 = 'TAG'
    dna3 = 'TGA'
    dna4 = 'TAA'
    dnaReplace1 = '*ATG*'
    dnaReplace2 = '*TAG*'
    dnaReplace3 = '*TGA*'
    dnaReplace4 = '*TAA*'
    newDNA = dna.replace(dna1, dnaReplace1).replace(dna2, dnaReplace2).replace(dna3, dnaReplace3).replace(dna4, dnaReplace4)
    print(newDNA)

ondekDNA(dna)
