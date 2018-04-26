import csv
import matplotlib.pyplot as plt
import numpy as np


data = open("DKSalaries2.csv", "r")

print "test"

csvReader = csv.reader(data)

header = csvReader.next()
pos = header.index("Roster Position")
name = header.index("Name")
ave = header.index("AvgPointsPerGame")
cost = header.index("Salary")

wordList = []

pg = open('DKPG.csv','w')
sg = open('DKSG.csv','w')
sf = open('DKSF.csv','w')
pf = open('DKPF.csv','w')
c = open('DKC.csv','w')
g = open('DKG.csv','w')
f = open('DKF.csv','w')
util = open('DKUTIL.csv','w')



#for i in range(len(sort)):#
#    f.write(str(sort[i]))


# Loop through the lines in the file and get each coordinate
for row in csvReader:
    if "PG" in str(row[pos]):
        pg.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
        g.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
        util.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
    if "SG" in str(row[pos]):
        sg.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
        g.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
        util.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
    if "SF" in str(row[pos]):
        sf.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
        f.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
        util.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
    if "PF" in str(row[pos]):
        pf.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
        f.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
        util.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
    if "C" in str(row[pos]):
        c.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))
        util.write('%s,%s,%s\n' % (row[name] , row[ave], row[cost]))

pg.close()
sg.close()
sf.close()
pf.close()
c.close()
g.close()
f.close()
util.close()
#PG
#SG
#SF
#PF
#C
#G
#F
#Util
