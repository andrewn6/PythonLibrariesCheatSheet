from urllib.request import urlopen
import json

# JavaScript Object Notation

# This is a valid json object
people_string = '''
{"people":
	[
		{
		"name": "John Smith",
		"phone": "655-555-7164",
		"emails": ["johnsmith@email.com", "john.smith@work.com"],
		"has_license": false
		},
		{
		"name": "Jane Doe",
		"phone": "566-666-8253",
		"emails": null,
		"has_license": true
		}
	]
}
'''

# Loads the a json string
data = json.loads(people_string)
print(data)

print("\n")

# Prints each people individually
for person in data['people']:
    print(person)

print("\n")

# Prints the name of each person
for person in data['people']:
    print(person['name'])

print("\n")

# Removing phone numbers then dump back into a json string
for person in data['people']:
    del person['phone']

######
new_string = json.dumps(data)
print(new_string)
print("\n")

#######
new_string = json.dumps(data, indent=2)  # Adds Indent
print(new_string)
print("\n")

#######
# Sorts the key name alphabetically
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)


###########################################
# Load a json file
# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-JSON/states.json
with open('states.json', 'r') as f:
    data = json.load(f)
# print(data)

print("\n")

# Prints each state
for state in data['states']:
    print(state)

print("\n")

# Prints specific values
for state in data['states']:
    print(state['name'], state['abbreviation'])

# Remove a key then save into a new json
for state in data['states']:
    del state['area_codes']
with open('newstates.json', 'w') as f:
    # json.dump(data, f) #This is messy
    json.dump(data, f, indent=2)  # More cleaner

print("\n")
##########################################
# Getting public api json

with urlopen('https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json') as response:
    source = response.read()

data = json.loads(source)  # We used loads because it is already a string
# print(data)

# Then dump it into a string(cleaner way)
#data = json.dumps(data, indent=2)
# print(data)

# Making a dictionary from the data of the api
pokeindex = dict()  # Makes a empty dict
for item in data:
    id = item['id']
    name = item['name']
    type = item['type']
    pokeindex[id] = [name['english'], type]

# Prints the new json string
print(json.dumps(pokeindex, indent=2))

# Then save it to a new json file
with open("pokemon.json", "w") as f:
    json.dump(pokeindex, f, indent=2)
