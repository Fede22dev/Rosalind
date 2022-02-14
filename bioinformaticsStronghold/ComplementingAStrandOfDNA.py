dna = "CCAACATATTAAGGTGTCAACGGAAACGTCGCAATCCACTACAAACAATTTCTATAATACTCTCCGAACGGCGGCAGACCCTTTGTACCCACCGGGATACTACGTGCATTGTGTCGGGGGCAAATCGTAACGTCTTCCTCAGCCCAGCAGCGGGGGATCGCTAGAGACGATAAAATAGGTGTTGGGCATAAGGTCACATTAATAGGAATCAGGCACCAAAAGTAGCTCGTAAGGCAGGTTCAGATCGACAAATCTGTTCTTGAACTGCCCCCCGGTGTCTTTTTGATAAAGCCTACGGTGACGGTCTGACCAGGCAAACGGCCTTAGGAACATACTACGTGGGATCAAGACACCCTAGGTCCGCCTAGTACGGAGGAGGGCACAACTCTGACGTCCCAGCCGTAGACCTCGACCCTACTTTAACGGCCCATAATGTAAAAGTCTTGATAGCCGTCTCCTAACCAAGTACAGCGAACCGTGTAACAGCTCTCTAGGGTCATATAATTAATTTCCTAGAGACGGATCCTATCTAAGACTCTCGAATTCTCGTCCTCTGCATTTTGATACTGGGCTAGGTTGGCAATCCTATCAACGAACAACTCAGGCCGTTTCCGTTAGGGTGAGACAGCCCTGTCCAGCCAGAGGTATACGACTACGTGTCCGGGATTTGCGGTGCCCGTGATCGCTATGCCCTTCGCCGACTATGTATCACAATCCCCTATCTGAGAGAAAATTTCTGTGTTCCGAACTCCCCGTACGGATCTCACGCTATTTGCGGGACAATGGGCTGGTTAAGTATGGATAGAGGCAGGTTCGTACGACACGACGTCGTTCCCTAATACCGGGGTATGTGGCAGGCCTCGCGAGATGGTGTACTATGCCCGTAACCCTCACTCGCTTTAAAGTTTTACGAAC"

reversedDna = dna[::-1]
complementary = reversedDna.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')

print(complementary.upper())
