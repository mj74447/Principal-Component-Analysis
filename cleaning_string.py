import re
states = ['Delhi','mumb@aI','MADHYA PRADESH','kERE!LA']
def clean_strings(strings):
  result = []
  for value in strings:
    value = value.strip()
    value = re.sub('[@!#?]','',value)
    value = value.title()#used for changing state of string starting from Uppercase first alph rest lowercase
    result.append(value)
    
  return result
clean_strings(states)
