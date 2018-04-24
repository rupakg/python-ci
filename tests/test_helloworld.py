import unittest
from hw.helloworld import HelloWorld
from handler import hello_world

class TestHelloWorld(unittest.TestCase):

    """ test the handler code """
    def test_hello_world(self):
        event = {}
        context = {}

        resp = hello_world(event, context)
        self.assertEqual(resp["statusCode"], 200)

    """ test the lib code """
    def test_say_hello(self):
        event = {}
        world = HelloWorld()

        actual = world.say_hello(event)
        expected = "Go Serverless v1.0! Your function executed successfully!"
        self.assertEqual(actual["message"], expected)

if __name__ == '__main__':
    unittest.main()
