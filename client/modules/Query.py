import wolframalpha
import sys
import re
from client.app_utils import *

WORDS = ["QUESTION"]

def handle(text, mic, profile):
    app_id='924H4R-9432GUPJU7'

    client = wolframalpha.Client(app_id)

    filename = "static/text/Qresponse.txt"
    mic.say(getResponse(filename))

    query = mic.MactiveListen()
    #query = ' '.join(sys.argv[1:])
    res = client.query(query)

    if len(res.pods) > 0:
        texts = ""
        pod = res.pods[1]
        if pod.text:
            texts = pod.text
        else:
            texts = "I have no answer for that"
        # to skip ascii character in case of error
        texts = texts.encode('ascii', 'ignore')
        mic.say(texts)
    else:
        mic.say("Sorry, I am not sure.")
    response = mic.MactiveListen()
    mic.say(respond(response))

def isValid(text):
   return bool(re.search(r'\bquestion\b', text, re.IGNORECASE))
