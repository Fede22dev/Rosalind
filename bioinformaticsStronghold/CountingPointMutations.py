def hamming_distance(dna_1, dna_2):
    count = 0
    for i in range(len(dna_1)):
        if dna_1[i] != dna_2[i]:
            count += 1
    return count


dna1 = "GGTTCACTGAACCCAGTGTATCAGCGTCGGTCACAGATAGCCCAATGGATCCCGGACATAGGCACGTGTTTGCTGAGAGTTCCGAAAGGTATCTTATGGTTCATAGCCGCCCCTGGTCGCTCACAGACGACATCGTGACCGGCTTTGGACGCGGAGCTAAAGTGAGTGAATGAGCGAGCCCATAATAAGTTAGAACATTCACCCGGTCGTCTCTCCAGTGTGCCAATCGCCCATGACCGTCTTGATGAAGATCCGCAAGCCTACAAAATTAATGTGTCAGCTGCGCCACAAACTCGTGAAGCGGTCTTCTACCTCCGACAGCTCCCCACCGATAAGAGACTCGAATCACTTGACTAGGCGTTTACAGAATCGCTAGACAACTCCAGGCATTATAGGCAGGAGTGAATTGCTTAATCGATCCTAAGCGTGTATCTGACTCGGTTTACATAAGCGCTTTCTGTTGCCTAGACCCCCACTTTTACTGCAGCAGGGCGATGTAATCATAGCCGCGGCTTGTCGGGCAGCGACGAGCGACCATATGGCTCCCTATCATTTGACCGGGCGGCGAAGTGTTATCCCCTAATATTACTATGACTCCTACCCAAGCGACCGCTGAGAGTCCCTATGCAGAGAGGGTGGTCCCCAACCCGGGGGCGTGTTCCGTCGAACAGTATGGACTATACTGCGCATGCACTACACCCCAGCTGCGCCGCGGTCATTGTAACTAATGCTTATGACTCAAGTCGCAAACCAAGACCTCTTGTCCGATACGGTGCAGTTGAAACCGCCGTCCGTTCACCAATTGCAGGGAGAGTGTTCCTACGGATAGAAGGGTGGTCACCGCTGTTTTCACGTATTGGTGCGAGACCAACTACTGATCTTTCGGAAAAGGGCCATATTACCTCAAACCGAGGTTCCTTATTA"
dna2 = "GGTCATTTCATCCTCCCCAAACTTCGTGGAGGACAGCTCCTAAACGAAATATCAAACCTTGGACTAAGTTGGGAGGTGATTACGAGTCTTTATGTATGGCACGTAGACGCTTCTAGACAGTTTGTGATGCTGTTGGTTTGGCCTGTTATCTCGGGGCTTTAACGGGTTCATTCAGGTGTTCTTCATAATTGCTTACATCCTAGGTGCCCTATCTTAGGCTTGTGATGCGCCCCTAAGCGTCTTGGCGAGCCTTCGACGGCCGAAAGCCCTGCTTTAAAACCTAAGCCGCTGGCCCATAAAGTGGTTCACTTTGGCTTCTAGCATCTTTCTGACAGAGCACCGGGATCTTTGTAGTGTGTCTCGACAGGACCTGTCCAAGAATCTGGTGATTGTGGGAAGGGGAGTTTTACTTAACCCGTTCTGATGGTGTAACTGCAGCTGTTTGTCTACGCGATGTCAATTTTCTAGGCTCCCAGCTGTTTGGCAGGTCCAGGGCGCAATGATCGGTCCTGCTTGTCCTGCACCTAGTACAGGCCAGATGTTCATTCGGCAACGCGCCGCTCGCTGAACAGATCGCCGCTAGCGTGACGATGTTCCCAAGTTGAAGGAAGCGTGTGTTTACCGGAGAGAGGTGGGAAGTTCTCTACCTGAGGACGTGATCTTTTATGCCGGAGCGCCTACAGTGCGGCTGCACCTGAATCGAGATCTCCGGCGATCATAATCTTTTACATTTTTGCCTAAAGTCCGCAACCACGCTAGCTTGTCCAACATTGTACAGAGGAAATACGAGTCCAGTCCCCGATTGCAGGGGTGTTATTCTTGCGGATACAAGGATGCACCCCCGGGCATCGCAGCCTTGGAGTTTGACAAACTACTTATCAGTTGGCAATTAGACAGATAACGCCAATGCTACTGGCACTACTC"

print(hamming_distance(dna1, dna2))
