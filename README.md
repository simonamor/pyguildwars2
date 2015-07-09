# pyguildwars2

Python class for accessing the Guild Wars 2 API

To get an API key, visit https://account.guildwars2.com/account/api-keys
and login with your Guild Wars 2 account. Once logged in, click the
'New key' link and fill in the form with a user friendly name and check
the permission boxes depending on which functions you want access to.

Create a pyguildwars2 object
----------------------------

    gw2 = pyguildwars2.pyguildwars2()
    args = {
        'api_key': '123ABC',
    }

The API key should be inserted into the dictionary _args_ in place
of '123ABC'

Call pre-defined methods on the object
--------------------------------------

    account = gw2.account( **args )
    print( account.get( 'name' ) )

**or**

Use the api_call() method directly
----------------------------------

This is useful for new API features that haven't been added to the module.

For example, the following (upon substition of a valid API key) will return
a list of dictionaries, each one declaring one slot within the bank.

    bank = gw2.api_call( 'v2/account/bank', **args )
    print( bank )

    [{'count':1, 'id':41291}, {'count':250, 'id':46735}]


