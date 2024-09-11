input_filename1 = "Part1/title.tsv"
input_filename2 = "Part1/body.tsv"
output_filename = "Part1/clean_all.csv"

f0 = open(input_filename1, "r")
f1 = open(input_filename2, "r")
f2 = open(output_filename, "w")

for i in f0:
    line = i.split("\t")
    f2.write(line[0] + "," + line[1] + "\n")
for i in f1:
    line = i.split("\t")
    f2.write(line[0] + "," + line[1] + "\n")

f0.close()
f1.close()
f2.close()

