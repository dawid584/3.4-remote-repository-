sp = []
shop = {"piekarnia" : ["chleb", "pączek", "bułki"] , "warzywniak" : ["marchew", "seler", "rukola"] }
print("Lista zakupów:")
amount = 0
for shop_0 , product in shop.items():
    amount = amount + len(product)
    
    sp = [  x.capitalize() for x in product ]
     
    print(f'Idę do {shop_0.title()}, kupuję tu tam : {sp} ' )

print(f"W sumie kupuję {amount} produktów.")