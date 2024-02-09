import json
import pymysql
import os
import boto3

# Environment variables would be set in your Lambda function's configuration
db_host = os.environ.get('RDS_HOST')
db_user = os.environ.get('RDS_USER')
db_password = os.environ.get('RDS_PASSWORD')
db_name = os.environ.get('RDS_DB_NAME')
sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')

def lambda_handler(event, context):
    try:
        # Initialize the database connection
        connection = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
        
        print("EVENT", event)
        category = event['Category']
        with connection.cursor() as cursor:
            # Query users whose selected category matches the category value
            cursor.execute("SELECT Email FROM NotificationSubscribers WHERE Category = %s OR Category = 'All Categories'", (category,))
            matching_users = cursor.fetchall()

        # Initialize the SNS client
        sns_client = boto3.client('sns')

        for user in matching_users:
            user_email = user[0]
            print("user_email", user_email)
            message = "We've discovered a new item in your preferred category! Please explore it on Food Share Hub."
            
            # Publish the message to the specified SNS topic
            sns_client.publish(
                Message=message,
                Subject='New Item Found in Your Preferred Category: ' + category,
                TopicArn=sns_topic_arn,
            )

        # Return a successful response
        return {
            'statusCode': 200,
            'body': json.dumps({"message": "Notifications sent successfully."}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    except Exception as e:
        # Handle exceptions and return a JSON error response
        error_message = str(e)
        return {
            'statusCode': 500,
            'body': json.dumps({"error": error_message}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    finally:
        # Make sure to close the database connection
        if 'connection' in locals() and connection is not None:
            connection.close()

