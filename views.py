from simple_web_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')


class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html')
