import json

path = r"C:\Users\nthakre\Desktop\POC\fhir\json_project\Javier_Abshire.json"


# LOAD :- json.load FUNDTION IS USED TO LOAD DATA AS PYTHON OBJECT  
with open(path, 'r') as file:
    json_data = json.load(file)

    



print(type(json_data),'json_data')
#print(json_data)

# json.dumps(file, indent = 4) :- this function converts python object to json string data
json_string_data = json.dumps(json_data, indent = 4)
print(type(json_string_data), 'json_string_data')
#print(json_string_data)



data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open('data.json','w') as file:
    json_sample_dump = json.dump(data, file)
print(type(json_sample_dump),'json_sample_dump')

 

