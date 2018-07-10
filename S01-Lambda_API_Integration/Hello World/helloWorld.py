def lambda_handler(event, context):
    # TODO implement
    result = helloWorld()
    return result

def helloWorld():
    return 'Hello World!'
