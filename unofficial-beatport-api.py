import requests
import json
from urllib.parse import urlencode
from bs4 import BeautifulSoup


class beatport(object):

    def __init__(self):
        pass

    def query(self, artist, title):
        '''
        Search for artist+title+track
        :return:
        Html response from server
        '''
        search = "https://pro.beatport.com/search?"
        value = urlencode({"q":str(artist + " " + title)}, safe='', encoding=None, errors=None)
        return requests.get(search+value).text

    def jsonify(self,html):
        '''
        Beatport returns a script id 'data-objects' containing json of track metadata
        :return:
        Only json string
        '''
        begin = "window.Playables ="
        end = "};"
        soup = BeautifulSoup(test,"html.parser")
        tag = soup.find("script",attrs={"id":"data-objects"})
        return tag.string[(tag.string.find(begin)+len(begin)):(tag.string.find(end)+1)]

api = beatport()

test = api.query("kursa","Just a Glitch")
#test = api.query("spor", "empire")

raw = api.jsonify(test)
demo = json.loads(raw)

dict = demo['tracks'][-1]

print(dict['title'])
print(dict['duration'])
print(dict['bpm'])
print(dict['artists'][0]['name'])
print(dict['label']['name'] )