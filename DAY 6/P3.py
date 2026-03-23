fruit_list1 = ['Apple','Berry','Cherry','Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
fruit_list2[0] = 'Guava' # Guava replaced at both fruit_list1[0] and fruit_list2[0]
fruit_list3[1] = 'Kiwi'

sum = 0
for ls in (fruit_list1,fruit_list2,fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print(sum)