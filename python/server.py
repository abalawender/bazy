import os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime as dt
import urllib.parse
import time
import mapper
from mapper import *
from sqlalchemy.orm import sessionmaker
import urllib.parse
import json

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
    valid = [k for k,i in mapper.__dict__.items() if i.__class__ is sqlalchemy.ext.declarative.api.DeclarativeMeta]

    def do_GET(self):
        """ Handle HTTP GET Request"""
        print( "do_GET: ", self.path )
        self.path = pathExtract(self.path)

        if 'show' in self.path:
            mapReq = self.path.split('/')[-1]
            if mapReq in self.valid:
                self.send_response(200)
                self.end_headers()
                cols = json.dumps( eval(mapReq).__table__.columns.keys(), 'utf-8' )
                with open('show.html', 'r') as fileHandle:
                    self.wfile.write( bytes( fileHandle.read().replace("$name$", mapReq ).replace("$columns$", cols ), 'utf-8' ) )
            else:
                self.send_response(404, 'Not Found')
                self.end_headers()
        elif 'json' in self.path:
            print( 'somebody here wants some JSON' )
            mapReq = self.path.split('/')[-1]
            if mapReq in self.valid:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                query = session.query( eval(mapReq) )
                data = [ { c.name: str( getattr(item, c.name) )
                    for c in item.__table__.columns} for item in query ]
                self.wfile.write( bytes( json.dumps(data, indent=4), 'utf-8' ) )
            else:
                self.send_response(404, 'Not Found')
                self.end_headers()
        elif 'exec' in self.path:
            execReq = self.path.split('/')[-1]+".py"
            print( 'somebody here wants some execution' )
            env = { 'retVal' : None }
            if os.path.isfile( execReq ):
                self.send_response(200)
                self.end_headers()
                with open( execReq ) as f:
                    exec( compile(f.read(), execReq, 'exec' ), env )
                self.wfile.write( bytes(env['retVal'], 'utf-8' ) )
            else:
                self.send_response(418, "Sorry, I'm just a teapot")
                self.end_headers()
        elif os.path.isfile(self.path):
            self.send_response(200)
            self.end_headers()
            with open(os.getcwd() + os.sep + self.path, 'rb') as fileHandle:
                self.wfile.write(fileHandle.read())
        else:
            self.send_response(404, 'Not Found')
            self.end_headers()

    def do_POST(self):
        """ Handle HTTP POST Request"""
        print( "do_POST: ", self.path )
        self.path = pathExtract(self.path)

        length = int(self.headers['content-length'])
        mapReq = self.path.split('/')[-1]
        if length and mapReq in self.valid:
            print( 'somebody here wants to upload stuff' )
            data = self.rfile.read(length)
            print("request came with ", length, " : ", data)

            parsed = urllib.parse.parse_qs(data)
            dec = lambda x: x.decode( encoding='utf-8', errors='replace' )
            parsed2 = { dec(k):dec(i[0]) for k,i in parsed.items() }

            print( parsed2 )
            print( *parsed2 )
            record = eval(mapReq)( **parsed2 )
            session.add( record )
            try:
                session.flush()
                self.send_response(200)
                print( record )
            except:
                print("B-Baka!")
                session.rollback()
                self.send_response(418, "Sorry, I'm just a teapot")

            self.end_headers()

        else:
            self.send_response(418, "I'm just a teapot")
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
