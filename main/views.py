from django.shortcuts import render

def main(request):
    return render(request, "main.test.html")

def guide(request):
    return render(request, "guide.test.html")