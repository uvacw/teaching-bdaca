#!/usr/bin/env/python

import re

list_w_urls = ["some text with a url http://www.youtube.com... ",
"and another one!! https://www.facebook.com",
"more urls www.baidu.com??",
"And even more?!! %$##($^) https://www.yahoo.com and this one http://www.amazon.com and this one www.wikipedia.org" ]


# option 1: one list
results = []
for e in list_w_urls:
    results.extend(re.findall(r"https?://[\w\.]+\b|www\.[\w\w.]+\b", e))

print(results)

# option2: nested lists
results2 = [re.findall(r"https?://[\w\.]+\b|www\.[\w\w.]+\b", e) for e in list_w_urls]
print(results2)
