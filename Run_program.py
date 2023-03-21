
from amazon_webscraper import amazon_webscraper
from flipkart_webscraper import flipkart_webscraper
from email_automation import email_automation
from tabulate import tabulate

ascii_art = '''  _____      _            __  __       _ _           
 |  __ \    (_)          |  \/  |     (_) |          
 | |__) | __ _  ___ ___  | \  / | __ _ _| | ___ _ __ 
 |  ___/ '__| |/ __/ _ \ | |\/| |/ _` | | |/ _ \ '__|
 | |   | |  | | (_|  __/ | |  | | (_| | | |  __/ |   
 |_|   |_|  |_|\___\___| |_|  |_|\__,_|_|_|\___|_|   
                                                     '''

print(ascii_art + "by Pratik\n\n")

print('Enter the product you want to search:',end="")
product = input('>')

flipkart_product, flipkart_price = flipkart_webscraper(product)
amazon_product, amazon_price= amazon_webscraper(product)

print('Do you want the prices to be mailed to you? (Y/N)',end="")
w = input('>')

if w.upper() == 'Y':
	to_mail = input('Enter the Mail you want the prices to be sent.(For Multiple email ids write them seperated by commas(","))\t>').split(',')
	email_automation(to_mail, flipkart_product, flipkart_price, amazon_product, amazon_price,product)

if w.upper() == 'N':
	print(tabulate({'Amazon-Products':amazon_product,'Prices':amazon_price},headers='keys'))
	print(tabulate({'Flipkart-Products':flipkart_product,'Prices':flipkart_price},headers='keys'))
