from pymemcache.client import base
from pymemcache import fallback


def perform_query():
    return 13


# set ignore_exc=True to shut down old cache before removing its usage from program
old_cache = base.Client(('localhost', 32000), ignore_exc=True)
new_cache = base.Client(('localhost', 32001))

client = fallback.FallbackClient((new_cache, old_cache))

result = client.get('KEY')

if result is None:
    result = perform_query()
    client.set('KEY', result)


print(result)