dico = {'r':3, 'a':0, 'y':5, 'z':1, 't':4, 'e':2}

test = dico.keys()
print(test)
# for key, value in dico.items():
test3 = dico.items()
print(test3)
for val in test3:
  print(val)



test2 = dico.values()
print(test2)


cles_tries = list(dico.keys())
print(cles_tries)
cles_tries.sort()
for k in cles_tries:
  print(k,':',dico[k])
[print(k,':',dico[k]) for k in cles_tries]

values_tries = list(dico.values())
values_tries.sort()
new_list=[]
for val in values_tries:
  for k,v in dico.items():
    if v == val:
      new_list.append((k,v))
      print(v,':',k)
print(new_list)
