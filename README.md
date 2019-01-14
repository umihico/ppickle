# ppickle
multilingual human-readable output pickler

## Installation
```
pip install ppickle
```

## How to use
```
>>> data = {'ar': 'عربى', 'en': 'english', 'jp': '日本語', 'ko': '한국어'}
>>> import ppickle
>>> ppickle.dump('data.txt', data)
$ cat data.txt
{'ar': 'عربى', 'en': 'english', 'jp': '日本語', 'ko': '한국어'}
```
Yes, your data keep its look the same on disk regardless of language!  
```
>>> loaded = ppickle.load('data.txt')
>>> loaded['jp']
日本語
>>> loaded == data
True
```

## Other builtin ways
```
>>> import pickle
>>> with open('data.txt', 'wb') as f:
>>>     pickle.dump(data, f)
$ cat data.txt
{"ar": "\u0639\u0631\u0628\u0649", "en": "english", "jp": "\u65e5\u672c\u8a9e", "ko": "\ud55c\uad6d\uc5b4"}
```

```
>>> import json
>>> with open('data.txt', 'w') as f:
>>>     json.dump(data, f)
$ cat data.txt
▒}q(XarqعربىqXenqXenglishqXjpqX 日本語qXkoqX    한국어u.
```
