import random

def lambda_handler(event, context):
    if event.get("calculated_float"):
        rand_float = float(event.get("calculated_float"))
    else:
        rand_float = random.random()
    millenial_quotes = [
        "You're a wizard",
        "He who controls the keyboard controls the universe",
        "Never put twinkies on your pizza"
        ]
    quote_index = int(rand_float * len(millenial_quotes))
    result = millenial_quotes[quote_index]

    return result
