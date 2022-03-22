import re

# Raw string is prfixed with r. example r'\tTab'

text_to_search = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
123465798825

Ha Haha

Meta Characters (need to be escaped)
.[{(\/$!?*+

example.com

312-369-4595
123.365.3654

Mr. kX
Mrs. Jklm

cat
mat
bat
pat

RishiVaishnav@gmail.com
rishi.vaisnav@email.net
rishi-321-vaishnav@my-work.edu
"""

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
print(text_to_search[141:153])
