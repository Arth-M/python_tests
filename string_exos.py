alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(0,5):
  print(alphabet[i], ':', i)
print(alphabet.find("r"))
index=alphabet.find("r")

tuple =alphabet.partition("r")
tuple2=alphabet.partition(alphabet[index+5])

print(alphabet[index:index+4])


test="lA FaCE cachéE De marGO"
print(test.capitalize())
print(test.lower())
print(test.title())
print(test.swapcase())
print(test.upper())
