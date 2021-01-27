input = int(input(),16)
for i in range(1,16):
    print("%X"%input+"*"+"%X"%i+"="+"%X"%(input*i))