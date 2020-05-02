from bs4 import BeautifulSoup
import requests
import csv


# Install lxml 'pip install lxml'

# Making a soup object from a html file and print it
with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
print(soup)

print("\n")

# Makes the soup more easier to read(adds indentation)
print(soup.prettify(), "\n")

# Get specific html tag
match = soup.title  # Gets title, you can do .h1, p, etc..
print(match)
print(match.text, "\n")  # Removes the tag <title>

# Get a div block
match = soup.div
print(match, "\n")  # Only returns the first div block

# Get a div block by its class (footer)
match = soup.find('div', class_='footer')
print(match, "\n")  # Returns div with footer class

# Get the div block with the article class
article = soup.find('div', class_='article')
print(article, "\n")

# Get headline2 child tag of the first article that we got (We access it
# from the soup object that we made, 'article')
headline = article.h2.a
print(headline.text, "\n")

# Get paragraph child tag of the article
summary = article.p
print(summary.text, "\n")

# .find() only returns the first occurence of the tag that you specified while .file_all() returns all occurence of the tag you specified
# This returns a list so we can also iterate through each item
articles = soup.find_all('div', class_='article')
print(articles, "\n")

# Iterate through all of the articles
for article in articles:
    print(article)

print("\n")

# Iterate through each headlines and summary of all the articles
for article in articles:
    headline = article.h2.a
    print(headline.text)

    summary = article.p
    print(summary.text)

    print()

#######USING BS4 IN REAL WEBSITE########
# Our goal is to print the title, description and the link from the website


# Use request to get the html from a website
source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())

print("\n")

# Use inspect element to get the tag what you needed, we want to get the
# article, the first article to be exact
article = soup.find('article')
print(article.prettify())

# From this, we can like get more specific tags we need, we need headline
headline = article.h2.a
print(headline.text)

# Then the description of that title
desc = article.find('div', class_="entry-content").p
print(desc.text)
print()

# Then the youtube link, our link as you can see in the source code is in
# the src attribute in the iframe tag, we just need to get that id
vid_link = article.find('iframe', class_='youtube-player')
# print(vid_link)

# Then, after we got the iframe tag, we can just call that src attribute
# like a dictionary in python
print(vid_link['src'])
print()

# The link that we got is not the real youtube link, but it is a embed. We
# are gonna get the id from that link, so we gonna split it by forward
# slash
vid_id = vid_link['src'].split('/')
print(vid_id)
print()

# Then print the 5th index because it is where the yt id can be found
print(vid_id[4])
print()

# So we can found the id before the ? so we gonna split it again
vid_id = vid_id[4].split('?')
print(vid_id[0])  # Then select the first index because it contains the id

print()

# Then we can finally make the youtube link
yt_link = f"https://youtube.com/watch?v={vid_id[0]}"
print(yt_link)

print()

# So this is basically our final result
article = soup.find('article')
headline = article.h2.a
desc = article.find('div', class_="entry-content").p

print(headline.text)
print(desc.text)
print(yt_link)

print()

# Then finally we can print all of the articles using find_all and for loop

for article in soup.find_all('article'):
    headline = article.h2.a
    print(headline.text)

    desc = article.find('div', class_="entry-content").p
    print(desc.text)

    try:
        vid_link = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_link.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except BaseException:
        yt_link = None
    print(yt_link)

    print()


# What if we had a article that doesnt have a youtube link/vid, so it will
# give us an TypeError, just like above. I made a try and except block in
# that link where if it doesnt return a link, it gives us None


# Then we can put this in a file
csv_file = open('scraped_data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'description', 'yt_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    # print(headline.text)

    desc = article.find('div', class_="entry-content").p.text
    # print(desc.text)

    try:
        vid_link = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_link.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except BaseException:
        yt_link = None
    # print(yt_link)

    # print()
    csv_writer.writerow([headline, desc, yt_link])

csv_file.close()
