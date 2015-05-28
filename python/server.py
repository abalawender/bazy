# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 13:04:43 2014

@author: balawend
"""
import os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime as dt
import urllib.parse
import time

PORT = 8080

def pathExtract(path):
    """ Extracts path to file from HTTP request path """
    return path.lstrip('/').split('?')[0]

def log(msg):
    """ Log messages and timestamps to stderr """
    sys.stderr.write(str(dt.datetime.now()) + ' : ' + str(msg) + '\n')


class HTTPRequestHandler(BaseHTTPRequestHandler):
    """ Handles HTTP requests and server logs """
    def do_GET(self):
        """ Handle HTTP GET Request"""
        self.path = pathExtract(self.path)

        if os.path.isfile(self.path):
            self.send_response(200)
            self.end_headers()
            with open(os.getcwd() + os.sep + self.path, 'rb') as fileHandle:
                self.wfile.write(fileHandle.read())
        else:
            self.send_response(404, 'Not Found')
            self.end_headers()

    def do_POST(self):
        """ Handle HTTP POST Request"""
        self.path = pathExtract(self.path)
        if self.path in (''):
            self.send_response(200, 'OK')
            self.end_headers()
            with open('report.html', 'rb') as fileHandle:
                self.wfile.write(fileHandle.read())
            length = int(self.headers['content-length'])
            data = self.rfile.read(length)
        elif os.path.isfile(self.path):
            self.send_response(200, 'OK')
            self.end_headers()
            with open(os.getcwd() + os.sep + self.path, 'rb') as fileHandle:
                self.wfile.write(fileHandle.read())
        else:
            self.send_response(404, 'Not Found')
            self.end_headers()
    def log_message(self, frmt, *args):
        pass

if __name__ == '__main__':

    HTTPDeamon = HTTPServer(('', PORT), HTTPRequestHandler)

    print("Listening at port", PORT)

    try:
        HTTPDeamon.serve_forever()
    #except KeyboardInterrupt:
    #    pass
    except ConnectionAbortedError:
        pass

    HTTPDeamon.server_close()
    print("Server stopped\n")
