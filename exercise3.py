from __future__ import division

#this is exercise 3 <- Restriction fragment lengths

sequence = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

strand1 = sequence.find("GAATTC") + 1

strand2 = len(sequence) - strand1

print("The first strand is of length:" + str(strand1))


print("The second strand is of length:" + str(strand2))
