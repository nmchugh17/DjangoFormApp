from django.shortcuts import render
from .forms import ApplicationForm
from.models import Form


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

        # message_body = f"Thank you for your submission {first_name}." \
        #                f"Here is your data: \n{first_name}\n{last_name}\n{date}\n"

        # message = Message(
        #     subject='New Form Submission',
        #     sender=app.config["MAIL_USERNAME"],
        #     recipients=[email],
        #     body=message_body
        # )

        # mail.send(message)

        # flash(f"{first_name}, Your form was submitted successfully!", "success")

    return render(request, "index.html")
