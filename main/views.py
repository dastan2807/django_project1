from django.shortcuts import render

# Create your views here.
def main(request):
    context = {

    }
    return render(request, 'index.html', context)

def bank(request):
    context = {

    }
    return render(request, 'bank.html', context)
def internalCode(request):
    context = {

    }
    return render(request, 'InternalCode.html', context)