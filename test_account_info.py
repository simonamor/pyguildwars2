import pyguildwars2
import json

# Insert your API key that has the 'account' permission into
# the dictionary below
args = {
    'api_key': ''
}

gw = pyguildwars2.pyguildwars2()
# Uncomment the following line to see all requests and responses
# gw.debug = True

acct = gw.api_call('v2/account', **args)

print(json.dumps(acct, sort_keys=True, indent=4))

print("Account name: " + acct.get('name'))

print("Guilds:")
for g in acct.get('guilds'):
    gargs = {
        'guild_id': g
    }
    guild = gw.guild_details(**gargs)
    print("  Name: " + guild.get('guild_name') + " [" + guild.get('tag') + "]")

