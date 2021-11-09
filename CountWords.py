introstring=input("enter ur introduction :")
print(introstring)
ccount=0
wcount=1
for i in introstring:
    ccount=ccount+1
    if(i==" "):
        wcount=wcount+1
print("total characters",ccount)
print("total words", wcount)