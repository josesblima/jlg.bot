from bs4 import BeautifulSoup
import requests

class Jisho():
    def __init__(self):
        return
    def jisho(self, message):
        print("entrou dentro da funcao jisho\n")
        p_message = message.content.lower()
         #??辞書 Dictionary
        p_message = p_message[2:]
        print('p_message: ' + p_message)
        page_to_scrape = requests.get("https://jisho.org/search/" + p_message)
        
        soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
        
        
        furigana_elements = soup.findAll('span', attrs={'furigana'})
        reading_text = None
        if furigana_elements:
            reading_text = furigana_elements[0].text.strip()
        
        
        word_elements = soup.findAll('div', attrs={'class':'concept_light-representation'})[0].findChildren("span" , recursive=False)
        word_text = None
        if word_elements:
            word_text = word_elements[1].text.strip()
            '''furigana_elements[0].text.strip() + '''
        
        meaning_elements = soup.findAll('span', attrs={'class':'meaning-meaning'})
        meaning1_text = None
        if meaning_elements:
            meaning1_text = meaning_elements[0].text.strip()
            meaning2_text = meaning_elements[1].text.strip()
        return f'({reading_text}){word_text}: {meaning1_text}; {meaning2_text}'
