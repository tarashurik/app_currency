from django.shortcuts import render


def main_page(request):
    if request.method == 'GET':
        return render(request=request, template_name='index.html')
