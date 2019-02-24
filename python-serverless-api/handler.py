import json

def hello1(event, context):
    return dict(
        statusCode=200,
        body="hello"
    )
