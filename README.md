# python-genomic-data
Using Python for bioinformatics analysis of DNA sequences with MULTI-FASTA files. A few problems I worked on.

# HERE ARE THE PROBLEMS THAT I TRIED TO SOLVE WITH THE dna2.fasta FILE:

# INTRO:
Write a Python program that takes as input a file containing DNA sequences in multi-FASTA format, and computes the answers to the following questions.
The program should be able to perform the following tasks:
1. How many records are in the file? 
   -> The program should count the number of ">" in the multi-fasta file
2. What are the lengths of the sequences in the file? What is the longest sequence and what is the shortest sequence?
Is there more than one longest or shortest sequence? What are their identifiers? 
   -> Seperate the headers from the sequences, and seperate each individual sequence
3. Given an input reading frame on the forward strand (1, 2, or 3) the program should be able to identify all ORFs present in each sequence of the FASTA file,
and answer the following questions: What is the length of the longest ORF in the file? What is the identifier of the sequence containing the longest ORF?
For a given sequence identifier, what is the longest ORF contained in the sequence represented by that identifier?
What is the starting position of the longest ORF in the sequence that contains it?

# QUESTIONS:

-> input file: dna2.fasta

1) How many records are in the multi-FASTA file?
2) What is the length of the longest sequence in the file?
3) What is the length of the shortest sequence in the file?
4) What is the length of the longest ORF appearing in reading frame 2 of any of the sequences?
5) What is the starting position of the longest ORF in reading frame 3 in any of the sequences?
The position should indicate the character number where the ORF begins. For instance, the following ORF:
> sequence1
ATGCCCTAG
starts at position 1.
6) What is the length of the longest ORF appearing in any sequence and in any forward reading frame?
7) What is the length of the longest forward ORF that appears in the sequence with the identifier  gi|142022655|gb|EQ086233.1|16?
8) Find the most frequently occurring repeat of length 6 in all sequences. How many times does it occur in all?
9) Find all repeats of length 12 in the input file. Let's use Max to specify the number of copies
of the most frequent repeat of length 12. How many different 12-base sequences occur Max times?
10) Which one of the following repeats of length 7 has a maximum number of occurrences?
