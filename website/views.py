from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == 'POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		send_mail(
			'Message from ' + message_name, # subject
			message, # message
			message_email, # from email
			['riksmith1@hotmail.com'], # to email
		)
		return render(request, 'contact.html', {'message_name': message_name})
	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def services(request):
	return render(request, 'services.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def appointment(request):
	if request.method == 'POST':
		print(request.POST)
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_time = request.POST['your-time']
		your_message = request.POST['your-message']

		msg = f'{your_name} would like to book an appointment on {your_time} at {your_schedule}' \
			  f'Phone Number: {your_phone}. Address: {your_address}.\nMessage: {your_message}'
		send_mail(
			'Appointment Request', # subject
			msg, # message
			your_email, # from email
			['riksmith1@hotmail.com'], # to email
		)
		context = {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_schedule': your_schedule,
			'your_time': your_time,
			'your_message': your_message,
		}
		return render(request, 'appointment.html', context)
	else:
		return render(request, 'home.html', {})