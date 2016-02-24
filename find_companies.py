#!/usr/bin/env python3
import sys
import requests

input_file = sys.argv[1]

with open(input_file) as fin:
    id_list = fin.read().splitlines()

for company_id in id_list:
    get_url = 'https://api.pinpoint.microsoft.com/api/en-us/services(%s)' % (company_id)
    req = requests.get(get_url)
    print(req.content)

with open('all_companies.txt', 'w') as fout:
    for company_id in id_list:
        fout.write(str(req.content))
