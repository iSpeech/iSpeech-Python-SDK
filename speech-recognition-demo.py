from ispeech import *

speechrecognizer = speechrecognizer()
speechrecognizer.set_parameter("server", "http://api.ispeech.org/api/rest")
speechrecognizer.set_parameter("apikey", "developerdemokeydeveloperdemokey")
speechrecognizer.set_parameter("freeform", "3")
speechrecognizer.set_parameter("locale", "en-US")
speechrecognizer.set_parameter("output", "json")
speechrecognizer.set_parameter("content-type", "wav")
speechrecognizer.set_parameter("audio", speechrecognizer.base64_encode(speechrecognizer.file_get_contents("output.wav")))
result = speechrecognizer.make_request()

if isinstance(result, dict): #error occured
    print(result["error"])
else:
    print(result)
