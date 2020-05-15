import re

#Regular Expressions allows us to find specific pattern or match of a text


text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa
	
Meta Characters(Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

hoax.com

123-333-5678
123.333.5678
234*444*6789

Mr. Snowden
Mr Davis
Ms Davis
Mrs. Snowden
Mr. S
'''

sentence = "Start a sentence and then bring it to an end"

#We should always use raw string so that the regex will work well
print("\tTab") #Not a raw string
print(r"\tTab") #A raw string


#This is where you wanna put your regex pattern
pattern = re.compile(r'abc') #Searches for abc in the text to search in exact order 'abc' and not 'bca' or 'cba'

#Find the matches for the pattern
matches = pattern.finditer(text_to_search)

#Print the matches
#You can see the location(index) of the word 'abc' inside the span.( 1,4 )
for match in matches:
	print(match)

print(text_to_search[1:4]) #Just showing you

#Thats just simple too find a pattern and print its matches


print()

#When finding symbols like . / ?, we should use escape character or the backslash.
pattern = re.compile(r'\.') #Finds for . in the text
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)
	
print()

#Get the hoax.com
pattern = re.compile(r'hoax\.com')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)

print()

#Match any character except a newline
pattern = re.compile(r'.')
matches = pattern.finditer(text_to_search)
#for match in matches:
#	print(match)

print()

#Match all digits (0-9)
pattern = re.compile(r'\d')
matches = pattern.finditer(text_to_search)
#for match in matches:
#	print(match)

print()

#Match all non-digits (means it prints all except zero to nine (0-9))
pattern = re.compile(r'\D')
matches = pattern.finditer(text_to_search)
#for match in matches:
#	print(match)

print()

#Match all word characters (a-z, A-Z, 0-9, _)
pattern = re.compile(r'\w')
matches = pattern.finditer(text_to_search)
#for match in matches:
#	print(match)

print()

#Match all not word characters
pattern = re.compile(r'\W')
matches = pattern.finditer(text_to_search)
#for match in matches:
#	print(match)

print()

#Match all whitespace (newlines and spaces and tabs)
pattern = re.compile(r'\s')
matches = pattern.finditer(text_to_search)
#for match in matches:
#	print(match)

#Match all non whitespace (all characters except whitespaces)
pattern = re.compile(r'\S')
matches = pattern.finditer(text_to_search)
#for match in matches:
#	print(match)

print()

#Get the Ha after a word boundary (boundaries are whitespaces(spaces, tab, and newline))
#\b are word boundaries then Ha.
pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)

print()

#Get the Ha after a non word boundary
pattern = re.compile(r'\BHa')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)

print()

#Get matches if the text we are finding are at the start. (^ must a prefix)
pattern = re.compile(r'^Start')
matches = pattern.finditer(sentence)
for match in matches:
	print(match) #Gives us Start because it is the first word in the sentence


#Get matches if the text we are finding are at the end ($ sign must be as suffix)
pattern = re.compile(r'end$')
matches = pattern.finditer(sentence)
for match in matches:
	print(match)

print()

#Match any 3digits in a row
pattern = re.compile(r'\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)

#Match the phone numbers above
#\d{3} means 3 digits
#\W means not a word so it gives symbols
pattern = re.compile(r'\d{3}\W\d{3}\W\d{4}')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)

print()

#Parse phone numbers from the PeopleData.txt
with open('peopleData.txt') as file:
	data = file.read()
pattern = re.compile(r'\d{3}\W\d{3}\W\d{4}')
matches = pattern.finditer(data)
#for match in matches:
#	print(match)

print()

#Use a character set to just provide what to match in the text to search
#Just match phone numbers with - and . only
pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)

print()

#Just match phone numbers that are not using - and .
pattern = re.compile(r'\d\d\d[^-.]\d\d\d[^-.]\d{4}')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)

print()

#Get numbers that start with 800 or 900 using character set in the text file
pattern = re.compile(r'[98]00\W\d{3}\W\d{4}')
matches = pattern.finditer(data)
#for match in matches:
#	print(match)

print()

#Get numbers that are in the range of 1-5 using character set []
pattern = re.compile(r'[1-5]')
matches = pattern.finditer(text_to_search)
#for match in matches:
#	print(match)

print()

#Get range of A-Y
pattern = re.compile(r'[A-Y]')
matches = pattern.finditer(text_to_search)
#for match in matches:
#	print(match)

print()

#Get range of 0-8
pattern = re.compile(r'[0-8]')
matches = pattern.finditer(text_to_search)
#for match in matches:
#	print(match)

print()

#Get all characters that are in range of A-Y and a-y and 0-8
pattern = re.compile(r'[a-yA-Y0-8]')
matches = pattern.finditer(text_to_search)
#for match in matches:
#	print(match)

print()

#Get all characters that are not in range of [a-zA-Z0-9] using ^ inside []
pattern = re.compile(r'[^a-zA-Z0-9]')
matches = pattern.finditer(text_to_search)
#for match in matches:
#	print(match)

#Get all words except bat
words = '''
cat
pat
bat
dat
'''
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(words)
for match in matches:
	print(match)

print()

#Get phone numbers using {}
#{3,4} means in the range of 3-4
pattern = re.compile(r'\d{3,4}.\d{3,4}.\d{3,4}')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)

#Get all Mr. (with or without the . after the Mr using ?), we escaped . because we wouldnt want to print all characters
#* means 0 or more and + means 1 or more
#we used 0 to specify that we can just use the \s[A-Z] without the next letter
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)

print()

#Now include all of the Mr, Ms, and Mrs
#() is grouping the text that we can find 
# | is or
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)

print()

#Get all emails
emails = '''
HoaxSnowden@gmail.com
hoax.snowden@university.edu.ph
hoax-17-snowden@some-work.net
hoax.snowden18-204@some.computer-company.com
'''
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9-.]+')
matches = pattern.finditer(emails)
for match in matches:
	print(match)

print()


#Get all website names
urls = '''
https://www.nasa.gov
https://www.facebook.com
https://github.com
http://hoaxsnowden.com
'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
	print(match)

#Prints the group 1 of the match that we made above
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
	print(match.group(1)) #(www\.)


#Get the domain name only of each urls
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#\2 means the group 2 (\w+) and \3 is (\.\w+)
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)


#Remove the other thingys like the object and span=''
pattern = re.compile(r'(Mr|Ms|Mrs)\.? (\w+)')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match.group(0))





