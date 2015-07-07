# Import urllib and JSON libraries
import urllib.request

try:
    import json
except ImportError:
    import simplejson as json

class pyguildwars2:

    def __init__(self):
        self.headers = {}
        self.debug = False

    def api_call(self, type, **params):

        api_urls = {
            'account': 'v2/account',
            'character': 'v2/character',
            'guild_details': 'v1/guild_details',
            'item_details': 'v1/item_details',
        }

        headers = { }

        if (not type in api_urls):
            raise Exception('APIType','Unknown request type')

        if ('api_key' in params):
            headers['Authorization'] = 'Bearer ' + params.get('api_key')
            del params['api_key']

        url = 'https://api.guildwars2.com/' + api_urls.get(type)

        # v2 URLs often need an API key
        # Both v1 and v2 URLs may accept GET parameters

        if (params):
            if (self.debug):
                print(" Adding params:")
                for p in params:
                    print('  ' + p + ': ' + params.get(p))
            url_args = urllib.parse.urlencode(params)
            url = url + "?" + url_args

        if (self.debug):
            print("Fetching URL: " + url)

        req = urllib.request.Request(url, None, headers)
        with urllib.request.urlopen(req) as response:
            json_data = response.read()
            json_data = json_data.decode(response.headers.get_content_charset())

        if(self.debug):
            print("Response: " + json_data)

        return json.loads(json_data)
