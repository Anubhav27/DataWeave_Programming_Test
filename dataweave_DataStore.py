class DataStore:
    dataStore={}
    l = []
    def __init__(self,num_versions):
        self.num_versions = num_versions
        self.l.append(1);

    def add(self,key,value):
        print "adding key value in a datastore"
        print len(l)

    def get(self,key):
        print "return latest value of key"

    def get(self,key,latest_value):
        print "return latest value of key"

    def delete(self,key):
        print "delete a key"



version=""
with open('datastore_configuration') as f:
    for line in f:
        print line
        version = line

ds = DataStore(version)
ds.add(1,1)
ds.add(1,2)
ds.add(1,3)
