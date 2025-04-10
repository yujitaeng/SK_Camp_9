from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    return [b"<h1>Hello with WSGI</h1>"]

with make_server('', 8000, application) as s:
    print('WSGI 서버 실행 중... http://localhost:8000')
    s.serve_forever()
