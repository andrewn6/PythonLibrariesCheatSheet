import requests

# Get a response from a page
r = requests.get('https://xkcd.com/353')
print(r)

print("\n")

# Show attributes and methods that we can access from the page
# print(dir(r))


# Get content of a page in text(unicode)
print(r.text)  # In text(unicode)

print("\n")

# Get content of a image in a page in bytes
r = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(r.content) #In bytes

# Save the image in a file
with open('comics.png', 'wb') as file:
    file.write(r.content)


# Check Status code
'''
Status Codes:
	200 - Success
	300 - Redirect
	400 - Client Errors(No permission to access)
	500 - Server Errors
'''
print(r.status_code)

# Or to make it shorter
print(r.ok)

print("\n")

# View in-depth response information
print(r.headers, "\n")
r = requests.get('https://xkcd.com/353')
print(r.headers)

print("\n")

# Use dictionary as parameters in urls(GET Parameters)
payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)  # Get the response
print(r.url)  # Get the url with the params

print("\n")

# Post request using dictionary
payload = {'username': 'Hoax', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)

print("\n")

# Create python dictionary from the response using json() then access its data
r_dict = r.json()
print(r_dict, "\n")
print(r_dict['form'])  # Get username and pass that we post using post request

# Logging in credentials using with basic_auth using get
# The tuple in 'auth' must be the same with the ones that are in the url
r = requests.get(
    'https://httpbin.org/basic-auth/hoax/testing',
    auth=(
        'hoax',
        'testing'))
print(r.text, "\n")


# Set a timeout response
r = requests.get('https://httpbin.org/delay/1', timeout=3)
print(r)

# If we passed a delay(7) > timeout(3), it will give as a error
r = requests.get('https://httpbin.org/delay/7', timeout=3)
print(r)
