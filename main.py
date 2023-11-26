import requests
import pandas as pd
import random

url = 'https://api.koios.rest/api/v0/pool_delegators?_pool_bech32=pool19f6guwy97mmnxg9dz65rxyj8hq07qxud886hamyu4fgfz7dj9gl'

response = requests.get(url)

storage = response.json()


e = random.randrange(1,1000)

print(type(storage))

print(storage[e]['stake_address'])
print(storage[e]['amount'])
print(storage[e]['active_epoch_no'])
print(storage[e]['latest_delegation_tx_hash'])


a = storage[e]['stake_address']
b = storage[e]['amount']
c = storage[e]['active_epoch_no']
d = storage[e]['latest_delegation_tx_hash']

list1 = [a]
list2 = [b]
list3 = [c]
list4 = [d]

col1 = "Stake Address"
col2 = "Amount"
col3 = "Active Epoch No"
col4 = "Latest Delegation Tx Hash"

data = pd.DataFrame({col1: list1, col2: list2, col3: list3, col4: list4})
data.to_excel("snapshot.xlsx", sheet_name="data", index=False)