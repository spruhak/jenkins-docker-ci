from http.server import BaseHTTPRequestHandler, HTTPServer

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Jenkins CI/CD Pipeline\n")
        self.wfile.write(b"Feature branch version - testing")

HTTPServer(("0.0.0.0", 8000), App).serve_forever()

