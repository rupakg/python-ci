# Serverless app in Python for CI

A simple serverless Python app that showcases CI with Circle CI. This is a companion app for the blog post [Automating a CI workflow for a Python app with Circle CI]().

![](https://circleci.com/gh/rupakg/python-ci.svg?style=shield&circle-token=:circle-token)

## Local

Before deploying your service, test out the functions and run unit tests locally.

### Test Functions

```
$ sls invoke local -f helloWorld -d '{"body":"blah"}'

{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v1.0! Your function executed successfully!\", \"input\": {\"body\": \"blah\"}}"
}
```

### Run Tests

For running tests with coverage we will use [nose](https://nose.readthedocs.io/en/latest/):
```
$ nosetests --with-coverage --cover-html

..
Name               Stmts   Miss  Cover
--------------------------------------
handler.py             6      0   100%
hw/__init__.py         0      0   100%
hw/helloworld.py       3      0   100%
_bootlocale.py        17     17     0%
--------------------------------------
TOTAL                 26     17    35%
----------------------------------------------------------------------
Ran 2 tests in 0.061s

OK
```

The above command also creates a html representation of the coverage metrics in the default folder `cover` and looks like so:

![Coverage](https://user-images.githubusercontent.com/8188/39218547-48cb51b6-47f3-11e8-9186-c828b75df567.png)


## Deploy

To `deploy` the service to the cloud:

```
$ sls deploy

Serverless: Installing requirements of requirements.txt in .serverless...
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Injecting required Python packages to package...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (977.97 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..............
Serverless: Stack update finished...
Service Information
service: python-ci
stage: dev
region: us-east-1
stack: python-ci-dev
api keys:
  None
endpoints:
  GET - https://xxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/helloworld
functions:
  helloWorld: python-ci-dev-helloWorld
```

### Test functions remotely

To test the function `helloWorld` remotely on the cloud:

```
$ sls invoke -f helloWorld -d '{"body":"blah"}'          
{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v1.0! Your function executed successfully!\", \"input\": {\"body\": \"blah\"}}"
}
```

## Continuous Integration

We will use CirclCI for continuous integration, that will pull our latest code on commit, set up our environment, run tests and then deploy our app to AWS.

* Set up your account on CircleCI
* Configure a Github repo as a project
* Set up AWS credentials for the project
* Check in code to the repo
* CircleCI will trigger a build based on that commit

## Cleanup

Cleanup all functions and resources deployed to the AWS cloud.

```
$ sls remove

Serverless: Getting all objects in S3 bucket...
Serverless: Removing objects in S3 bucket...
Serverless: Removing Stack...
Serverless: Checking Stack removal progress...
...................
Serverless: Stack removal finished...
```
