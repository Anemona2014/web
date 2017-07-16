__author__ = 'menkovich'

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    params = environ['QUERY_STRING']
    body = params.replace('&', '\n')
    start_response(status, headers)
    return [body]