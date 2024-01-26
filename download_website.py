
#clés : vgWtOGgg3WsMx0yaYgOk1YUDH1PSnBgVM53RrEPztceYf3xujoQ5koaBzz2gjRU

import os
import requests
import time
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

wax = """
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  WWWWWWWWwwwwwwwwwwwwwwwwwwwwwwwwwwwWWWWWWWWwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwTTTTTTTTTTTTTTTTTTTTTTTwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwlllllllwwwwwwwwwwwwwwwwww
#  W::::::WwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::WwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwT:::::::::::::::::::::Twwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwl:::::lwwwwwwwwwwwwwwwwww
#  W::::::WwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::WwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwT:::::::::::::::::::::Twwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwl:::::lwwwwwwwwwwwwwwwwww
#  W::::::WwwwwwwwwwwwwwwwwwwwwwwwwwwwW::::::WwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwT:::::TT:::::::TT:::::Twwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwl:::::lwwwwwwwwwwwwwwwwww
#  wW:::::WwwwwwwwwwwwWWWWWwwwwwwwwwwwW:::::WaaaaaaaaaaaaawwwxxxxxxxwwwwwwxxxxxxxwwwwwTTTTTTwwT:::::TwwTTTTTTooooooooooowwwwwwooooooooooowwwwl::::lwwwwwsssssssssswww
#  wwW:::::WwwwwwwwwwW:::::WwwwwwwwwwW:::::Wwa::::::::::::awwwx:::::xwwwwx:::::xwwwwwwwwwwwwwwT:::::Twwwwwwoo:::::::::::oowwoo:::::::::::oowwl::::lwwwss::::::::::sww
#  wwwW:::::WwwwwwwwW:::::::WwwwwwwwW:::::Wwwaaaaaaaaa:::::awwwx:::::xwwx:::::xwwwwwwwwwwwwwwwT:::::Twwwwwo:::::::::::::::oo:::::::::::::::owl::::lwss:::::::::::::sw
#  wwwwW:::::WwwwwwW:::::::::WwwwwwW:::::Wwwwwwwwwwwwwa::::awwwwx:::::xx:::::xwwwwwwwwwwwwwwwwT:::::Twwwwwo:::::ooooo:::::oo:::::ooooo:::::owl::::lws::::::ssss:::::s
#  wwwwwW:::::WwwwW:::::W:::::WwwwW:::::Wwwwwwwaaaaaaa:::::awwwwwx::::::::::xwwwwwwwwwwwwwwwwwT:::::Twwwwwo::::owwwwwo::::oo::::owwwwwo::::owl::::lwws:::::swwssssssw
#  wwwwwwW:::::WwW:::::WwW:::::WwW:::::Wwwwwwaa::::::::::::awwwwwwx::::::::xwwwwwwwwwwwwwwwwwwT:::::Twwwwwo::::owwwwwo::::oo::::owwwwwo::::owl::::lwwwws::::::swwwwww
#  wwwwwwwW:::::W:::::WwwwW:::::W:::::Wwwwwwa::::aaaa::::::awwwwwwx::::::::xwwwwwwwwwwwwwwwwwwT:::::Twwwwwo::::owwwwwo::::oo::::owwwwwo::::owl::::lwwwwwwws::::::swww
#  wwwwwwwwW:::::::::WwwwwwW:::::::::Wwwwwwa::::awwwwa:::::awwwwwx::::::::::xwwwwwwwwwwwwwwwwwT:::::Twwwwwo::::owwwwwo::::oo::::owwwwwo::::owl::::lwsssssswwws:::::sw
#  wwwwwwwwwW:::::::WwwwwwwwW:::::::Wwwwwwwa::::awwwwa:::::awwwwx:::::xx:::::xwwwwwwwwwwwwwwTT:::::::TTwwwo:::::ooooo:::::oo:::::ooooo:::::ol::::::ls:::::ssss::::::s
#  wwwwwwwwwwW:::::WwwwwwwwwwW:::::Wwwwwwwwa:::::aaaa::::::awwwx:::::xwwx:::::xwwwwwwwwwwwwwT:::::::::Twwwo:::::::::::::::oo:::::::::::::::ol::::::ls::::::::::::::sw
#  wwwwwwwwwwwW:::WwwwwwwwwwwwW:::Wwwwwwwwwwa::::::::::aa:::awx:::::xwwwwx:::::xwwwwwwwwwwwwT:::::::::Twwwwoo:::::::::::oowwoo:::::::::::oowl::::::lws:::::::::::ssww
#  wwwwwwwwwwwwWWWwwwwwwwwwwwwwWWWwwwwwwwwwwwaaaaaaaaaawwaaaaxxxxxxxwwwwwwxxxxxxxwwwwwwwwwwwTTTTTTTTTTTwwwwwwooooooooooowwwwwwooooooooooowwwllllllllwwssssssssssswwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
"""

print(wax)

def get_api_key():
    api_key = input("Votre Clé API a bien été Confirmée :  ")
    with open('api_key.txt', 'w') as key_file:
        key_file.write(api_key)
    print("Clé API enregistrée avec succès.")

def download_website():
    api_key = load_api_key()

    while not api_key:
        print("Clé API non enregistrée.")
        register_key = input("Veuillez entrer votre clé API : ").strip()

        if register_key == 'vgWtOGgg3WsMx0yaYgOk1YUDH1PSnBgVM53RrEPztceYf3xujoQ5koaBzz2gjRU':
            get_api_key()
            api_key = load_api_key()
        else:
            print("Clé API invalide. Veuillez entrer une clé API valide pour continuer.")

    homepage_url = input("Veuillez entrer l'URL du site web à télécharger : ")
    output_dir = 'downloaded_website'
    os.makedirs(output_dir, exist_ok=True)
    download_page(homepage_url, output_dir, api_key)

    print("Le téléchargement du site web est terminé avec succès.")

def load_api_key():
    if os.path.exists('api_key.txt'):
        with open('api_key.txt', 'r') as key_file:
            return key_file.read().strip()
    else:
        return None

def download_page(url, output_dir, api_key):
    if not api_key:
        print("Clé API non enregistrée. Veuillez enregistrer une clé API valide.")
        return

    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else 'index'
        output_path = os.path.join(output_dir, f'{title}.html')

        download_css_js(soup, url, output_dir, headers)

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(str(soup))

        print(f"Page téléchargée : {title}")
    else:
        print(f"Échec du téléchargement de la page {url}. Code d'état : {response.status_code}")

def download_css_js(soup, page_url, output_dir, headers):
    css_links = soup.find_all('link', {'rel': 'stylesheet'})
    for css_link in css_links:
        css_url = urljoin(page_url, css_link['href'])
        download_file(css_url, output_dir, headers)

    js_scripts = soup.find_all('script', {'src': True})
    for js_script in js_scripts:
        js_url = urljoin(page_url, js_script['src'])
        download_file(js_url, output_dir, headers)

def download_file(url, output_dir, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_name = os.path.basename(urlparse(url).path)
        output_path = os.path.join(output_dir, file_name)
        with open(output_path, 'wb') as output_file:
            output_file.write(response.content)
        print(f"Fichier téléchargé : {file_name}")
    else:
        print(f"Échec du téléchargement du fichier {url}. Code d'état : {response.status_code}")

if __name__ == "__main__":
    download_website()

time.sleep(15)
print(wax)
