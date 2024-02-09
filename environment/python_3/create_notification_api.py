import boto3, json

client = boto3.client('apigateway', region_name='us-east-1')

# Integration Response is not included here, gonna make it link to lambda manually.

api_id = '01mn5z193c'
parent_id = 'p3vmg2eti8'

# Create the 'notification' resource
notification_resource_id = client.create_resource(
    restApiId=api_id,
    parentId=parent_id,
    pathPart='notification'
)["id"]

# Add the POST method to the 'notification' resource
post_method_response = client.put_method(
    restApiId=api_id,
    resourceId=notification_resource_id,
    httpMethod='POST',
    authorizationType='NONE'  # You might want to use "AWS_IAM" or another authorization type
)

# Set up the 200 response for the POST method
client.put_method_response(
    restApiId=api_id,
    resourceId=notification_resource_id,
    httpMethod='POST',
    statusCode='200',
    responseModels={
        'application/json': 'Empty'  # You might need to change or customize the model
    }
)

print ("DONE")

