#Put the product and its unit price in a dictionary
basket={'Leather_wallet': 1100, 'Umbrella':900, 'Cigarette':200, 'Honey':100}

#Calculate price of each with its quantity
Wallet_price = basket['Leather_wallet'] * 1
Umbrella_price = basket['Umbrella'] * 4
Cigarette_price = basket['Cigarette'] * 3
Honey_price = basket['Honey'] * 2

#Calculate tax i.e. gst of each product
wallet_tax = (18/100) * (Wallet_price)
umbrella_tax = (12/100) * (Umbrella_price)
cigarette_tax=(28/100) * (Cigarette_price)
honey_tax = 0

#Put all GSTs in a dictionary
taxes = {'Wallet' : wallet_tax, 'umbrella' : umbrella_tax, 'cigarette' : cigarette_tax, 'honey' : honey_tax}

#Compute maximum payed 
max_tax = wallet_tax
for i in taxes.keys():
    if taxes[i] > max_tax:
        max_tax = taxes[i]
        product = i

#Print the product and the tax paid
print('*****************************************')
print('OUTPUT \n')
print('Product having highest GST amount is= ', product, '\n')
print('Maximum tax paid for ' , product , 'is= ' ,max_tax, '\n')

#Calculate amount after 5% discount on wallet and umbrella
wallet_after_discount = Wallet_price - ((5/100) * Wallet_price)
umbrella_after_discount = Umbrella_price - ((5/100) * Umbrella_price)

#Add tax GST and the product price
total_wallet_price = wallet_after_discount + wallet_tax
total_umbrella_price = umbrella_after_discount + umbrella_tax
total_cigarette_price = Cigarette_price + cigarette_tax

#Compute the Total Basket price
total_price = (total_wallet_price + total_umbrella_price + total_cigarette_price + Honey_price)

print('Total amount to be paid to shopkeeper is= ', total_price, '\n')
print('******************************************')