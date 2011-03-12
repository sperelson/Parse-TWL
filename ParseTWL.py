import pdb
import os
file = open("TWL.txt", 'r')
if not os.path.exists(".\\dict\\AA"):
    os.makedirs(".\\dict\\AA")
# All file names end with an 'f' to prevent 'CON' causing an issue
fout = open(".\\dict\\AA\\AAHf.txt", 'w')
fout2 = open(".\\dict\\dbls.txt", 'w')

line = file.readline()
line = line.rstrip("\r")
line = line.rstrip("\n")
text = "0" + line + "\n"
x = "%x" % len(line)
counter = 0
fout2.write("1AA\n")
two = "AA"
while 1:
	s = file.readline()
	if not s:
		break;
	s = s.rstrip("\r")
	s = s.rstrip("\n")
	if len(s) == 2 and line != s:
		if two != s:
			fout2.write("1" + s[:2] + "\n")
			two = s
	elif len(s) > 2 and line[:3] != s[:3]:
		if two != s[:2]:
			fout2.write("0" + s[:2] + "\n")
			two = s[:2]
		line = s
		#pdb.set_trace()
		fout.write(text)
		fout.close()
		if not os.path.exists(".\\dict\\" + line[:2]):
			os.makedirs(".\\dict\\" + line[:2])
		fout = open(".\\dict\\" + line[:2] + "\\" + line[:3] + "f.txt", 'w')
		text = "0" + line + "\n"
		x = "%x" % len(line)
		counter = 0
	else:
# Compare the starting letters until they don't match
		if len(line) > len(s):
			s1 = s
			s2 = line
		else:
			s1 = line
			s2 = s
		i = 0
		for c in s1:
			if not s2[i] == c:
				break
			else:
				i = i + 1;
		x = "%x" % i
		part = s[i:]
		text = text + x + part + "\n"
		counter = counter + 1
		if counter >= 1000:
			fout.write(text)
			text = ""
			counter = 0
		line = s
fout.write(text)
fout.close()
fout2.close()
file.close()
