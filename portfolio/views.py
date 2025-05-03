from django.shortcuts import render,redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages

# Your existing views...

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Email body
        email_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        # Send email
        try:
            send_mail(
                f"Contact Form: {subject}",  # Email subject
                email_body,  # Email body
                email,  # From address (the visitor's email)
                ['bannavirru6@gmail.com'],  # Your Gmail address
                fail_silently=False,
            )
            # messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')  # Redirect to your home page after successful submission
        except Exception as e:
            messages.error(request, f'There was an error sending your message: {e}')
    
    return render(request, 'index.html')  # Assuming your form is on the index page

# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    if request.method == 'POST':
        nm=request.POST.get('name')
        em=request.POST.get('email')
        sub=request.POST.get('subject')
        msg=request.POST.get('message')
        data=Contact(name=nm,email=em,subject=sub,message=msg)
        data.save()
        return redirect('index')
    return render(request,'index.html')