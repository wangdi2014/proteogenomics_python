import sys


if len(sys.argv[1:])<=1:  ### Indicates that there are insufficient number of command-line arguments
    print "Warning! wrong command, please read the mannual in Readme.txt."
    print "Example: python prepare_annovar_input.py --input example_vardb_6rf_novpep.hg19cor.txt --output example_novpep_avinput.txt"
else:
    options, remainder = getopt.getopt(sys.argv[1:],'', ['input=','output='])
    for opt, arg in options:
        if opt == '--annovar_out': annovar_file=arg
        if opt == '--input': input_file=arg
        elif opt == '--output': output_file=arg
        else:
            print "Warning! Command-line argument: %s not recognized. Exiting..." % opt; sys.exit()


input1=open(annovar_file,"r") # annovar output
input2=open(input_file,"r") # novel pep cor blastout
output=open(output_file,"w")

category={}
while True:
    line1=input1.readline()
    line2=input1.readline()
    if not line2:break
    row1=line1.strip().split("\t")
    row2=line2.strip().split("\t")
    pep=row1[-1].replace("Comments:Seq=","")
    if row1[0]==row2[0]:
        category[pep]=[row1[0],row1[1]]
    else:
        fun=row1[0]+"-"+row2[0]
        category[pep]=[fun,row1[1]+","+row2[1]]

print len(category)

header=input2.readline().strip().split("\t")
header+=["function class","associated gene"]
output.write("\t".join(header)+"\n")
for line in input2:
    row=line.strip().split("\t")
    pep=row[0]
    if pep in category:
        fun=category[pep]
        row+=fun
        output.write("\t".join(row)+"\n")
    else:
        output.write(line)

input1.close()
input2.close()
output.close()






