import boto3, json

def lambda_handler(event, context):
    msg_id = event['Records'][0]['Sns']['MessageId']
    msg_data = event['Records'][0]['Sns'][Message]

    client = boto3.client('iot-data', region_name='us-east-1')
    link = "<a href=\"https://my.api/v1/get_email?id="+msg_id+"\"/>Click</a>"
    response = client.publish(
                topic='protego-a7-topic',
                qos=1,
                payload=json.dumps({"msg": msg_data, "id": link})
        )
