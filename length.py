import sys


try:
	def main(argv):
		# Open the FASTA file
		with open(argv[1], "r") as f:
			# Initialize variables
			lgsequence = 0
			headseq = "null"
			# Read each line of the file
			for line in f:
				# If the line starts with a ">", it is the start of a new sequence
				if line[0] == ">":
					# Print the length and name of the previous sequence
					if lgsequence > 0:
						x = headseq[:-1].replace(' ','\t')
						print(f"{lgsequence}\t{x}")
					# Set the name of the new sequence and reset the length counter
					headseq = line[1:]
					lgsequence = 0
				# If the line does not start with a ">", add its length to the current sequence
				else:
					lgsequence += len(line) - 1
			# Print the length and name of the final sequence
			x = headseq[:-1].replace(' ','\t')
			print(f"{lgsequence}\t{x}")

	if __name__ == "__main__":
		main(sys.argv)
except ImportError:
	pass
