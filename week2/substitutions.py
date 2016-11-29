# substitutions.py
import random

def count_bases(sequence):
	"""
	Returns a count of how many of each nucleotide (A,C,T,G) exist in the DNA sequence.
	"""
	A = 0
	T = 0
	C = 0
	G = 0
	for i in sequence:
		if i == "A":
			A = A + 1
		elif i == "T":
			T = T + 1
		elif i == "C":
			C = C + 1
		elif i == "G":
			G = G + 1
	print A , T, G, C


def complement(sequence):
	new_string = ""
	for i  in sequence:
		if i == "A":
			new_string = new_string + "T"
		elif i == "T":
			new_string = new_string + "A"
		elif i == "C":
			new_string = new_string + "G"
		elif i == "G":
			new_string = new_string + "C"
	return new_string

	


def transcribe_dna(sequence):
	new_string = ""
	for i  in sequence:
		if i == "A":
			new_string = new_string + "U"
		elif i == "T":
			new_string = new_string + "A"
		elif i == "C":
			new_string = new_string + "G"
		elif i == "G":
			new_string = new_string + "C"
	return new_string



def translate_rna(sequence):

	AA = []

	aminoAcids = {'UUU':'Phe', 'UUC':'Phe', 'UUA':'Leu', 'UUG':'Leu', 'UCU':'Ser','UCC':'Ser', 'UCA':'Ser', 'UCG':'Ser', 'UAU':'Tyr', 'UAC':'Tyr','UAA':'Stop', 'UAG':'Stop', 'UGU':'Cys', 'UGC':'Cys','UGA':'Stop', 'UGG':'Trp', 'CUU':'Leu', 'CUC':'Leu', 'CUA':'Leu','CUG':'Leu', 'CCU':'Pro', 'CCC':'Pro', 'CCA':'Pro', 'CCG':'Pro','CAU':'His', 'CAC':'His', 'CAA':'Gln', 'CAG':'Glyn', 'CGU':'Arg','CGC':'Arg','CGA':'Arg', 'CGG':'Arg', 'AUU':'Ile', 'AUC':'Ile','AUA':'Ile', 'AUG':'Met', 'ACU':'Thr', 'ACC':'Thr', 'ACA':'Thr','ACG':'Thr', 'AAU':'Asn', 'AAC':'Asn', 'AAA':'Lys', 'AAG':'Lys','AGU':'Ser', 'AGC':'Ser', 'AGA':'Arg', 'AGG':'Arg', 'GUU':'Val','GUC':'Val', 'GUA':'Val', 'GUG':'Val', 'GCU':'Ala', 'GCC':'Ala','GCA':'Ala', 'GCG':'Ala', 'GAU':'Asp', 'GAC':'Asp', 'GAA':'Glu','GAG':'Glu', 'GGU':'Gly', 'GGC':'Gly', 'GGA':'Gly', 'GGG':'Gly'}
	
	index = 0
	for i in range(len(sequence)/3):
		codon = ''
		codon = codon + sequence[index]
		codon = codon + sequence[index + 1]
		codon = codon + sequence[index + 2]
		AA.append(aminoAcids[codon])
		index = index + 3

	return AA
	print AA


def random_substitution(sequence):
	"""
	Replaces a random base position in the input string with a different base, 
	and returns the new string, simulating a subsitution mutation.
	"""
	pass

def is_synonymous(sequence1, sequence2):
	"""
	Return True if the two DNA sequences produce the same amino acid sequence,
	and False otherwise. 
	"""
	pass

def count_synonymous(sequence, num_trials=100):
	"""
	Run 100 trials in which we simulate a random substitution, and count how 
	many of the random substitutions result in a nonsynonymous vs
	synonymous(silent) mutation.
	"""
	pass


