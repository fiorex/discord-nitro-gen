import requests
import random
import string
from colorama import init
from colorama import Fore, Back, Style
import time
init(autoreset=True)

def start():
    with open("Nitro Codes.txt", "w", encoding='utf-8') as file:

        for i in range(number):
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,k = 16))

            file.write(f"https://discord.gift/{code}\n")

        print(Fore.YELLOW+f"{number} Adet Nitro Codes Oluşturuluyor\n")

    with open("Nitro Codes.txt") as file:
        for line in file.readlines():
            nitrocode = line.strip("\n")

            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
            file.close()
            r = requests.get(url)
            
            if r.status_code == 200:
                time.sleep(0.8)
                print(Back.BLACK,Fore.GREEN+f"\nGeçerli | {nitrocode}")

            else:
                time.sleep(0.8)
                print(Back.BLACK,Fore.RED+f"\nGeçersiz | {nitrocode}", end = "")

number = int(input('Nitro Adet Sayısını Giriniz: '))

if number<1:
   print("Sayı 1'den Küçük Olamaz")
   quit()

elif number>10000:
   print("Sayı 10000'den Büyük Olamaz")
   quit()

elif type(number) != int:
    print("Geçersiz Sayı")
    quit()

else:
   start()
