from pymemcache.client import base

def perform_query():
    # Code to query DB or remote REST API
    return 42


client = base.Client(('localhost', 11211))
result = client.get('C2000')

if result is None:
    # This means the cache is empty, so we need to get the value from src
    result = perform_query()

    # Then cache the result for next time
    client.set('C2000', result)


print(result)