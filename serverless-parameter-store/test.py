import boto3

client = boto3.client('ssm')


def get_secret(key):
	resp = client.get_parameter(
		Name=key,
		WithDecryption=True
	)
	return resp['Parameter']['Value']

test_token = get_secret('testkey')
print "token received is "+ test_token
#access_token = get_secret('supermanToken')
#database_connection = get_secret('databaseConn')
