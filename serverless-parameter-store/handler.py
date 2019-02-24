#!/usr/bin/python
import json
import boto3

def parameterstore(event, context):
    body = {'message' : 'You did not provide a Parameter Name'}
    client = boto3.client('ssm')
    try:
        if event['httpMethod'] == 'GET' and event['queryStringParameters']['ParameterName']:
            resp = client.get_parameter( Name = event['queryStringParameters']['ParameterName'], WithDecryption=True)
            body = resp['Parameter']
    except Exception as e:
        body = {'message' : 'You did not provide a Parameter Name',
                'Error': str(e)
                }
        pass
    response = {'statusCode': 200, 'body': json.dumps(body)}
    return response
