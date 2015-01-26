from __future__ import division

#This is exercise 1 -> Calculating AT content

sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

length = len(sequence)
A = sequence.count("A")

T = sequence.count("T")

AT_total = A + T

AT_content = AT_total / length

print(str(AT_content))
