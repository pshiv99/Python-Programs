import json
jokes = dict()
with open(r'C:\Users\Prashant\Documents\Codes\Flask\webhooktest\onelinefun.csv', 'r') as f:
    f.readline()
    for line in f:
        split_list = (line.split(',', maxsplit = 1))
        temp = split_list[1].lstrip('"').rstrip('"\n')
        jokes[int(split_list[0])] = temp

jokes_string = json.dumps(jokes, sort_keys=True, indent=4)

with open(r'C:\Users\Prashant\Desktop\jokes.json', 'w') as f:
    f.write(jokes_string)

