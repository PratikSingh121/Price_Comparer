
def url_maker(product):

	flipkart_url = 'https://www.flipkart.com/search?q='+product.replace(" ",'%20')+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
	return flipkart_url
