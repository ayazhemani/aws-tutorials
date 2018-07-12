def lambda_handler(event, context):
    patron = event.get("patron")
    if not patron:
        patron = "World"
    message = "Hello " + str(patron) + "!"
    return message
