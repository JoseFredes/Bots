import pyautogui
import webbrowser
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/es/"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
quotes_html = html.find_all('div', class_="price___3rj7O" )
numero = "Agregar numero de telefono"
quotes = list()
for quote in quotes_html:
    quotes.append(quote.text)

tiempo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

webbrowser.open("https://web.whatsapp.com/send?phone="+numero)
time.sleep(5)


for i in range(12):

  pyautogui.write("dia de hoy  : \n"+ tiempo +"\n"+"El valor es: \n "+"BTC " + quotes[0] + "\n" + "ETH " + quotes[1]+ "\n" + "ADA " + quotes[6])
  pyautogui.press("enter")