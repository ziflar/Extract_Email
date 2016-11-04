
#!/usr/bin/env python
import re, sys, argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input text file.")
parser.add_argument("-o", "--output", default="output.txt", help="output text file.")
parser.add_argument("-f", "--format", default=0, help="format output. SEPARATE- {0}->Vertical {1}-> ,")
args = parser.parse_args()

try:

	email_pattern = re.compile('([.|\w]+@(\w+[.]\w+[.|\w+])\w+)')
	data = ""
	with open(args.input,'r') as data_line:
		for line in data_line:
			data+=line
	matches = re.findall(email_pattern, data)
	emails = [match[0] for match in matches]
	unique_emails = list(set(emails))


	if args.format==0:
		vert_mail = '\n'.join(unique_emails)
		fichier = open(args.output, "w")
		fichier.write(vert_mail)
		fichier.close()
	else:
		comma_mail = ', '.join(unique_emails)
		fichier = open(args.output, "w")
		fichier.write(comma_mail)
		fichier.close()

except Exception as E:print E
