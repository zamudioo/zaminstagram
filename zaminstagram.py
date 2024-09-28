from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
import os
import time
from datetime import datetime
from PIL import Image, ImageDraw
import random
from http.cookiejar import CookieJar

USER= 'username of your ig account'
PWD= 'your instagram password'
PATH_PHOTO= './letter/letter.png' #replace letter.png to your photo in png with whatever letter you want the background to be replaced randomly, they all are in the folder letter, or use the other git code to generate your own letter or phrases, then replace where that photo or phrase is located
COOKIE_FILE = './cookies.json'
EXTENSION_PATH = './chaff.crx'

def iniciar_navegador_con_extension():
    chrome_options = Options()
    chrome_options.add_extension(EXTENSION_PATH)
    
    user_agent = random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
    ])
    chrome_options.add_argument(f"user-agent={user_agent}")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.instagram.com")
    
    time.sleep(random.uniform(10, 20) * 60)  

    cookies = driver.get_cookies()
    driver.quit()
    
    guardar_cookies_selenium(cookies)
    print("Extensión ejecutada y cookies guardadas")
    return cookies

def guardar_cookies_selenium(cookies):
    with open(COOKIE_FILE, 'w') as f:
        json.dump(cookies, f)

def cargar_cookies():
    if os.path.exists(COOKIE_FILE):
        with open(COOKIE_FILE, 'r') as f:
            cookies = json.load(f)
            session = requests.Session()
            jar = requests.cookies.RequestsCookieJar()
            
            for cookie in cookies:
                jar.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie.get('path', '/'))
            
            session.cookies.update(jar)
            print("Sesión cargada desde cookies")
            return session, jar
    return None, None

def random_color():
    while True:
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if color != (0, 0, 0) and color != (255, 255, 255):
            return color

def generar_foto_perfil():
    foreground = Image.open(PATH_PHOTO).convert("RGBA")
    width, height = foreground.size

    background = Image.new("RGBA", (width, height), random_color())
    background.paste(foreground, (0, 0), foreground)
    
    background = background.convert("RGB")
    background.save("foto.png")
    print("Foto generada/actualizada")

def guardar_cookies(session, cookies):
    data = {
        "cookies": cookies,
        "session_headers": dict(session.headers)
    }
    with open(COOKIE_FILE, 'w') as f:
        json.dump(data, f)
    print("Cookies guardadas en el json")

def login_instagram(username, password):
    session, cookies = cargar_cookies()

    if session and cookies:
        perfil_url = 'https://www.instagram.com/accounts/edit/'
        perfil_response = session.get(perfil_url)
        if perfil_response.status_code == 200:
            print("Sesión previamente iniciada, usando cookies guardadas.")
            return session, cookies
        else:
            print("Cookies expiradas o inválidas, realizando nuevo login.")

    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    link = 'https://www.instagram.com/accounts/login/'
    
    time_now = int(datetime.now().timestamp())
    session = requests.Session()
    response = session.get(link)
    csrf_token = response.cookies.get('csrftoken', '')

    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_header = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
        ]),
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf_token
    }

    login_response = session.post(login_url, data=payload, headers=login_header)
    login_data = json.loads(login_response.text)

    if login_data.get("authenticated"):
        print("Login exitoso")
        cookies = session.cookies.get_dict()
        guardar_cookies(session, cookies)
        return session, cookies
    else:
        print("Error en login", login_response.text)
        return None, None

def subir_foto_perfil(session, cookies, image_path):
    url_editar_perfil = 'https://www.instagram.com/accounts/web_change_profile_picture/'
    csrf_token = cookies.get('csrftoken')

    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
        ]),
        "x-csrftoken": csrf_token,
        "Referer": "https://www.instagram.com/accounts/edit/",
    }

    files = {
        'profile_pic': ('profile_pic.jpg', image_data, 'image/jpeg')
    }

    response = session.post(url_editar_perfil, headers=headers, files=files)
    
    if response.status_code == 200:
        print("Foto de perfil actualizada correctamente.")
    else:
        print("Error al cambiar la foto de perfil:", response.text)

if __name__ == "__main__":
    username = USER
    password = PWD
    image_path = "foto.png"

    if not os.path.exists(COOKIE_FILE):
        iniciar_navegador_con_extension()

    session, cookies = login_instagram(username, password)

    if session and cookies:
        while True:
            generar_foto_perfil()
            subir_foto_perfil(session, cookies, image_path)
            time.sleep(random.uniform(10800, 14400)) 
    else:
        print("Error en el login")

