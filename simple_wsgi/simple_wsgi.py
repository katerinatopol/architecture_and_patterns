def application(environ, start_response):
    """
    :param environ: словарь данных от сервера
    :param start_response: функция для ответа серверу
    """
    # Сначала в функцию start_response передаем код ответа и заголовки
    start_response('200 OK', [('Content-Type', 'text/html')])
    # Возвращаем тело ответа в виде списка из byte
    return [b'Hello world from a simple WSGI application!']


"""
Запуск: waitress-serve --listen=*:8000 simple_wsgi:application
"""