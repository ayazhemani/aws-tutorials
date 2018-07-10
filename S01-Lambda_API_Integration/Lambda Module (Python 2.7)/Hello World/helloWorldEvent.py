def lambda_handler(event, context):
    # TODO implement
    result = helloWorld()
    return event

def helloWorld():
    return 'Hello World!'
