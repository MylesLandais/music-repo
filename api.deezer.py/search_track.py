import requests


def search(q):

    payload = {
        "q": q
    }
    deezer_search_url = "https://api.deezer.com/search?"
    return requests.get(deezer_search_url, payload).json()

test = search("one more time daft punk")
print(test)

fn = "../.out/" + "2014 - dub"
with open(fn, "r") as f:
    for line in f.readlines():
        print(line)
        resp = search(line)
        print(resp)
        for track in resp['data']:
            print(track)
            break