import os
intotxt="pdf2txt $1 -o /tmp/my.txt"
print("\033c\033[47;31m\ngive me the file to parse ")
files=input().strip()
files="down.pdf"
print("please wait working file...")
os.system(intotxt.replace("$1",files))
f1=open("/tmp/my.txt","r")
a=f1.read()
f1.close()
f=a.find("Alphabetical list of Armv7-M Thumb instructions")
a=a[f:]
f=a.find("A7.7 Alphabetical list of Armv7-M Thumb instructions")
a=a[f:]
f=a.find("System Level Architecture")
a=a[:f]
aa=a.split("\n")
r=""
l=False
counter=0
for aaa in aa:
    aaa=aaa.strip()    
    if aaa!="":
        if l:
            r=r+"\n"+aaa
            counter=counter+1
    h=aaa.find("Assembler syntax")
    if h>-1:
        counter=0
        l=True
        
    if counter>1:
        l=False
r=r.replace("where:","")
f1=open("out.txt","w")
f1.write(r)
f1.close()