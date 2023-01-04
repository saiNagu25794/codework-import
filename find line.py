#importing module

import pickle

#opening file in writing mode
file = open("dictionary.txt", "wb")

my_dict = {"Name": "John",
           "Age": 21,
           "Id": 28}

#serializing dictionary
pickle.dump(my_dict, file)

#closing the file
file.close()
#reading the data from the file

with open("dictionary.txt", "rb") as handle:
	data = handle.read()

print((type(data)))

# reading the file as dictionary
d = pickle.loads(data)
print(type(d))
print(d)

