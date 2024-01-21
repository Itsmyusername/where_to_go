from django.http import HttpResponse


def blank_page(request):
    print('Кто-то зашёл на главную!')
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Стартовая</title>
    </head>
    <body>
        <h1>Здесь будет карта</h1>
    </body>
    </html>
    ''')
