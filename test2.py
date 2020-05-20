import yaml
import pymongo

with open('application.yml', 'r') as f:
    conf = yaml.load(f)

username = conf['musername']
password = conf['mpassword']

print(username)
print(password)

client = pymongo.MongoClient('mongodb://%s:%s@ds335648.mlab.com:35648/okky_job?retryWrites=false' % (username, password))

db = client.get_default_database()
jobCollection = db["jobCollection"]

mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = jobCollection.insert_one(mydict)

print(x.inserted_id)


