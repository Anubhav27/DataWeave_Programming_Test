"""

This is Question 1 of the assignment

I have created a Key Value Data Store which can perform following operation:

Add(key,value)
Get(key)
delete(key)

Solution:

Here in the solution i tried to create a DataStore class and where the number of versions for a key is taken from "datastore_configuration" file
and based on number of configuration for values of key values are appended to a list and if new value to be added exceeds this version it will be discarded.


"""


class DataStore:
    dataStore={}
    l = []
    def __init__(self,num_versions):
        self.num_versions = num_versions


    def add(self,key,value):
        print "adding key value in a datastore"
        local_list = []
        if key in self.dataStore.keys():
            print "key with %s is there so appending to it" % key
            local_list = self.dataStore.get(key)
            if (len(local_list) < int(self.num_versions)):
                local_list.append(value)
                self.dataStore[key] = local_list
            print self.dataStore
        else:
            print "key %s is not there" % key
            local_list.append(value)
            self.dataStore[key] = local_list
            print self.dataStore


    def get(self,key):
        print "return latest value of %s" % key
        loc_list = self.dataStore[key]
        print loc_list[len(loc_list)-1]

    def delete(self,key):
        del self.dataStore[key]
        print "key %s is deleted" % key





version=""
with open('datastore_configuration') as f:
    for line in f:
        version = line

ds = DataStore(version)
ds.add(1,1)
ds.add(1,2)
ds.add(1,3)
ds.add(1,4)

ds.add(2,1)
ds.add(2,2)
ds.add(2,3)

ds.get(1)

ds.delete(1)


