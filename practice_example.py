#!/usr/bin/env python3
fastaFile = "dna_example.fasta"

fileObj = open (fastaFile, 'r')
fa = fileObj.read()             # this is a single string

#1. How many records are there?
    # Count the number of '>'

num_rec = fa.count('>')
print(num_rec)

fileObj.close()

##################################################

#2.  What are the lengths of the sequences in the file? What is the longest sequence and what is the shortest sequence? Is there more than one longest or shortest sequence? What are their identifiers? 

fileObj = open (fastaFile, 'r')

flines = fileObj.readlines()    # This is a list of all lines
#check what the lines look like

# for line in flines:
#     line = line.strip()
#     print (line)

header_list = []
sequence = ""

for i in range(len(flines)):            # flines is a list, i is index
    line = flines[i].strip()            # line is a string 
    if line[0] == '>':
        header_list.append(line[1:])

#print(header_list)                      # This is a record of all headers

for line in flines:
    line = line.strip()
    if line[0] == '>':
        line = '\n'
    sequence = sequence + line
    
seq_list = sequence.split('\n')
seq_list = seq_list[1:]
#print(seq_list)                         # This is a record of all sequences


# Dictionary to record the lengths of each sample

seq_len = {}

for seq in seq_list:
    seq_len[seq] = len(seq)
#print(seq_len)
print()
#print(header_list)

# Max and Min length sequence

max_len = sorted(seq_len.values())[-1]
min_len = sorted(seq_len.values())[0]
print("The longest sequence length is", max_len, "and the shortest sequence length is" ,min_len)
print()

# Fetch the longest and shortest sequences!
num_longest = 0
num_shortest = 0
longest_seq = ""
shortest_seq = ""
for seq, length in seq_len.items():
    if length == max_len:
        num_longest += 1
        longest_seq = longest_seq + seq 
        print("The longest sequence is: \n" + seq + "\nAnd it's length is " + str(length))
    if length == min_len:
        num_shortest += 1
        shortest_seq = shortest_seq + seq
        print("The shortest sequence is: \n" + seq + "\nAnd it's length is " + str(length))
print("\nThe number of longest sequences is", num_longest)
print("\nThe number of shortest sequences is", num_shortest)
print()

# Fetch the identifiers of the longest and shortest sequence!
    # The logic is:
    # First get the index of the longest and shortest seq
    # Since headers and sequences are arranged in the same order
    # The index will correspond to the header of the sequence
    
keyList = list(seq_len.keys())
for i in range(len(keyList)):
    key = keyList[i]
    if key == longest_seq:
        max_id = i
    if key == shortest_seq:
        min_id = i
print("The identifier for the longest sequence is: \n"+ header_list[max_id])
print("The identifier for the shortest sequence is: \n" + header_list[min_id])
print()

#################################################

#3. ORF Problem

# Given sequence, reading frame, find position of start and stop codon

#def all_orf(sequence, frame):
    #sequence = sequence.lower()
    #startCodon = ['atg']
    #stopCodon = ['tga','taa','tag']
    
    ## loop through sequence from frame = 0 to frame = len(sequence)
    ## stepping through 3 bases at a time
    #for i in range(frame, len(sequence), 3):
        ##define the codon
        #codon = seq[i:i+3]      # the first codon will be indices 0, 1, 2 (3 not included)
        #print(codon)
        ##fetch index of start codon
        #if codon in startCodon:
            #start_index = sequence.find(codon)
            #print(start_index)
    #print()
            
s = "CGCGCCGCTTGACGATGCCCACGCGGCGTTTGACGACCGGCTCGACGAGCGGCACGCTCGTGAGAATCGGGTGGTCGTGCCCGGGCATCGCCATCGACGGCACCGCGGCGACGCCGAGCCCCGCCTATGCGATCAAGCCGAGCAGGGTCGTCACGTGGCGCGCTTCGCATACGCTCGGCCCCCGCGGCGCCACGGCGGCCAGCGCCTGGTCGAGCAACAGGCGGTTCCCGGAAGTCTTGTCCACCGACACGTAATCGTGCTCGTACAGTTCGTTCCAGGTAACGCGCTTCTTGCGCGCGAGCGGATGGTCGCGGCGGCAGGCAGCGACGAACCGCTCCTGGAGCAACATCTTGAACTCGATGTCGGATTCCTGGCTGCCCATGAAGCTCACGCCGAAATCGGCTTCGCCGCTGATGACGGCGCCCAGCACCTCGTTCGCGCTCGCGTCCAGCAGCTTGACCCGGATGCGCGGAAAGCGCTGATGATAGCGCGCGATGATGGCCGGCAGAAAGTAGTAGGCGACCATGGAGGGCACGCACGCGATGGTCACATGGCCCAGGCGGCTCGACGACACGTCGCGAATGCCGAGCAGCGCCGCATCGAGATCGTCGAGCAGCTGTTCGGCGCTCTGGGCGAACACGCGGCCGACCGTGGTGAGCGCGACGCGACGCGTGGTGCGCTCGAACAGGCGCACGCCGAGCGCTTCCTCGAGCTTGTCGATCCGGCGACTCAACGCGGGCTGGGAAATGCTGACCGATTCCGCGGCCTTGCGGAAACTGCCCGTTTCCACGACCGCGCGAAACGCCTGCAAGTCGTTCAAGTCGAAGTTGATCCCCACGGGCGCGTCTCCCCATCTCAGATGGGGCGTATTTTGCATGATTTCGCCGGGCGGCCGCATCGGCGCGGCACGCATTCGCGCCACCCTCGATCGCAACCGCGTGCGTGAGCGTGCGGCCTGGCCGTCGATCCGCCGCGCGTCGATGTCGATGGGGGGCGTCGAGCCTGCGGGCCTTACGGCGCAAGCAGGCCGCGTGCGGCCAGATTGGCATACAGCGCGCGCACGCCGAAGGTCCTAAGGCGCGATCTCGGTGCACAGCCGCACGGTGTTGACGAGTGCGCCGAGCG"

for i in range(0, len(s), 3):
    start = s.find('atg')
    orf = ""
    
# INCOMPLETE
    

