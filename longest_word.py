"""
find the longest word in a  string!

"""

# import re
# def LongestWord(sen):
#   regex = re.compile('[^a-zA-Z]')
#   s = sen.split()
#   hash = {}
#   for word in s:
#     if word.isalnum():
#       hash[word] = len(word)
#     else: 
#       word = regex.sub('', word)
#       hash[word] = len(word)
#   max_v = -10000000000000
#   for v in hash.values():
#     max_v = max(max_v, v)
#   for k, v in hash.items():
#     if v == max_v:
#       return k

def LongestWord(sen):
  ans =''
  for char in sen:
    if char.isalnum():
      ans+=char
    else: 
      ans+=' '
  return max(ans.split(), key =len)

# keep this function call here 
def main():
    sen = "I am a very(!) long? 'sentence'...!!!!"
    print(LongestWord(sen))
main()