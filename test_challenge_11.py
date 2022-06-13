# Write a function to reverse the order of words that have punctuation and keep the punctuation in place

# sample input: the quick brown fox, jumped over, the mouse.
# sample output: mouse the, over jumped, fox brown quick the.

original = 'the quick brown fox, jumped over, the mouse.'
o = []
for w in original.split(' '):
  comma = ','
  period = '.'
  if comma in w:
    w = comma + w[:-1]
  elif period in w:
    w = w[:-1]

  o.append(w)
o = reversed(o)
reversed_o = ' '.join(o) + '.'
print(reversed_o)
