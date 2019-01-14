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
>>> data = {'ar': 'عربى', 'en': 'english', 'jp': '日本語', 'ko': '한국어'}
>>> import pickle
>>> with open('data.txt', 'wb') as f:
>>>     pickle.dump(data, f)
$ cat data.txt
{"ar": "\u0639\u0631\u0628\u0649", "en": "english", "jp": "\u65e5\u672c\u8a9e", "ko": "\ud55c\uad6d\uc5b4"}
$ python -m pickle data.txt # you need specific command to see origin look
{'ar': 'عربى', 'en': 'english', 'jp': '日本語', 'ko': '한국어'}
```

```
>>> data = [('ar', 'عربى'), ('en', 'english'), ('jp', '日本語'), ('ko', '한국어')]
>>> import json
>>> with open('data.txt', 'w', encoding='utf-8') as f:
>>>     json.dump(data, f, ensure_ascii=False)
$ cat data.txt
[['ar', 'عربى'], ['en', 'english'], ['jp', '日本語'], ['ko', '한국어']]
# pretty close by using ensure_ascii=False option but inside tuples became lists
```
