#REST API - Python ##

A very simple example of a REST API using python and connection with MySQL database



**Example of a API class**
```python    
from base import dbexc

def testFnc():
	query = "SELECT * FROM teste"

	response = dbexc(query)
	return response
    
```

**The endpoint to call this function is: 'http://localhost/api/teste/testFnc'**

- The url parameter /teste because the API has been in teste.py, and you can create the file with any name, and just import de base to your code, to call the function, chancge testFnc to name of your designed function
