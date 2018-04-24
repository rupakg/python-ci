# Serverless app in Python for CI

A simple serverless Python app that showcases CI with Circle CI.

## Local

### Test Functions

```
$ sls invoke local -f helloWorld -d '{"body":"blah"}'

{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v1.0! Your function executed successfully!\", \"input\": {\"body\": \"blah\"}}"
}
```

### Run Tests

```
$ python -m unittest discover tests

..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Remote

### Deploy

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

### Test Functions

```
$ sls invoke -f helloWorld -d '{"body":"blah"}'          
{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v1.0! Your function executed successfully!\", \"input\": {\"body\": \"blah\"}}"
}
```

## CI


## Cleanup

```
$ sls remove

Serverless: Getting all objects in S3 bucket...
Serverless: Removing objects in S3 bucket...
Serverless: Removing Stack...
Serverless: Checking Stack removal progress...
...................
Serverless: Stack removal finished...
```
