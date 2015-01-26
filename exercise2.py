from __future__ import division

#this is exercise 2 - complementing DNA

sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

sequence2 = sequence.replace("A", "t")

seqeunce3 = sequence2.replace("C", "g")

sequence4 = seqeunce3.replace("G", "c")

sequence5 = sequence4.replace("T", "a")


print(sequence5.upper())
