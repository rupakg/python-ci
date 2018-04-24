from hw.helloworld import HelloWorld
import json

def hello_world(event, context):
    world = HelloWorld()

    response = {
        "statusCode": 200,
        "body": json.dumps(world.say_hello(event))
    }

    return response
