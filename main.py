from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window

driver.get("https://www.trendyol.com/sr?wc=144046&os=1&sk=1")

total_price = 0

if driver.find_elements(By.CLASS_NAME, "prc-box-dscntd"):
    playstation_5_prices = driver.find_elements(By.CLASS_NAME, "prc-box-dscntd")
    for i, price in enumerate(playstation_5_prices, start=1):
        try:
            each_price = float(price.text.replace("TL","").replace(".","").strip())
            if each_price >= 10000:
                total_price += each_price
                print(f"Price {i}: {each_price:.0f} TL")
            else:
                print(f"Price {i}(Skipped): {each_price:.0f} TL") #Fiyatı 10000 TL'den küçük olanlar Playstation 5 değildir. Playstation kolu, oyun vb. olabilir. Bu yüzden toplam fiyata dahil edilmemiştir!   
        except ValueError:
            print(f"Invalid Price {i}: {each_price:.0f} TL")
    print(f"Total Price: {total_price:.0f} TL")

else:
    print("Price box not found!")

driver.quit()