from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''<html>  
<head>  <title>my first page</title>
</head> 
<body>  
<table align="center" border="1" bgcolor="white" cellpadding="10" cellspacing="5">
    <caption>List of protocol in TCP/IP PROTOCOLSUITE</caption>
    <tr><th>S.No.</th><th>Name of the layer</th><th>Name of the protocol</th></tr>
    <tr><td>1</td><td bgcolor="red">Application layer</td><td>HTTP,FTP,DNS,TELNET & SSH</td></tr>
    <tr><td>2</td><td bgcolor="yellow">Transport layer</td><td>TCP/UDP</td></tr>
    <tr><td>3</td><td bgcolor="green">Network layer</td><td>IPV4/IPV6</td></tr>
    <tr><td>4</td><td bgcolor="blue">link layer</td><td>Ethernet</td></tr>
</table>
</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()