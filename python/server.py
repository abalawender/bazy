import os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime as dt
import urllib.parse
import time
import mapper
from mapper import *
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=mapper.engine)
session = Session()

Base.metadata.bind = mapper.engine
Base.metadata.create_all()
now = dt.datetime.now()

PORT = 8088

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
        self.send_response(200, 'OK')
        self.end_headers()
        length = int(self.headers['content-length'])
        data = self.rfile.read(length)
        print(self.path, ": ", data)
        import urllib.parse
        parsed = urllib.parse.parse_qs(data)
        dec = lambda x: x.decode( encoding='utf-8', errors='replace' )
        parsed2 = { dec(k):dec(i[0]) for k,i in parsed.items() }
        print( parsed2 )
        print( *parsed2 )
        firma = DaneFirmy( **parsed2 )
        session.add( firma )
        session.flush()
        print( firma )

        data = b''
        for firma in session.query(DaneFirmy):
            data += bytes( str(firma)+'<br>', sys.getdefaultencoding() )

        self.wfile.write(data)


        #self.path = pathExtract(self.path)
        #if self.path in (''):
        #    self.send_response(200, 'OK')
        #    self.end_headers()
        #    with open('report.html', 'rb') as fileHandle:
        #        self.wfile.write(fileHandle.read())
        #    length = int(self.headers['content-length'])
        #    data = self.rfile.read(length)
        #elif os.path.isfile(self.path):
        #    self.send_response(200, 'OK')
        #    self.end_headers()
        #    with open(os.getcwd() + os.sep + self.path, 'rb') as fileHandle:
        #        self.wfile.write(fileHandle.read())
        #else:
        #    self.send_response(404, 'Not Found')
        #    self.end_headers()
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
