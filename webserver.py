#!/usr/bin/env python
import os;
portnumber = int(os.getenv('PORT_NUMBER', 80))
from http.server import BaseHTTPRequestHandler, HTTPServer,socket

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "Webserver connection test succeed to " + socket.gethostname()
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
  print('starting server on port ' + str(portnumber) + '...')

 # Server settings
  server_address = ('', portnumber)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()

run()