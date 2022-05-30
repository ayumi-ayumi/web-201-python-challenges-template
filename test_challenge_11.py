# Write a function to reverse the order of words that have punctuation and keep the punctuation in place

# sample input: the quick brown fox, jumped over, the mouse.
# sample output: mouse the, over jumped, fox brown quick the.





first = 'the quick brown fox, jumped over, the mouse.'
new = first.split(',')
for i in new[0]:
  reversed_i = i[::-1]
  print(reversed_i)
print(new)