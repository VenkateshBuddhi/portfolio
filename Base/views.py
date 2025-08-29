
# Create your views here.

# def Home(request):
#     return render(request,'home.html')

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from .models import Contact

def portfolio_view(request):
    """Portfolio view with contact form handling"""
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', 'No Subject')
        message = request.POST.get('message', '')
        
        # Basic validation
        if not name or not email or not message:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'home.html')
        
        # Save to database
        try:
            contact = Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
        except Exception as e:
            messages.error(request, 'There was an error saving your message. Please try again.')
            return render(request, 'home.html')
        
        # Send email
        email_subject = f"Portfolio Contact: {subject}"
        email_message = f"""
        Name: {name}
        Email: {email}
        Message: {message}
        
        Received from your portfolio website.
        """
        
        try:
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],  # Your email address
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except BadHeaderError:
            messages.error(request, 'Invalid header found.')
        except Exception as e:
            # Even if email fails, we still saved the message to database
            messages.warning(request, 'Your message was received but there was an issue with email notification.')
        
        return redirect('/#contact')
    
    # If GET request, just render the portfolio page
    return render(request, 'home.html')