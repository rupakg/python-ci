class HelloWorld:
    def say_hello(self, event):
        return {
            "message": "Go Serverless v1.0! Your function executed successfully!",
            "input": event
        }
