import boto3
import json
from botocore.exceptions import ClientError

# Initialize a boto3 client for AWS Lambda
lambda_client = boto3.client('lambda', region_name='us-east-1')

# Lambda function details
FUNCTION_NAME = 'subscribe_notification'
RUNTIME = 'python3.11'
ROLE_ARN = 'arn:aws:iam::701068225110:role/LabRole' # User the LearnerLab LabRole
HANDLER = 'subscribe_notification_code.lambda_handler'
S3_BUCKET = 'assignmentlambdabucket'
S3_KEY = 'subscribe_notification_code.zip'  # The zip file containing your Lambda function code

def create_lambda_function():
    try:
        response = lambda_client.create_function(
            FunctionName=FUNCTION_NAME,
            Runtime=RUNTIME,
            Role=ROLE_ARN,
            Handler=HANDLER,
            Code={
                'S3Bucket': S3_BUCKET,
                'S3Key': S3_KEY
            },
            Description='Lambda function to subscribe notification.',
            Environment={
                'Variables': {
                    'RDS_HOST': 'foodsharehub.c1wc4i62kq5k.us-east-1.rds.amazonaws.com',
                    'RDS_USER': 'cadadmin',
                    'RDS_PASSWORD': 'cadpassword',
                    'RDS_DB_NAME': 'foodsharehub',
                    'S3_BUCKET_NAME': 'assignmentfoodsharehubbucket',
                    'SNS_TOPIC_ARN': 'arn:aws:sns:us-east-1:701068225110:FoodShareHubSNS'
                }
            }
        )
        
        print(json.dumps(response, indent=4))
        return response
    except ClientError as e:
        print(f"An error occurred: {e}")
        return None

# Call the function to create the Lambda
create_lambda_response = create_lambda_function()
if create_lambda_response:
    print(f"Created Lambda function: {create_lambda_response['FunctionName']}")
else:
    print("Failed to create Lambda function")