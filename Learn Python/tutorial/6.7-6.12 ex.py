#jabaran 6.7
#6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
##Make two new dictionaries representing different people, and store all three
#dictionaries in a list called people. Loop through your list of people. As you
#loop through the list, print everything you know about each person.

orang_Rizieq ={
    "first":"Muhamammad",
    "last":"Rizaldi",
    "Umur":19
}

orang_Martinelli = {
    "first":"Gabriel",
    "last":"Martinelli",
    "Umur":20,
}

orang_Sumitro = {
    "first":"Emile",
    "last":"Rowe",
    "Umur":20,
}

nama2 = [orang_Rizieq,orang_Martinelli,orang_Sumitro]

for data in nama2:
    print(data)
