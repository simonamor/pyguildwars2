# Import urllib and JSON libraries
import urllib.request

try:
    import json
except ImportError:
    import simplejson as json

"""
.. module:: pyguildwars2
    :synopsis: Module to provide access to the Guild Wars 2 API using Python
"""

class pyguildwars2:

    """
    debug

        This attribute can be set to True or False. It defaults to False
        and can be set directly using object.debug = True
    """

    def __init__(self, **config):
        self.headers = {}
        self.debug = False


    """
    .. function:: api_call(type, **params)

        Low level function to access the API, usually called by the other
        methods but can be called directly if there are new API functions
        not yet added to this module.
    """

    def api_call(self, type, **params):

        headers = { }

        if ('api_key' in params):
            headers['Authorization'] = 'Bearer ' + params.get('api_key')
            del params['api_key']

        url = 'https://api.guildwars2.com/' + type

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

        if (self.debug):
            print("Response: " + json_data)

        return json.loads(json_data)

    """
    .. function:: account(**params)

        One of the keys must be 'api-key' with a valid Guild Wars 2 API
        key as the value.
    """

    def account(self, **params):
        return self.api_call('v2/account', **params)

    """
    .. function:: guild_details(**params)

        One of the keys must be 'api-key' with a valid Guild Wars 2 API
        key as the value.
        You must also provide 'guild_id' being the GUID of the guild or
        'guild_name' being the name of the guild.
    """

    def guild_details(self, **params):
        return self.api_call('v1/guild_details', **params)


