import urllib.request
page = urllib.request.urlopen("http://www.gutenberg.org/cache/epub/12429/pg12429.txt")
print(page.read(100)) # 100글자만 불러오자

encoded = page.read().decode("utf-8")
print(encoded[:100]) # 100글자만 받아오자 너무 크다
