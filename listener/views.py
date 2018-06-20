from django.shortcuts import render

def listener_page(request):
    return render(request, 'listener/listener_page.html', {})
