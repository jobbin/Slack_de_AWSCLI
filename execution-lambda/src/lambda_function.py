# -*- coding: utf-8 -*-
import commands
import json
import os
from cStringIO import StringIO
import re
import urllib
from urllib2 import Request, urlopen, URLError, HTTPError

print('Loading function')

def _(cmd):
    return commands.getoutput(cmd)

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    #response_urlのデコード
    response_url = urllib.unquote(event['response_url']).encode('raw_unicode_escape').decode('utf-8')
    print(response_url)

    slack_message = {
        'channel': event['channel_name'],
        'response_type': 'ephemeral',
        'isDelayedResponse': 'true',
        'text': "response for: `aws " + event['text'] + "`\n" + _("./aws " + event['text'])
    }
    req = Request(response_url)
    req.add_header('Content-Type', 'application/json')
    try:
        response = urlopen(req, json.dumps(slack_message))
        response.read()
        print("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        print("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        print("Server connection failed: %s", e.reason)
