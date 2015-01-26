from __future__ import division

#this is exercise 4 <- Splicing out introns

# 1

sequence = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon_1 = sequence[0:64]
exon_2 = sequence[91:len(sequence)]

print("Coding region: " + exon_1 + exon_2)

