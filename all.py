import os
# a = os.listdir()
a = os.listdir()
print(a)
for c in a: 
    if ".txt" in c:
        with open("all","a") as wri:
            wri.write(f"hashcat -m 22000 -w 4 -d 1  test.22000 {c} \n")
