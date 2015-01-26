from __future__ import division

#this is exercise 4 <- Splicing out introns

# 1

sequence = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon_1 = sequence[0:64]
exon_2 = sequence[91:len(sequence)]

print("Coding region: " + exon_1 + exon_2)


#2

lengthtotal = len(sequence)

lengthexon = len(exon_1) + len (exon_2)

percent = lengthexon/lengthtotal * 100

print("The percentage of the sequence that is coding is: " + str(percent) + "%")


#3


intron = sequence[63:90]

print(exon_1 + intron.lower() + exon_2)
