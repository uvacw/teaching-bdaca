# Working with textual data

This week, we exercise with working with large collections of texts.


## 0. Warm up with regular expressions!
Write a script that

- extracts URLS form a list of strings  
- removes everything that is not a letter or number from a list of
strings


```python
list_w_urls = ["some text with a url http://www.youtube.com... ",
"and another one!! https://www.facebook.com",
"more urls www.baidu.com??",
"And even more?!! %$##($^) https://www.yahoo.com and this one http://www.amazon.com and this one www.wikipedia.org" ]
```



## 1. Get the data
Use the IMDB movie review dataset from https://cssbook.net/d/aclImdb_v1.tar.gz
You can use the code in Example 11.1 in the book to download and access it, which directly reads it into a data strucutre we can use for supervised machine learning later on. But you can also -- as a good exercise maybe -- choose to download the file, unpack it, and write own code to read some texts from it.

## 2. Counting words

Reproduce Example 11.2 and explain the logic behind the code to a classmate.

*Note that this is **not** how sentiment analysis is typically done nowadays, except maybe as a baseline or in very specific edge cases. You can of course use this approach for counting other things (e.g., names of actors) as well. We will discuss recent approaches to sentiment analysis later in the course.*


## 3. Apply the techniques from the lecture

Try the techniques from this week's lecture on the dataset!
