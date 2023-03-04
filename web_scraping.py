import requests
from bs4 import BeautifulSoup

# Kullanıcıdan web sitesi adresini al
url = input("Please enter the website address: ")

# İstek yap ve yanıtı al
response = requests.get(url)

# Eğer yanıt 200 OK ise devam et, aksi takdirde hata mesajı ver
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Başlık etiketlerini topla
    headings = soup.find_all(['h1', 'h2', 'h3'])

    # Toplanan başlık etiketlerini yazdır
    for heading in headings:
        print(heading.text)
else:
    print("The website could not be accessed. Error code:", response.status_code)
