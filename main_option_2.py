from sys import stdin
input_string = ''
# input_string = input()

for text in stdin:
#  text = 'Twas brillig, and the slithy toves\nDid gyre and gimble in the wabe;\nAll mimsy were the borogoves,\nAnd the mome raths outgrabe.'
  input_string += text
  
char_dict = {}
gist_count = []

string = "".join(input_string.rstrip().split())
gist_count = [char for char in string]

for i in range(len(gist_count)):
  check = char_dict.get(gist_count[i], 0)
  if (check == 0):
    char_dict.update({string[i]: 1})
  else:
    char_dict.update({string[i]: check + 1})

sorted_char_dict = dict(sorted(char_dict.items(), key=lambda x: x[0]))


count_to_print = list(sorted_char_dict.values())

for i in reversed(range(1,max(count_to_print, default=1)+1)):
  for j in range(len(count_to_print)):
    if (count_to_print[j] >= i): 
      print('#',end = '')
    else:
      print(' ', end = '')
  print()
for key, value in sorted_char_dict.items() :
    print(key, end = '')