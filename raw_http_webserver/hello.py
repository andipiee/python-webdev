import http.server
import socketserver

PORT = 4000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Server running at port", PORT)
    httpd.serve_forever()