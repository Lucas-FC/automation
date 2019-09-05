import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--verbose')

#Permet d'excuter le navigateur pour visiter le lien choisi

browser = webdriver.Chrome("D:/webdrivers/chromedriver.exe")
browser.get("https://www.bing.com/news")

#Localiser la barre de recherche sur le site web et entrer la recherche souhaité

search = browser.find_element_by_name("q")
print(search)
print([search.text, search.tag_name, search.id])
print("Entrez votre recherche")
txt = input()
search.send_keys(txt)

#Ordonner le clic pour lancer la recherche

#search_button = browser.find_element_by_name('go')
#search_button.click()
search.send_keys(Keys.RETURN)

#png = browser.save_screenshot("screen.png") --- Fonctionnalité optionnel pour prendre un screen de la page de recherche

#Permet d'extraire les liens des articles de la page et d'organiser ces derniers en liste

links = browser.find_elements_by_xpath("//div[@class='news-card newsitem cardcommon'][@url]")
results = []
for link in links:
    try:
        url = link.get_attribute('url')
    except StaleElementReferenceException as e:
        print("Issue with '{0}' and '{1}'".format(url, link))
        print("It might be due to slow javascript which produces the HTML page.")
    results.append(url)
print(results)

browser.quit()

#Enregistre un fichier avec les liens des articles.

txt_result = open('result.txt', 'w')
txt_result.write(str(results))