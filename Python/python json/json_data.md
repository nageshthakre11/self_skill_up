Q. What is JSON, and why is it used?
- light weighted, easy to store and exchange
- human readable
- used for API and configuration


Q. How to read JSON file format?
with open('file_name', 'r') as file:
    data = json.load(file)

json.dumps(obj)             Converts a Python object into a JSON string.
json.dump(obj, file)        to write a Python dictionary to a JSON file.
json.load(file)	            Reads JSON data from a file and converts it into a Python object.
json.loads(string)	        Parses JSON data from a string and converts it into a Python object.


