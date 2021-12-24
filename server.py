import socketserver
import http.server
import logging
import cgi
import random
import time

PORT = 8080

class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        http.server.SimpleHTTPRequestHandler.do_GET(self)
        
        random.seed(time.time())
        print("----------------------\n")
        
        # random number to avoid overwritting files
        NUM_APPENDED = str(random.random())[2:7]
        
        FILENAME = "./" + NUM_APPENDED + str(form.list[0].filename)
        
        bytes = form.getvalue('filename')
        f = open(FILENAME, "wb")
        f.write(bytes)
        f.close()

Handler = ServerHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
