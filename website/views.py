from django.shortcuts import render
from django.core.mail import send_mail

### Pass in a request to our back-end webpage When a user requests a page ###

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# Send email
		send_mail(
			message_name, #subject
			message, #message
			message_email, #from email;
			['str8outtajerzy@gmail.com'], # to email'
			fail_silently = False,

			)
		return render(request, 'contact.html', {'message_name': message_name})
	else:
		#return the page
		return render(request, 'contact.html', {})