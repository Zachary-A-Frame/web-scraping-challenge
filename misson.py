# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from splinter import Browser
from bs4 import BeautifulSoup
import time
import re
import pandas as pd


# %%
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# %%
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# %%
article_title = soup.find("div", class_="list_text").find('a').text
article_body = soup.find("div", class_="article_teaser_body").get_text()

### For debugging purposes.
print(article_title)
print(article_body)


# %%
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# %%
### Find the image url, attach to variable. Make sure you get full size.jpg. Make sure to save correct url string.

image = soup.find('img', class_="thumb")['src']
featured_image_url = 'https://jpl.nasa.gov' + image

print(featured_image_url)


# %%
url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# %%
# For the record, most people in this class have never heard of regular expressions. That having been said, I have. This is way beyond the scope of what we've learned here, this activity needs to be updated. It was much easier before they changed it into what it is today, which is partially due to bundling their scripts via react scripting. There are some students who spend 8+ hours trying to figure this out and learned absolutely nothing during this time, because regex is outside of anything they're familiar with, and this activity clearly hasn't been updated or looked at in quite some time.

# for x in range(1,5):
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     articles = soup.find_all('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")

# soup.find_all("span", string="InSight")

mars_weather = ''
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)
time.sleep(5)
browser.reload()
time.sleep(5)
html = browser.html
time.sleep(5)
soup = BeautifulSoup(html, 'html.parser')
time.sleep(5)
results = soup.find('div', class_= 'css-1dbjc4n').find_all('span', class_ ="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
found = False
for result in results:
    if (bool(result.find(string=re.compile("InSight"))) & (not found)):
        mars_weather = result.find(string=re.compile("InSight"))
        print(mars_weather)
        found = True
print(mars_weather)


# %%
facts_url = "https://space-facts.com/mars/"

facts_tables = pd.read_html(facts_url)
df_mars_facts = facts_tables[1]
df_mars_facts.columns = ['Description', 'Value', 'Index']
df_mars_facts.set_index('Description', inplace=True)


# %%
df_mars_facts.to_html('Resources/mars_facts.html')


# %%
mars_facts = df_mars_facts.to_html(header=True, index=True)
print(mars_facts)


# %%


# Visit the url for USGS Astrogeology.
astrogeo_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(astrogeo_url)

html = browser.html

astrogeo_soup = BeautifulSoup(html, "html.parser")

main_astrogeo_url = "https://astrogeology.usgs.gov"

hems_url = astrogeo_soup.find_all("div", class_="item")

hemis_url = []

for hem in hems_url:
    hem_url = hem.find('a')['href']
    hemis_url.append(hem_url)

browser.quit()


# %%
print(hemis_url)


# %%


