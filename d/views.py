from django.shortcuts import render
import math
def home(request):
    return render(request, 'home.html')

def guruhlash(request):
    if request.method == 'POST':
        n = int(request.POST.get('entry1'))
        m = int(request.POST.get('entry2'))

        if m < n:
            result = "m soni n dan katta bulishi kerak qayta urinib koring"
        else:
            c=math.factorial(m) / (math.factorial(n) * math.factorial(m - n))
            result = f"={c}"

        return render(request, 'guruh.html', {'result': result})
    else:
        return render(request, 'guruh.html')
def takroriy(request):
    if request.method == 'POST':
        n = int(request.POST.get('entry1'))
        m = int(request.POST.get('entry2'))
        if m<n:
            result = "m soni n dan katta bulishi kerak qayta urinib koring"
        else:
            c=math.factorial(m+n-1)/(math.factorial(n)*math.factorial(m-1))
            result = f"={c}"
        return render(request, 'takroriy.html', {'result': result})
    else:
        return render(request, 'takroriy.html')
        
def orin(request):
    if request.method == 'POST':
        n = int(request.POST.get('entry1'))
        m = int(request.POST.get('entry2'))
        c = math.factorial(m)/math.factorial(n)
        result = f"={c}"
        return render(request, 'orin.html', {'result':result})
    else:
        return render(request, 'orin.html')
def p(request):
    if request.method == 'POST':
        n = int(request.POST.get('entry1'))
        c = math.factorial(n)
        result = f"={c}"
        return render(request, 'p.html', {'result':result})
    else:
        return render(request, 'p.html')
