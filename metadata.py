class meta(object):
    def __init__(self, tags={}):
        self.tags = {
            "title": '',
            "artists": '',
            "release": '',
            "label": '',
            "genre": '',
            "bpm": ''
        }

    def __eq__(self, other):
        return False

    def __str__(self):
        return "my proper name, maybe filename"

    def parse(self, data):
        # Meta dictionary for temp storage
        temp = {}
        # Get list of keys to parse data for
        tags = self.tags.keys()
        # Begin iterating over data
        for key, value in data.items():
            # Match key to tags
            if key in tags:
                # Secondary check; match for artists list and collaborations
                if type(value) == list:
                    temp[key] = value[0]["name"]
                elif type(value) == dict:
                    # Move value out of dictionary
                    temp[key] = value["name"]
                else:
                    # Default value parse
                    temp[key] = value
        # self.data = temp # replace old data with temp
        return temp

def main():
    print("hello world, testing meta functions...")

    seed = {"genre": "Drum & Bass"}

    data = {
        'slug': 'empire-feat-james-hadoukan-original-mix',
        'duration': {
            'minutes':
                '4: 24',
            'milliseconds': 264462
        },
        'title': 'Empire feat. James Hadoukan (OriginalMix)',
        'guest_pick': False,
        'images': {
            'large': {
                'id': 11077301,
                'width': 500,
                'height': 500,
                'url':
                    'https: //geo-media.beatport.com/image/11077301.jpg'},
            'dynamic': {
                'id': 11077301,
                'url':
                    'https: //geo-media.beatport.com/image_size{hq}/{w}x{h}/11077301.jpg'},
            'small': {
                'id': 8294704,
                'width': 30,
                'height': 30,
                'url':
                    'https: //geo-media.beatport.com/image/8294704.jpg'},
            'medium': {
                'id': 8294705,
                'width': 60,
                'height': 60,
                'url':
                    'https: //geo-media.beatport.com/image/8294705.jpg'}},
        'waveform': {
            'large': {
                'id': 11712837,
                'width': 1500,
                'height': 250,
                'url':
                    'https: //geo-media.beatport.com/image/11712837.png'},
            'dynamic': {
                'id': 11712837,
                'url':
                    'https: //geo-media.beatport.com/image_size{hq}/{w}x{h}/11712837.png'}},
        'type': 'track',
        'remixers': [],
        'purchase': 1,
        'sponsored': False,
        'price': {
            'display': '$1.49',
            'symbol': '$',
            'value': 1.49,
            'code': 'USD'
        },
        'artists': [
            {
                'name': 'Spor',
                'id': 11105,
                'slug': 'spor'
            }
        ],
        'id': 6373145,
        'label': {
            'name': 'Sotto Voce',
            'id': 35740,
            'slug': 'sotto-voce'
        },
        'formats': {
            'aiff': {
                'display': '$0.75',
                'symbol': '$',
                'value': 0.75,
                'code': 'USD'
            },
            'wav': {
                'display': '$0.75',
                'symbol': '$',
                'value': 0.75,
                'code': 'USD'
            }
        },
        'genres': [
            {
                'name': 'Drum & Bass',
                'id': 1,
                'slug': 'drum-and-bass'
            }
        ],
        'date': {
            'published': '2015-02-20',
            'released': '2015-02-20'
        },
        'mix': 'Original Mix',
        'audio_format': 'mp3',
        'key': 'A min',
        'name': 'Empire feat. James Hadoukan',
        'exclusive': False,
        'purchase_type': None,
        'preview': {
            'mp3': {
                'url':
                    'https: //geo-samples.beatport.com/lofi/6373145.LOFI.mp3',
                'offset': {'end': 225784, 'start': 105784}},
            'mp4': {
                'url':
                    'https: //geo-samples.beatport.com/lofi/6373145.LOFI.mp4',
                'offset': {'end': 225784, 'start': 105784}}},
        'bpm': 86,
        'active': True,
        'release': {'name': 'Caligo', 'id': 1477986, 'slug': 'caligo'}}

    metademo = meta(seed)

    r = metademo.parse(data)
    print(r)


if __name__ == '__main__':
    main()
