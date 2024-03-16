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
            result = f"Natija: {c}"

        return render(request, 'guruh.html', {'result': result})
    else:
        return render(request, 'guruh.html')