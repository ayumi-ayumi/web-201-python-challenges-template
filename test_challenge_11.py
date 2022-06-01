# Write a function to reverse the order of words that have punctuation and keep the punctuation in place

# sample input: the quick brown fox, jumped over, the mouse.
# sample output: mouse the, over jumped, fox brown quick the.





original = 'the quick brown fox, jumped over, the mouse.'
original_list = original.split('.')
original_list_2 = original_list.split(' ')

print(original_list_2)

# new = first.split(',')
# for i in new[0]:
#   reversed_i = i[::-1]
#   print(reversed_i)
# print(new)