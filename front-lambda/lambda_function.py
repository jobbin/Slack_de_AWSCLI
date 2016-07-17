# -*- coding: utf-8 -*-
from __future__ import print_function
import boto3
import json

print('Loading function')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    #messageが　"+"で連結されたため,"+"をスペースに戻す
    event['text'] = event['text'].replace('+',' ')

    clientLambda = boto3.client("lambda")
    clientLambda.invoke(
        #invokeするLambda Name
        FunctionName="Execution-Lambda",
        InvocationType="Event",
        Payload=json.dumps(event)
    )
    return event # Echo back the first key value
