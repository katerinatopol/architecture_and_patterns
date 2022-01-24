class IndexPage:
    def __call__(self):
        return '200 OK', b'Hello world from a simple WSGI application!'


class AboutPage:
    def __call__(self):
        return '200 OK', b'About page'


class NotFoundPage:
    def __call__(self):
        return '404 Not Found', b'404 page not found'


routes = {'/': IndexPage(),
          '/about': AboutPage(),}


def application(environ, start_response):
    """
    :param environ: словарь данных от сервера
    :param start_response: функция для ответа серверу
    """
    path = environ['PATH_INFO']
    if path in routes:
        controller = routes[path]
    else:
        controller = NotFoundPage()

    code, body = controller()
    start_response(code, [('Content-Type', 'text/html')])

    return [body]
