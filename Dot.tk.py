banner = """   ___               _                _____     _
  |   \\     ___     | |_             |_   _|   | |__
  | |) |   / _ \    |  _|      _       | |     | / /
  |___/    \\___/    _\\__|    _(_)_    _|_|_    |_\\_\\
_|\"\"\"\"\"| _|\"\"\"\"\"| _|\"\"\"\"\"| _|\"\"\"\"\"| _|\"\"\"\"\"| _|\"\"\"\"\"|
\"`-0-0-' \"`-0-0-' \"`-0-0-' \"`-0-0-' \"`-0-0-' \"`-0-0-'"""
author = """    Coded by Ijaz Ur Rahim A.K.A Muhammad Ibraheem with """
website = "https://ijazurrahim.com/"
from termcolor import colored
from colorama import init
import requests,json
from bs4 import BeautifulSoup
init()
import os
if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")
print colored(banner,"red",attrs={"bold","blink"})
print colored(author,"yellow",attrs={"bold","blink"})+colored("<3","red",attrs={"blink","bold"})
print """    """+colored(website,"blue",attrs={"bold","underline"})+"   "+colored("https://github.com/IJAZ9913","blue",attrs={"bold","underline"})

requests.headers = {}
def checklocation(location):
    html = requests.get("http://www.unece.org/cefact/locode/service/location.html")
    soup = BeautifulSoup(html.content,"lxml")
    table = soup.find("table", attrs={"class":"contenttable"})
    headings = [th.get_text() for th in table.find("tr").find_all("th")]
    datasets = []
    for row in table.find_all("tr")[1:]:
        dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
        datasets.append(dataset)
    for dataset in datasets:
        if "."+dataset[0][1].lower()==location:
            real_location = dataset[1][1].encode('utf-8')
            print "{0:<30}{1:<40}{2:<15}".format(colored(real_location,"blue"),PaidDomains,price)
            break


requests.headers = {
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"en-US,en;q=0.5",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "DNT":"1",
            "Host":"my.freenom.com",
            "Origin":"http://www.dot.tk",
            "Referer":"http://www.dot.tk/en/index.html?lang=en",
            "User-Agent":"Mozilla (X11; Linux i686;) Gecko/20100101 Firefox"
}
text = colored("Enter the Domain You Want: ","green")
site = raw_input(text)
splitted = site.split(".")
if len(splitted)>1:
    domain,tld = site.split(".",1)
else:
    domain = site
    tld = ""
data = {
    "domain":domain,
    "tld":tld
}
r = requests.post("http://my.freenom.com/includes/domains/fn-available.php",data=data,allow_redirects=False)
r = json.loads(r.content)
try:
    if r["top_domain"]["status"]=="AVAILABLE":
        Status = colored(site,"yellow")+colored(" Found", 'Green')
    else:
        Status = colored(site,"yellow")+colored(" Not Found", 'red')
except:
    Status = colored("The Following Domains are available for: ", 'red')+colored(site,"yellow")

print(Status)
global FreeDomains
global price
print colored("{0:<15}{1:<30}{2:<15}{3:<10}".format("Status","Domains","Price(USD)","Type"),"green")
for a in r["free_domains"]:
    data = "{0:<15}{1:<30}{2:<15}{3:<10}".format(a["status"],a["domain"]+a["tld"],a["price_int"]+"."+a["price_cent"],a["type"])
    FreeDomains = colored(data, 'blue')
    print(FreeDomains)
print colored("{0:<30}{1:<30}{2:<15}".format("\nLocation","Domains","Price(USD)"),"green")
b=0
for a in r["paid_domains"]:
    b = b + 1
    data = "{0}".format(a["domain"]+a["tld"])
    PaidDomains = colored(data, 'blue')
    price = a["price_int"]
    if int(price)<=10:
        price = colored(price+"."+a["price_cent"],"blue")
    elif int(price)<50:
        price = colored(price+"."+a["price_cent"],"yellow")
    elif int(price)<100:
        price = colored(price+"."+a["price_cent"],"green")
    elif int(price)>=100:
        price = colored(price+"."+a["price_cent"],"red")
    
    if os.name == 'nt':
        if b == 100:
            more = raw_input("Press Enter/Return to Extract More...")

    if a["location"]=="true":
        try:
            checklocation(a["tld"])
        except:
            print "{0:<30}{1:<40}{2:<15}".format(colored("Location Error","red"),PaidDomains,price)
    else:
        print "{0:<30}{1:<40}{2:<15}".format(colored("No Location","blue"),PaidDomains,price)
exit = raw_input("Press Enter To Exit")
