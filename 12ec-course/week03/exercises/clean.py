#!/usr/bin/env python3

'''
Script to clean up wozwaarde.csv:
- distinguish between 'stadsdelen' (overarching units) en 'wijken' (smaller units)
- separate numerical codes from names of the 'wijk'
'''


import pandas as pd

df = pd.read_csv("wozwaarde.csv", delimiter=';')

df['code'] = df['wijk'].map(lambda x: x.split()[0])
stadsdelen = df[df['code'].map(lambda x: len(x)==1)]
stadsdelen['wijk'] = stadsdelen['wijk'].map(lambda x: x[2:])
stadsdeelcodes = {}
for k, v in stadsdelen[['wijk','code']].to_dict(orient='index').items():
    stadsdeelcodes.update({v['code']: v['wijk']})
    
wijken = df[df['code'].map(lambda x: len(x)>1)]
wijken['wijk'] = wijken['wijk'].map(lambda x: x[4:])
wijken['stadsdeel'] = wijken['code'].map(lambda x: stadsdeelcodes[x[:1]])

wijken.to_csv("wozwaarde-clean.csv", index=False)
