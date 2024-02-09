import json
import pymysql
import os

# Environment variables would be set in your Lambda function's configuration
db_host = os.environ.get('RDS_HOST')
db_user = os.environ.get('RDS_USER')
db_password = os.environ.get('RDS_PASSWORD')
db_name = os.environ.get('RDS_DB_NAME')

def lambda_handler(event, context):
    # Initialize the database connection
    connection = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
    
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        # Execute the SQL query
        cursor.execute("SELECT * FROM FoodItemCategories")
        
        # Fetch all the rows in a list of dictionaries
        result = cursor.fetchall()

    # Make sure to close the database connection
    connection.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps(result),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    
# To move this code into a zip file and save it in a S3 Bucket
# By Following this commands:
# Ensure in the /aws 
# 1. zip get_categories_code.zip get_categories_package
# 2. aws s3 cp get_categories_code.zip  s3://assignmentlambdabucket

# To Create the Lambda Function
# python3 get_categories_wrapper.py

#Package
# pip install pymysql -t .
#cd path/to/your/lambda_function_package
#zip -r9 ../get_categories_code.zip .
# aws s3 cp ../get_categories_code.zip s3://assignmentlambdabucket/
