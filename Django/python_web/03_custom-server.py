from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Custom Python Server</h1>")

server = HTTPServer(('localhost', 8000), MyHandler)
print('서버 실행 중... http://localhost:8000')
server.serve_forever()
