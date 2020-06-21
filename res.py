import re

regexp = 'A'
string = 'Arashant Shivhare'

#-------------Data Descriptors-------------

res = re.match(regexp, string)
print(res)

# Return the index into the string beyond
# which re engine will not go
print(res.endpos)

# Return the name of the last matched capturing group
print(res.lastgroup)

# re object - Pattern object
print(res.re)

print(res.regs)

# The string used for matching re
print(res.string)

print(res.pos)

print(res.lastindex)

#-------------Functions------------------

regexp = 'aa'
string = 'aaaaaaa'

res = re.search(regexp, string)
res.group()

#----------------------------------

regexp = '(123)+'
string = '12333123'

res = re.findall(regexp, string)
for i in res:
    print(i)

#------------------------------------

import re

regexp = r'/\*(.|\s)+\*/'
string = """Pras/*hant
Shivhar*/e"""

res = re.findall(regexp, string)
res

#--------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import sys

reg = r'(?://.*)|(/\*(.|\s)*\*/)'

string = """Pras/*hant
Shivhar*/e"""                 #   string = r'Pras/*hant\n\tShivhar*/e' 

res = re.finditer(reg, string)

for comments in res:
    print(comments.groups())

#---------------------------------------

import re

reg = r'Prashant\n(?=Shivhare)'
string = 'Prashant\nShivhare'

res = re.search(reg, string)

print(res.group())

#-----------------------------------------

import re
import sys

reg = r'(?://.*)|(?:/\*(.|\s)*?\*/)'

string = """Pras/*hant
    Shivhar*/e"""                 #   string = r'Pras/*hant\n\tShivhar*/e' 

res = re.finditer(reg, string)

for comments in res:
    print(comments.groups())

comments.group()
