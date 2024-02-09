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
        # Retrieve form data from the event
        form_data = event
        name = form_data['Name']
        email = form_data['Email']
        category = form_data['Category']
        
        print("EMAIL", email)
        # Initialize the database connection
        connection = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)

        with connection.cursor() as cursor:
            # Check if the email already exists in the database
            cursor.execute("SELECT Id FROM NotificationSubscribers WHERE Email = %s", (email,))
            existing_subscriber = cursor.fetchone()

            if existing_subscriber:
                # Email already exists, update the name and category
                cursor.execute("UPDATE NotificationSubscribers SET Name = %s, Category = %s WHERE Email = %s",
                               (name, category, email))
            else:
                # Email does not exist, insert a new record
                cursor.execute("INSERT INTO NotificationSubscribers (Name, Email, Category) VALUES (%s, %s, %s)",
                               (name, email, category))

        # Commit the changes to the database
        connection.commit()

        # Subscribe the user's email to the SNS topic
        sns_client = boto3.client('sns', region_name='us-east-1')  
        response = sns_client.list_subscriptions_by_topic(TopicArn=sns_topic_arn)
        
        # Check if the email address is already subscribed
        subscriptions = response.get('Subscriptions', [])
        subBoolean = False
        for subscription in subscriptions:
            if subscription['Protocol'] == 'email' and subscription['Endpoint'] == email:
                print(f"The email address {email} is already subscribed.")
                subBoolean = True
                return {
                    'statusCode': 200,
                    'body': json.dumps({
                        "redirect_url": "index.html",
                        "message": {"category": "success", "text": "Subscription successful."}
                    })
                }
          
        if subBoolean == False:
            response = sns_client.subscribe(
                TopicArn=sns_topic_arn,
                Protocol='email',
                Endpoint=email
            )

        # Return a successful response
        return {
            'statusCode': 200,
            'body': json.dumps({
                "redirect_url": "index.html",
                "message": {"category": "success", "text": "Subscription successful."}
            })
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