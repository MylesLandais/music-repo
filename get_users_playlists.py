# request page with /users/sets
import requests
import json

# some header shit
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}

# request /users/sets
base_url = "https://api-v2.soundcloud.com"
path = "users/"


def playlist_without_albums_params(client_id=None, app_version=None, limit=None, app_locale=None, offset=None):
    """/
        (future implementation)
        Dictionary of parameters for api request
    :param client_id:
    :param app_version:
    :param limit:
    :param app_locale:
    :param offset:
    :return: dictionary for url_param
    """
    ## TODO Future implementation of parameterization
    return {
        client_id: "",
        app_version: "",
        limit: "",
        offset: "",
        app_locale: "en",
    }


def playlists_without_albums(user_id, limit_param="limit=99"):
    test_str = ""
    # build get parameters
    # offset = 10 original, omitting is good for us
    # offset = None
    # need to hack on client_id more / this may be a secret,,,
    # maybe try NaN or None?
    client_id = ""
    # app_version is probably tracked by sc internal teams
    app_version = ""
    # app_locale is not interesting.. just en // may want to test against "es"
    app_locale = "app_locale=en"
    url_cat = base_url + "/" \
              + path + user_id \
              + "/" + "playlists_without_albums" + "?" \
              + limit_param + "&" \
              + client_id + "&" \
              + app_version + "&" \
              + app_locale
    if url_cat == test_str:
        print("w")
        return requests.get(url_cat, headers=headers).json()
    else:
        print(url_cat)
        print(test_str)


if __name__ == "__main__":
    resp = playlists_without_albums("")
    for i in resp['collection']:
        print(i['title'])
