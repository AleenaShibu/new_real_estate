from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_name = request.POST['listing_name']
        listing = request.POST['listing']
        place = request.POST['place']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        owner_name = request.POST['owner_name']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
                user_id = request.user.id
                has_contacted = Contact.objects.all().filter(listing_name=listing_id, user_id=user_name)
                if has_contacted:
                        messages.error(request, 'You have already made an inquiry for this listing')
                        return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_name=listing_name, owner_name=name, email=email, phone=phone, message=message, user_name=user_name)
        contact.save()

        # Send email
        send_mail(
                'Property Listing Inquiry',
                'There has been an inquiry for ' + listing + '. Sign into the admin panel for more',
                'YourEmail',
                [realtor_email],
                f
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soo')
        return redirect('/listings/'+listing_name)
