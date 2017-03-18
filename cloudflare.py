# python 3 kullanilmistir.
import requests,re
print("""
 ██████╗██╗      ██████╗ ██╗   ██╗██████╗ ███████╗██╗      █████╗ ██████╗ ███████╗
██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗██╔════╝██║     ██╔══██╗██╔══██╗██╔════╝
██║     ██║     ██║   ██║██║   ██║██║  ██║█████╗  ██║     ███████║██████╔╝█████╗  
██║     ██║     ██║   ██║██║   ██║██║  ██║██╔══╝  ██║     ██╔══██║██╔══██╗██╔══╝  
╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝██║     ███████╗██║  ██║██║  ██║███████╗
 ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
        umutbasal.com     github@umutbasal        twitter@umutbsl
""")
site = input("Domain adresini girin example.com : ")
r = requests.post('http://www.crimeflare.com/cgi-bin/cfsearch.cgi',{"cfS":site})
ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}<[^0-9]", r.text)
ips = []
for i in ip:
  ips.append(i.replace("</",""))

if (ips):
  print("== Ip adresleri.")
  for i in ips:
    print("=> "+i)
else:
  print("IP adresi bulunamadi.")
