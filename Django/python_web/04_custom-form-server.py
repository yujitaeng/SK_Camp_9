from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class FormHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = """
<html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <form method="POST">
            이름: <input name="name">
            <input type="submit">
        </form>
    </body>
</html>
        """
        self.wfile.write(html.encode('utf-8'))
        
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        raw_data = self.rfile.read(length).decode()
        parsed_data = urllib.parse.parse_qs(raw_data)
        name = parsed_data.get('name', [''])[0]

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=UTF-8')
        self.end_headers()
        self.wfile.write(f"""
<html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>이름: {name}</h1>
    </body>
</html>
""".encode('utf-8'))

server = HTTPServer(('localhost', 8000), FormHandler)
print('서버 실행 중... http://localhost:8000')
server.serve_forever()
