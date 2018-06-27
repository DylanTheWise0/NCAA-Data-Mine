import keyring
import smtplib

def Main():
	msg = "\r\n".join([
		"From: ",
		"To: ",
		"Subject: NCAA stats update script has stopped",
		"",
		"The script has stopped running and needs to be restarted."
		])
		
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	
	
	server.login('', keyring.get_password('MailBot',''))
	server.sendmail("", [''], msg)
	server.quit()

Main()
