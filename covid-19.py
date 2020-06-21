# importing libraries

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import numpy as np
import matplotlib.pyplot as plt


extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
URL = 'https://www.mohfw.gov.in/'

SHORT_HEADERS = ['SNo', 'State','Indian-Confirmed(Including Foreign Confirmed)','Cured','Death']

response = requests.get(URL).content
soup = BeautifulSoup(response, 'html.parser')
header = extract_contents(soup.tr.find_all('th'))

stats = []
all_rows = soup.find_all('tr')

for row in all_rows:
	stat = extract_contents(row.find_all('td'))

	if stat:
		if len(stat) == 4:
			# last row
			stat = ['', *stat]
			stats.append(stat)
		elif len(stat) == 5:
			stats.append(stat)

stats[-1][0] = len(stats)
stats[-1][1] = "Total Cases"

table = tabulate(stats, headers=SHORT_HEADERS)
print(table)


