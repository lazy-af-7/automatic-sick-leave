import requests
import smtplib
import os

#make a file name api-key.txt and paste your api key in
#it 
api_file=open('api-key.txt')
api_key=api_file.read()
api_file.close()


home=input('Enter your home address: ')
work=input('Enter your work address: ')


url='https://maps.googleapis.com/maps/api/distancematrix/json?units=metric'

print(url+'origins='+home+'&destinations='+work+'&key='+api_key)
#get response
response=requests.get(url+'origins='+home+'&destinations='+work+'&key='+api_key)

time=response.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds=response.json()["rows"][0]["elements"][0]["duration"]["value"]

#travel time 
print('\n The total travel time from home to work is ', time)


if(True):
	sender_email=""
	reciptent=""
	subject="Sick Day"
	message="Hi,\n\n Sorry but I am down from the weather and won't be able to make it to work today.\n"


	#email-format
	email="Subject: {}\n\n{}".format(subject,message)


	#get sender email
	password_file=open('password-file.txt','r')
	password=password_file.readline()
	password_file.close()

	s=smtplib.SMTP("smtp.gmail.com",587,)

	s.starttls()

	s.login(sender_email,password)
	s.sender_email(sender,reciptent,email)
	s.quit()
	print("\n Successfuly sent.\n")









