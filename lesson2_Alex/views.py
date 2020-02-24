from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def hello(request):
    return HttpResponse("Hi")

def http_redirect(request):
    return redirect('/lesson2/target')

def target(request):
    return HttpResponse("Hello from redirect !")

def render_html(request):
    _html = """
        <html>
        <head><title>TTILE</title>
        <body>
            <h1>HELLO FROM RENDER HTML!!!</h1>
        </body>
        </html>
    """
    return HttpResponse(_html)

def render_template(request):
    return render(request, "main.html", {})
