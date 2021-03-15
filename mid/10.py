import json

x = input()
json_data = json.loads(x)
tot, tot_name, minim = 0, '', max

for item in json_data["Subscriptions"]:
     price = int(item["price"])
     discount = int(item["discount"])
     tot = int(price*(100 - discount)/100)
     if minim > tot:
         minim = tot
         tot_name = str(item["name"])
print('Name: ' + tot_name)
print('Price: ' + str(minim))