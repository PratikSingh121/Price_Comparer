def amazon_webscraper(product):
	import requests
	import lxml
	from bs4 import BeautifulSoup
	from amazon_url_maker import url_maker
	
	url = url_maker(product)
	new = []
	while True:
		response = requests.get(url)
		html = response.text
		if response.status_code == 200:
			break
		else:
			continue

	soup = BeautifulSoup(html, 'lxml')
	product_html = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
	price_html = soup.find_all('span', class_='a-price-whole')

	def text_maker(value):
		parsed = value.text
		return parsed

	amazon_product_list = list(map(text_maker, product_html))
	if len(amazon_product_list) == 0:
		product_html = soup.find_all('span', class_='a-size-base-plus a-color-base a-text-normal')
		amazon_product_list = list(map(text_maker, product_html))
	for i in amazon_product_list:
		new.append(str(i[0:50])+"...")
	amazon_product_list = new
	amazon_price_list = list(map(text_maker, price_html))

#	print(tabulate({'Product':amazon_product_list,'Price':amazon_price_list},headers='keys'))
	return amazon_product_list, amazon_price_list