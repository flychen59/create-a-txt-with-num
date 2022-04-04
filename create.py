seq=0
with open("val.txt","w") as f:
  for i in range(100):

    text=f.write("{:06d}".format(seq)+"\n")
    seq+=1

f.close()
