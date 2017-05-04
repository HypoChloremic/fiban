# Fiban
# (c) 2017 Ali Rassolie

import argparse as ap

def genout(infile=None):
	with open(infile, "r") as file:
		occurence = 0
		tot = 0
		for i, line in enumerate(file):
			clean_line = line.replace("\n", "").split("\t")
			tot += 1
			if float(clean_line[4]) < 10:
				occurence += 1
		return tot, occurence, (occurence/tot)

if __name__ == '__main__':
	the_arguments = ap.ArgumentParser()		
	the_arguments.add_argument("-i", "--infile",  help="The name of the file", nargs=1)
	opts = the_arguments.parse_args()
	infile = opts.infile[0]
	with open("{}_output.vcf".format(infile), "w") as file:
		tot, occurence, ratio = genout(infile=infile)
		file.write("File: {}\nTot: {}\nOccurence: {}\nRatio: {}".format(infile, tot, occurence, ratio))
	print("File: {}\nTot: {}\nOccurence: {}\nRatio: {}".format(infile, tot, occurence, ratio))