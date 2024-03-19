import requests
from bs4 import BeautifulSoup

# URL of the Twitter profile
profile_url = 'https://twitter.com/warrior_0719'
test_url = 'https://www.fotmob.com/matches/cr-belouizdad-vs-nc-magra/8u6qbmml#4366445'

response = requests.get(test_url)

if response.status_code == 200:
    # Parse the HTML content of the profile page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Search for the term "CR Belouizdad" and count its occurrences
    term = "CR Belouizdad"
    term_count = soup.text.count(term)

    # # Extract specific information from the profile
    # profile_name = soup.find('div', {'class': 'css-1dbjc4n r-1habvwh'}).text.strip()
    # profile_handle = soup.find('div', {'class': 'css-1dbjc4n r-18u37iz r-1wtj0ep r-156q2ks'}).text.strip()
    # profile_bio = soup.find('div', {'class': 'css-1dbjc4n r-18u37iz r-1h3ijdo r-1wtj0ep'}).text.strip()
    # profile_location = soup.find('div', {'class': 'css-1dbjc4n r-18u37iz r-1h3ijdo r-1wtj0ep'}).text.strip()

    # Print the extracted information
    # print("Profile Name:", profile_name)
    # print("Twitter Handle:", profile_handle)
    # print("Bio:", profile_bio)
    # print("Location:", profile_location)
    print(soup.prettify())
    print("The term '{}' appears {} times on the webpage.".format(term, term_count))
# else:
#     print("Failed to fetch data from the URL:", url)
else:
    print("Failed to fetch data from the profile:", profile_url)



# OutPut is
# The term 'CR Belouizdad' appears 13 times on the webpage.