from flask import request
from s1 import app

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    print('path', request.path)
    assert request.path == '/hello'
    assert request.method == 'POST'
