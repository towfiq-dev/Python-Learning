import re

text = "1 My name is Towfiqul Islam"
pattern = r"^1"

# re.search() ম্যাচ পেলে Match অবজেক্ট দেয়, না পেলে None দেয়
if re.search(pattern, text):
    print('good')
else:
    print('bad')