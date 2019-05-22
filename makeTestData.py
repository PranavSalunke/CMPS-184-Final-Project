import random    

def createData(country, filename):
    pop = random.randint(100000,1000000)
    with open(filename,"a") as outfile:
        outfile.write("%s,"%(country))
        for year in range(1950,2051):
            pop += random.randint(10000,100000)
            if year == 2050:
                outfile.write("%s"%(str(pop)))
            else:
                outfile.write("%s,"%(str(pop)))
        outfile.write("\n")

filename = "data/testdata.csv"
header = "Country,"
for year in range(1950,2051):
    if year == 2050:
        header += str(year)
    else:
        header += str(year) + ","

with open(filename,"w") as outfile:
    outfile.write("%s\n"%(header))

for i in range(1,51):
    createData("Country"+str(i), filename)