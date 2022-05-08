import pandas as pd
from bin.data import db


def store_data(content):
    bubbledb = db.bubbledb()
    try:
        bubbledb.create_main_table()
    except:
        pass
    data = []
    for key in content:
        data.append(content[key])
    bubbledb = db.bubbledb()
    bubbledb.insert("accounts", data)


def retrieve_data(content):
    from bin.cluster.infer import Cluster
    username = content['username']
    cluster = Cluster()
    cluster.clusters()
    result = cluster.find_similar(username)
    output = result.head()
    return output.to_json()


def dummyvalues(n=4500):
    bubbledb = db.bubbledb()
    bubbledb.create_main_table()
    import random
    data = []
    for i in range(n):
        data1 = [f'dasykfhhh{i}89', f'2g828106{i}@gmail.com']
        data2 = ['Blockchain', 'App_Development', 'Cryptography']
        data = data1 + [random.choice(data2), random.choice(data2), random.choice(data2)]
        bubbledb.insert("accounts", data)

# dummyvalues()
output = retrieve_data({ "username":"jokhn90", "email": "34330@kiit.ac.in", "interest1":"App_Development", "interest2":"Blockchain", "interest3":"Cryptography" })
print(output)