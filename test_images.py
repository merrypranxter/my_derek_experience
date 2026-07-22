import urllib.request

urls = [
    "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_dates_1.PNG",
    "https://storage.googleapis.com/astraltrash_other/derek/duet_count/duet_dates_2.PNG",
    "https://storage.googleapis.com/astraltrash_other/derek/art/art_for_him_1.jpeg",
    "https://storage.googleapis.com/astraltrash_other/derek/art/art_for_him_2.jpg"
]

for url in urls:
    try:
        req = urllib.request.Request(url, method='HEAD')
        response = urllib.request.urlopen(req)
        print(f"{url} - {response.status}")
    except Exception as e:
        print(f"{url} - Error: {e}")
