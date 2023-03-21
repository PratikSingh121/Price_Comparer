def email_automation(to_mail,flipkart_product, flipkart_price, amazon_product, amazon_price,product):
	#modules
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	from tabulate import tabulate

	#parameters required
	server_add = 'smtp.gmail.com'
	port = 587
	from_mail = 'starsmakegalaxy@gmail.com' 
	password = '!!Believe:ME//'

	msg = MIMEMultipart()

	msg['Subject'] = product.upper() + " Prices"
	msg['To'] = ','.join(to_mail)
	msg['From'] = from_mail

	for comp in ['Amazon','Flipkart']:
		msg.attach(MIMEText("\n"+comp+" Prices:\n", 'plain'))
		if comp == 'Amazon':
			msg.attach(MIMEText(tabulate({'Amazon-Product':amazon_product,'Price':amazon_price},headers='keys',tablefmt="html"), 'html'))
		if comp == 'Flipkart':
			msg.attach(MIMEText(tabulate({'Flipkart-Product':flipkart_product,'Price':flipkart_price},headers='keys',tablefmt="html"), 'html'))

	with smtplib.SMTP(server_add, port) as server:
		server.set_debuglevel(1)
		server.ehlo()
		server.starttls()

		server.login(from_mail, password)
		server.sendmail(from_mail, to_mail, msg.as_string())