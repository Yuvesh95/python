def new(x,s):
    f=open("output2.txt","a")

    f.write(x[:-1]+","+str(s-1))
    f.write("\n")
    f.close()
f = open("ICP2.txt", "r")
for x in f:
  s=len(x)
  new(x,s)
  print(x[:-1]+","+str(s-1))
