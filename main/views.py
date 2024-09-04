from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152310',
        'name': 'Joe Mathew Rusli',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)