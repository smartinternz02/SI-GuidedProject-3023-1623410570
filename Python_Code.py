from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result
from cloudant.result import Result, ResultByKey


# IBM Cloudant Legacy authentication
client = Cloudant("apikey-v2-otb7qtvzldequqh11vvtr91djtqoi7id47ktg715615", "9a9efd7bcb572582d757ed00cbccd664",
                  url="https://apikey-v2-otb7qtvzldequqh11vvtr91djtqoi7id47ktg715615:9a9efd7bcb572582d757ed00cbccd664@0243d9ae-7814-4ddf-96be-40c9e34899f8-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()

database_name = "imageurl"

my_database = client.create_database(database_name)

if my_database.exists():
    print(f"'{database_name}' successfully created.")
    json_document = {
                    "_id": "001",
                    "name":"jyoti"
                    }
    new_document = my_database.create_document(json_document)
    if new_document.exists():
        print("Document '{new_document}' successfully created.")

result_collection = Result(my_database.all_docs, include_docs=True)
# Get the result for matching a key
result = result_collection['001']  #search by id, if id=1001   

print("---------------")
print("the data with id =001 is")
print (result)
print("---------------")
# Iterate over the result collection
for result in result_collection:
    print(result)# it will print all the records

# First retrieve the document
for document in my_database:
    my_document = my_database['001'] 

# Update the document content
# This can be done as you would any other dictionary
my_document['Temperature'] = 23
my_document['Humidity'] = 45
my_document['Vibration'] = 30
my_document['Current'] = 30
my_document['Voltage'] = 40

# You must save the document in order to update it on the database
my_document.save()

result_collection = Result(my_database.all_docs, include_docs=True)
# Get the result for matching a key
result = result_collection['001']     
# Iterate over the result collection
print (result)


