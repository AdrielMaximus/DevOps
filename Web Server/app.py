# Save this code in a file, e.g., server.py

from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the port number
PORT = 8000

# Define the handler class
class MyHandler(SimpleHTTPRequestHandler):
    pass

# Create the server object
with HTTPServer(('localhost', PORT), MyHandler) as server:
    print(f'Server started on localhost:{PORT}')
    server.serve_forever()
