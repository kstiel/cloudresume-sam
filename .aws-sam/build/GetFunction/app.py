import json
import boto3

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cloudresume')

    response = table.get_item(
    Key={
        'ID': 'visitors'
    }
    )

    # Check if the item exists in DynamoDB
    # if 'Item' in response:
    item = response['Item']
    visitor_count = item.get('visitors', 0)  # Default to 0 if 'visitors' attribute is not present
    return {
        "headers": {
            "Access-Control-Allow-Origin":  "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*"
        },
        "statusCode": 200,
        'body': json.dumps({
            "count": str(visitor_count),
        }),
    }   
