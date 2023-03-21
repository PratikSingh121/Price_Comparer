def url_maker(product):

	amazon_url = 'https://www.amazon.in/s?k='+product.replace(' ','+').strip()+'&ref=nb_sb_noss_2'
	return amazon_url