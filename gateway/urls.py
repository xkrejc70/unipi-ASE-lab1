'''
HOME_URL = 'http://0.0.0.0'

GATEWAY_PORT = 5000
GATEWAY_URL = HOME_URL + f":{GATEWAY_PORT}"

MATH_PORT = 5001
MATH_URL = HOME_URL + f":{MATH_PORT}"

STRING_PORT = 5002
STRING_URL = HOME_URL + f":{STRING_PORT}"
'''

PORT = ":5000"
GATEWAY_URL = 'http://gateway' + PORT
MATH_URL = 'http://math-service' + PORT
STRING_URL = 'http://string-service' + PORT
