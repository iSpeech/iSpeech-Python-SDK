import http.client
import urllib.parse
import base64
'''
@author: iSpeech, Inc.
@version: 0.1
@since: Python 3.2.3 (default, Apr 11 2012, 07:12:16) [MSC v.1500 64 bit (AMD64)] on win32
'''
class ispeech:
    parameters = {}
    parameters["device-type"] = "python-SDK-0.1"
    server = "";
    serverpage = "";
        
    def set_parameter(self, key, value):
        if key == "server":
            value = value.replace("http://", "")
            pos = value.find("/")
            self.server = value[0:pos]
            self.serverpage = value[pos:len(value)]
        else:
            self.parameters[key] = value;

    def make_request(self):
        httpClientObj = http.client.HTTPConnection(self.server)
        httpClientObj.request("GET", self.serverpage+"?"+urllib.parse.urlencode(self.parameters))
        httpResponse = httpClientObj.getresponse()
        httpBody = httpResponse.read()
        
        if httpResponse.status != 200:
            return {"error": httpBody}
        
        return httpBody
    
class speechsynthesizer(ispeech):
    def __init__(self):
        super(speechsynthesizer, self).set_parameter("action", "convert")
    def file_put_contents(self, path, data):
        try:
            f = open(path, "wb")
            try:
                result = f.write(data)
            finally:
                f.close()
                return result
        except IOError:
            print("Error writing file")
    
class speechrecognizer(ispeech):
    def __init__(self):
        super(speechrecognizer, self).set_parameter("action", "recognize")
    def file_get_contents(self, path):
        try:
            f = open(path, "rb")
            try:
                result = f.read()
            finally:
                f.close()
                return result
        except IOError:
            print("Error reading file")
    def base64_encode(self, var):
        return base64.encodebytes(var).replace(b'\n',b'')
