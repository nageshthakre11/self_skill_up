import json
with open('Javier_Abshire.json','r') as file:
    data = json.load(file)

print(data.keys())

#print(type(data['entry']))
patient = data['entry'][0]['resource']
#print(patient)


with open('patient.json', 'w') as patient_file:
    json.dump(patient, patient_file, indent=4)

# load patient data to file 


with open('patient.json', 'r') as file:
    data = json.load(file)

if isinstance(data['address'],dict):
    for item in data['address']:
        print(item)
else:
    print('not a list')