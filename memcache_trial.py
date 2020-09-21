from pymemcache.client import base

# Run memcached before this line
client = base.Client(('localhost', 11211))

# Access the cache
client.set('C1000', 'Orange Water')

# Retrieve
print(client.get('C1000'))

