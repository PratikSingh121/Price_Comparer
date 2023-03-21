def flipkart_webscraper(product):
	import requests
	import lxml
	from bs4 import BeautifulSoup
	from flipkart_url_maker import url_maker
	
	url = url_maker(product)

	html = requests.get(url).text
	soup = BeautifulSoup(html, 'lxml')
	product_html = soup.find_all('div', class_='_4rR01T')
	price_html = soup.find_all('div', class_='_30jeq3 _1_WHN1')

	def text_maker(value):
		parsed = value.text
		return parsed

	flipkart_product_list = list(map(text_maker, product_html))
	if len(flipkart_product_list) == 0:
		product_html = soup.find_all('a', class_='s1Q9rs')
		price_html = soup.find_all('div', class_='_30jeq3')
	flipkart_product_list = list(map(text_maker, product_html))
	
	if len(flipkart_product_list) == 0:
		product_html = soup.find_all('a', class_='IRpwTa')
		price_html = soup.find_all('div', class_='_30jeq3')
	
	flipkart_price_list = list(map(text_maker, price_html))

#	print(tabulate({'Product':flipkart_product_list,'Price':flipkart_price_list},headers='keys'))
	return flipkart_product_list,flipkart_price_list