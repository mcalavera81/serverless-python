import json


def hello(event, context):

    print("New invocation:" + json.dumps(event))


    body = {
        "message": "Go Serverless v9.0! ",
        "input": json.dumps(event)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "event": event
    }
    """
