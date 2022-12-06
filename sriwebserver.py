from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<html>
<head>
<tittle> My web server</tittle>
</head>
<body>
<h1>Top Five Web Application Development Framework</h1>
<h2>1.Django</h2>
<h2>2.MEAN</h2>
</body>
</html>
'''

class Myserver(BaseHTTPRequestHandler):
     def do_GET(self):
         print("GET request recieved...")
         self.send_response(200)
         self.end_headers()
         self.wfile.write(content.encode())

         print("This is my webserver")
server_address=(' ',80)
httpd=HTTPServer(server_address,Myserver)
httpd.serve_forever()         