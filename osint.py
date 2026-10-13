import requests
domains = input("Target email: ").lower().split("@")[1]
url = f"https://open.kickbox.com/v1/disposable/{domains}"
answer = requests.get(url)
data_mails = answer.json()
if data_mails["disposable"]:
    print(f"❌ Domain {domains} is blacklisted")
else:
    print(f"✅ Domain {domains} is clean")


