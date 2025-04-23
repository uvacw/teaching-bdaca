import re

list_w_urls = [
    "some text with a url http://www.youtube.com... ",
    "and another one!! https://www.facebook.com",
    "more urls www.baidu.com??",
    "And even more?!! %$##($^) https://www.yahoo.com and this one http://www.amazon.com and this one www.wikipedia.org"
]

all_urls = []

cleaned_texts = []

for line in list_w_urls:
    # (https?:\/\/)?   => matches 'http://' or 'https://'
    # (www\.)?         => matches 'www.'
    # [a-zA-Z0-9\-\.]+ => matches domain (letters, numbers, hyphens, and dots)
    # \.[a-zA-Z]{2,}   => matches top-level domain like '.com', '.org', {2,} is a quantifier that means: Match at least 2 of the preceding character class.
    found_urls = re.findall(r'(https?:\/\/)?(www\.)?[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}', line)

    for url_parts in found_urls:
        url = ''.join(url_parts)
        all_urls.append(url)

    # Remove all non-alphanumeric characters: [^a-zA-Z0-9] matches anything that is NOT a letter or number
    cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line)
    cleaned_texts.append(cleaned_line)
    
print("Extracted URLs:")
for url in all_urls:
    print(url)

print("\nCleaned Texts:")
for text in cleaned_texts:
    print(text)
