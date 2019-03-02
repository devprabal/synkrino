import cgi
myform = cgi.FieldStorage()
searchitem = myform.getvalue('search_item_field')
print("Content-type:text/html\r\n\r\n")
print("<html>")
print ("<head>")
print ("<title>Hello CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello %s </h2>" % (searchitem))
print ("</body>")
print ("</html>")

