import urllib.request
from urllib.error import URLError
from datetime import datetime



url = "https://example.com"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


try:
    start_at = datetime.now()

    for x in range(0, 400):
        req = urllib.request.Request(url, headers=hdr)
        response = urllib.request.urlopen(req)
        response.read()

        print("Link Click Counter", x)

    print("Start At =",start_at, " -- End At =", datetime.now())
            
except URLError as e:
    print(e, '<-- Internet Error..')
except Exception as e:
    print(e, '<-- Exception Error..')
