from django.shortcuts import render
from .forms import ContactForm
# Create your views here.


def home(request):
    template = "home/home.html"
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, template, context)