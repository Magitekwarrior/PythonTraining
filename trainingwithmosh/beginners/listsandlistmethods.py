names =["John", "Peter", "Gwen", "Mary-Jane", "May"]
print(names[0])

print(names[2])

print(names[-1])

print(names[-2])

# print(names[5])  # Index out of range

names[0] = "Felicia"

print(names[0])

print(names[0:3])

names.append('Norman')

print(names)

print('Number of elements: ', len(names))

names.insert(2, 'Alister')

print(names)

print('Alister' in names)

print('Harry' in names)

print('Number of elements: ', len(names))

names.clear()

print(names)