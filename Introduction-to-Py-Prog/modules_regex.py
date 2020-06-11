import re
string = "'I AM NOT YELLING', she said. Though we knew it not to be true."

# substitute object (pattern to match, what to replace with, string on which it is used)
new = re.sub('[A-Z]', '', string)
print(new)


new1 = re.sub('[a-z]', '', string)
print(new1)


new2 = re.sub('[.,\']', '', string)
print(new2)

new3 = re.sub('[.,\'A-Z]', '', string)
print(new3)


new4 = re.sub('[.,\'A-Z+" "]', '', string)
print(new4)


string = string + "6 298-345"
print(string)

new5 = re.sub('[^0-9]','',string)
print(new5)