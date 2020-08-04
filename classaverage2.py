a = int(input("how many students in the whole class?"))
list_score = []
name = []
for i in range(a):
    name_input = input ("your name:") 
    score = int(input("insert score here: "))
    list_score.append(score)
    name.append(name_input)
highest = 0
for n in range(a):
    if list_score[n] > highest:
        highest = list_score[n]
        highname = name[n]
print("highest score:" ,highest, highname)
lowest = 100
for n in range(a):
    if list_score[n] < lowest:
        lowest = list_score[n]
        lowname = name[n]
print("lowest score:" ,lowest, lowname)
sum_score = sum(list_score)
print("class score average: ",sum_score/a)