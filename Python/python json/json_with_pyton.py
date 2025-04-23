import json

'''
Here json file is present in given path and to read it,
json.load(file) function is used.
result is in python object.
'''
path = r"C:\Users\nthakre\Desktop\POC\fhir\json_project\Javier_Abshire.json"
with open(path, 'r') as file:
    json_from_file = json.load(file)
print('json_from_file', type(json_from_file))


# as json.loads function work with string so first read file_1 as string
with open(path,'r') as file_1:
    json_file_str = file_1.read()
    json_loads = json.loads(json_file_str)
print('json_loads-------->',type(json_loads))


print('-----------------------------------------------------------------------------------')

'''
data attribute has data in json string, and to parse that data we can use the 
json.loads(data) function.
result is in python object 
'''

data = '''{
    "name": "John",
    "age": 30,
    "city": "New York"
}'''

json_from_data = json.loads(data)
print(json_from_data)
print('json_from_data ****',type(json_from_data))

print('-----------------------------------------------------------------------------------')

# convert python object to json string 
# json.dumps()
json_string = json.dumps(json_loads, indent= 4)
print(type(json_string))

print('-----------------------------------------------------------------------------------')

with open('new_file.json', 'w') as file:
    json.dump(data, file)


with open('new_file.json', 'r') as file:
    file_2 = file.read()
    load_from_file = json.loads(file_2)
print('load_from_file',type(load_from_file))  # output is str as file has data in string
print(load_from_file)

ned_data = json.loads(load_from_file)
print(type(ned_data))

data_2= data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open('json_data_load.json', 'w') as file:
    json.dump(data_2, file, indent=4)

print('-----------------------------------------------------------------------------------')


import ijson

with open("Javier_Abshire.json", "r") as file:
    objects = ijson.items(file, "item")  # Read JSON objects lazily
    print(type(objects))
    print(i for i in objects)
