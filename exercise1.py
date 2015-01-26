from __future__ import division

#exercise 1 


my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

length = len(my_dna)

a_count = my_dna.count('A')

t_count = my_dna.count('T')

at_content = (a_count + t_count) / length 


print(str(AT_content))
