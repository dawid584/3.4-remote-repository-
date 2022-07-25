sp = []
shop = {"piekarnia" : ["chleb", "pączek", "bułki"] , "warzywniak" : ["marchew", "seler", "rukola"] }
print("Lista zakupów:")
amount = 0
for shop_0 , product in shop.items():
    amount = amount + len(product)