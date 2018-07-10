def lambda_handler(event, context):
    # TODO implement
    if event.get('patron'):
        patron = event['patron']
    else:
        patron = 'World'
    result = greetPatron(patron)
    return result

def greetPatron(patron):
    return 'Hello ' + patron + '!'
