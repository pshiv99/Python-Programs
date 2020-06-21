""" Reading txt file and writing to JSON"""

import json

words = dict()

english_words = dict()

with open(r'C:\Users\Prashant\Desktop\words.txt', 'r') as f:
    i = 1
    for j in f:

        english_words[i] = j.rstrip('\n')
        i += 1

with open(r'C:\Users\Prashant\Desktop\EnglishWords.txt', 'w') as f:
    f.write(json.dumps(english_words, sort_keys=True, indent=0))

""" Experiment with os module """

import os
print(os.getcwd())
print(os.path.abspath('..'))      # Return absolute path of parent directory

print(os.path.abspath('.'))        # Return absolute path of current directory

print(os.path.abspath('C:\\Users\\Prashant'))       # Return same path as passed

final = os.path.basename(os.path.abspath('.'))
print(os.path.basename('C:\\Users\\Prashant'))      # Return Prashant

paths = [os.path.normcase(os.path.abspath('.')), os.path.normcase(r'C:\Users\Prashant')]
print(os.path.commonpath(paths))
print(os.path.commonprefix(paths))

print(os.path.dirname('C:\\Users\\Prashnt\\Desktop'))

print(os.path.exists('C:\\Users'))

print(os.path.lexists('C:\\Users\\'))

print(os.path.getatime('C:\\Borland'))

print(os.path.getsize('C:\\Users\\Prashant'))

print(os.path.isabs('.'))

print(os.path.samefile('.', r'C:\Users\Prashant'))

""" Experiment with re module """



