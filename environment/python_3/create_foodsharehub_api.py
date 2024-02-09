import boto3, json

client = boto3.client('apigateway', region_name='us-east-1')

response = client.create_rest_api(
    name='FoodShareHubApi',
    description='API For FoodShareHub.',
    minimumCompressionSize=123,
    endpointConfiguration={
        'types': [
            'REGIONAL',
        ]
    }
)
api_id = response["id"]

resources = client.get_resources(restApiId=api_id)
root_id = [resource for resource in resources["items"] if resource["path"] == "/"][0]["id"]

categories = client.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='categories'
)
categories_resource_id = categories["id"]


category_method = client.put_method(
    restApiId=api_id,
    resourceId=categories_resource_id,
    httpMethod='GET',
    authorizationType='NONE'
)

category_response = client.put_method_response(
    restApiId=api_id,
    resourceId=categories_resource_id,
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

category_integration = client.put_integration(
    restApiId=api_id,
    resourceId=categories_resource_id,
    httpMethod='GET',
    type='MOCK',
    requestTemplates={
        'application/json': '{"statusCode": 200}'
    }
)

category_integration_response = client.put_integration_response(
    restApiId=api_id,
    resourceId=categories_resource_id,
    httpMethod='GET',
    statusCode='200',
    responseTemplates={
        "application/json": json.dumps({
            "categories": [
                { "Id": "1", "Name": "Milks & Dairies" },
                { "Id": "2", "Name": "Fresh Fruits" },
                { "Id": "3", "Name": "Vegetables" },
                { "Id": "4", "Name": "Wine & Drinks" },
                { "Id": "5", "Name": "Baking Material" },
                { "Id": "6", "Name": "Pet Foods" },
                { "Id": "7", "Name": "Noodles & Rice" },
                { "Id": "8", "Name": "Snacks" },
                { "Id": "9", "Name": "Others" }
            ]
        })
    },
    responseParameters={
        'method.response.header.Access-Control-Allow-Headers': "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
        'method.response.header.Access-Control-Allow-Methods': "'GET'",
        'method.response.header.Access-Control-Allow-Origin': "'*'"
    }
)

print ("DONE")

