from django.shortcuts import render
from django import forms

# Now we have to create a form to take 2 numbers and then store those numbers into some variable for further calculations
class userNumbers(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()

# Create your views here
def calculations(request):
    form = userNumbers(request.POST)
    if form.is_valid():
        num1 = form.cleaned_data['num1']
        num2 = form.cleaned_data['num2']

    return render(request, 'calculator/calculations.html', {
        'form' : form
    })

def result(request):

    form = userNumbers(request.POST)
    if form.is_valid():
        num1 = form.cleaned_data['num1']
        num2 = form.cleaned_data['num2']
    
    result = num1 + num2

    return render(request, 'calculator/results.html', {
        'result' : result
    })
