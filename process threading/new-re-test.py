import re


d1 = ["love", "13", "lin"]
d2 = ["i", "eilinge", "14"]

c1 = " ".join(d1)


e1 = re.findall(r"(\d.?)", c1)
d1_remove = []
for i in e1:
    if i in d1:
        d1.remove(i)
        d1_remove.append(i)

print("d1_keep", d1)
print("d1_remove", d1_remove)

c2 = " ".join(d2)

e2 = re.findall(r"(\d.?)", c2)

d2_remove = []
for j in e2:
    if j in d2:
        d2.remove(j)
        d2_remove.append(j)

print("d2_keep", d2)
print("d2_remove", d2_remove)
for jj in d2:
    print(jj)
