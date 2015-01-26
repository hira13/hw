from __future__ import division

#Splicing out introns

#1

my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon_1 = my_dna[0:63]
exon_2 = my_dna[90:len(sequence)]

print("Coding region: " + exon_1 + exon_2)


#2

lengthtotal = len(sequence)

lengthexon = len(exon_1) + len (exon_2)

percent = lengthexon/lengthtotal * 100

print("The percentage of the sequence that is coding is: " + str(percent) + "%")


#3


intron = my_dna[63:90]

print(exon_1 + intron.lower() + exon_2)
