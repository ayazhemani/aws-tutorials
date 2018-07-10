import random
import json

def lambda_handler(event, context):
    if event.get("calculated_float"):
        rand_float = event["calculated_float"]
    else:
        rand_float = random.random()
    millenial_quotes = [
        "You're a wizard",
        "He who controls the keyboard controls the universe",
        "Never put twinkies on your pizza"
        ]
    quote_index = int(rand_float * len(millenial_quotes))
    result = millenial_quotes[quote_index]

    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": '*',
        "Access-Control-Allow-Credentials": 'true'
    }
    body = {
        "result": result
    }
    response = {
        "statusCode": 200,
        "headers": headers,
        "body": body
    }
    return response
