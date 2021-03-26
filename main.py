# push test - update B2 branch

import http.server as SimpleHTTPServer
import socketserver as SocketServer
import logging

PORT = 8000

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        # print('got client')
        # logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        # self.send_response(200, "")


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()