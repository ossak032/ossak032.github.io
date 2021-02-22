i = 1
group3 = []
group6 = []
group9 = []
while i<100:
    if i%3==0:
        group3.append(i)
    if i%6==0:
        group6.append(i)
    if i%9==0:
        group9.append(i)
    i=i+1
print(group3)
print(group6)
print(group9)
