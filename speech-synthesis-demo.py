from ispeech import *

speechsynthesizer = speechsynthesizer()
speechsynthesizer.set_parameter("server", "http://api.ispeech.org/api/rest")
speechsynthesizer.set_parameter("apikey", "developerdemokeydeveloperdemokey")
speechsynthesizer.set_parameter("text", "yes")
speechsynthesizer.set_parameter("format", "mp3")
speechsynthesizer.set_parameter("voice", "usenglishfemale")
speechsynthesizer.set_parameter("output", "json")
result = speechsynthesizer.make_request()

if isinstance(result, dict): #error occured
    print(result["error"])
else:
    print(speechsynthesizer.file_put_contents("output.mp3", result))
