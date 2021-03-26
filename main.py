# first version test - push to github

import http.server as SimpleHTTPServer
import socketserver as SocketServer

PORT = 8000


class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        response = b'Response from server!\nPage text line 2\nPage text line 3'
        self.send_header('Content-type', 'text/unknown')
        # self.send_header('Content-Length', len(response))
        self.end_headers()
        self.wfile.write(response)


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()
