import boto3, json

client = boto3.client('apigateway', region_name='us-east-1')


api_id = '01mn5z193c'
parent_id = 'p3vmg2eti8'

donations = client.create_resource(
    restApiId=api_id,
    parentId=parent_id,
    pathPart='donations'
)
donations_resource_id = donations["id"]


donations_get_method = client.put_method(
    restApiId=api_id,
    resourceId=donations_resource_id,
    httpMethod='GET',
    authorizationType='NONE'
)

donation_getresponse = client.put_method_response(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': True,
        'method.response.header.Access-Control-Allow-Origin': True,
        'method.response.header.Access-Control-Allow-Methods': True
    },
    responseModels={
        'application/json': 'Empty'
    }
)

product_integration = client.put_integration(
    restApiId=api_id,
    resourceId=products_resource_id,
    httpMethod='GET',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)





print ("DONE")

