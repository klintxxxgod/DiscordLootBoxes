from pystyle import *
import os
import json
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

 ██ ▄█▀  ██▓     ██▓ ███▄    █ ▄▄▄█████▓     ▒█████   ▄████ 
 ██▄█▒  ▓██▒   ▒▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒    ▒██▒  ██▒ ██▒ ▀█
▓███▄░  ▒██░   ▒▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░    ▒██░  ██▒▒██░▄▄▄      ds: .klintxxxgod
▓██ █▄  ▒██░   ░░██░▓██▒  ▐▌██▒░ ▓██▓ ░     ▒██   ██░░▓█  ██      tg: @klintxxxgod 
▒██▒ █▄▒░██████░░██░▒██░   ▓██░  ▒██▒ ░     ░ ████▓▒░▒▓███▀▒
▒ ▒▒ ▓▒░░ ▒░▓   ░▓  ░ ▒░   ▒ ▒   ▒ ░░       ░ ▒░▒░▒░ ░▒   ▒ 
░ ░▒ ▒░░░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░    ░          ░ ▒ ▒░  ░   ░ 
░ ░░ ░    ░ ░  ░ ▒ ░   ░   ░ ░   ░          ░ ░ ░ ▒   ░   ░ 
░  ░   ░    ░    ░           ░                  ░ ░       ░ 

                > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.RED}

 ██ ▄█▀  ██▓     ██▓ ███▄    █ ▄▄▄█████▓     ▒█████   ▄████ 
 ██▄█▒  ▓██▒   ▒▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒    ▒██▒  ██▒ ██▒ ▀█
▓███▄░  ▒██░   ▒▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░    ▒██░  ██▒▒██░▄▄▄      ds: .klintxxxgod
▓██ █▄  ▒██░   ░░██░▓██▒  ▐▌██▒░ ▓██▓ ░     ▒██   ██░░▓█  ██      tg: @klintxxxgod 
▒██▒ █▄▒░██████░░██░▒██░   ▓██░  ▒██▒ ░     ░ ████▓▒░▒▓███▀▒
▒ ▒▒ ▓▒░░ ▒░▓   ░▓  ░ ▒░   ▒ ▒   ▒ ░░       ░ ▒░▒░▒░ ░▒   ▒ 
░ ░▒ ▒░░░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░    ░          ░ ▒ ▒░  ░   ░ 
░ ░░ ░    ░ ░  ░ ▒ ░   ░   ░ ░   ░          ░ ░ ░ ▒   ░   ░ 
░  ░   ░    ░    ░           ░                  ░ ░       ░ 


""")

time.sleep(1)


while True:
    
    print("\nWhich option do you want to choose: ", Colors.red)
    print("\n1. Enter Token", Colors.red)
    print("\n2. Start", Colors.red)
    print("\n3. Close", Colors.red)
    print("\nMake your selection: ", Colors.red, end="")
    choice = input()

    if choice == "1":
        if not os.path.exists("config.json"):    
            with open("config.json", "w") as file:
                        json.dump({}, file)
        os.system("cls || clear")
        token = input("Enter your token: ")
        data = {"token": token}
        with open("config.json", "w") as file:
            json.dump(data, file)
        print("Token saved successfully.")
    elif choice == "2":
        
        url = 'https://discord.com/api/v9/users/@me/lootboxes/open'
        with open("config.json", "r") as arquivo:
            token = json.load(arquivo)

        headers = {
            'Authorization': token['token'],
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI4MDQ3MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
        }

        tentativa_atual = 1

        while True:
            res = requests.post(url, headers=headers)

            if res.status_code == 200:
                print(f"{Fore.WHITE}[{Fore.GREEN}{tentativa_atual}{Fore.WHITE}] {Fore.GREEN} New item collected!", Colors.red)
            elif res.status_code == 429:
                print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED}You are collecting items very quickly! Wait a while before trying again.', Colors.red)
            else:
                print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Fore.RED}An error occurred while trying {tentativa_atual}:', Colors.red)

            tentativa_atual += 1

            time.sleep(3) 

    elif choice == "3":
        Write.Print("\nExiting the program...", Colors.red)
        break

    else:
        Write.Print("\nYou have entered invalid. Please try again.", Colors.red)
