import json
import pymysql
import os
import boto3
import base64
from botocore.exceptions import ClientError
import uuid
from io import BytesIO


# Environment variables would be set in your Lambda function's configuration
db_host = os.environ.get('RDS_HOST')
db_user = os.environ.get('RDS_USER')
db_password = os.environ.get('RDS_PASSWORD')
db_name = os.environ.get('RDS_DB_NAME')
s3_bucket_name = os.environ.get('S3_BUCKET_NAME')

def lambda_handler(event, context):
    # Connect to the database
    connection = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
    
    # Parse the JSON body from the event
    form_data = event
    food_item_data = form_data['FoodItem']
    
    # Generate a unique filename for the S3 object
    unique_filename = str(uuid.uuid4()) + "_" + food_item_data['Image']['FileName']
    
    # Decode the base64 image
    image_data = base64.b64decode(food_item_data['Image']['Base64'])
    
    image_fileobj = BytesIO(image_data)

    # Upload the image to S3
    try:
        s3_client = boto3.client('s3')
        folder_path = "assets/uploads/"
        s3_client.upload_fileobj(image_fileobj, s3_bucket_name, 
                          f"{folder_path}{unique_filename}", 
                          ExtraArgs={'ContentType': food_item_data['Image']['ContentType']})
                          
        public_access_url = f"https://{s3_bucket_name}.s3.amazonaws.com/assets/uploads/{unique_filename}"
    except ClientError as e:
        print(f"Failed to upload image to S3: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({"error": "Failed to upload image to S3"})
        }
    
    try:
        with connection.cursor() as cursor:
            # Insert the new attachment
            cursor.execute(
                "INSERT INTO Attachments (FileName, ContentType, FileSize, FilePath, PublicAccessURL) VALUES (%s, %s, %s, %s, %s)",
                (unique_filename, food_item_data['Image']['ContentType'], food_item_data['Image']['Size'], f"assets/uploads/{unique_filename}", public_access_url)
            )
            attachment_id = cursor.lastrowid
            
            # Insert the new food item
            cursor.execute(
                "INSERT INTO FoodItems (Name, Description, ExpiryDate, CategoryID, AttachmentID) VALUES (%s, %s, %s, %s, %s)",
                (food_item_data['Name'], food_item_data['Description'], food_item_data['ExpiryDate'], food_item_data['CategoryID'], attachment_id)
            )
            food_item_id = cursor.lastrowid
            
            # Insert the new donation
            cursor.execute(
                "INSERT INTO Donations (Status, MeetUpLocation, UserId, Username, FoodItemID) VALUES (%s, %s, %s, %s, %s)",
                ('ACTIVE', form_data['MeetUpLocation'], '211283E', 'Liu JiaJun', food_item_id)
            )
            
            # Commit the transaction
            connection.commit()
            
    finally:
        # Close the database connection
        connection.close()
    
    # Return a successful response
    return {
        'statusCode': 200,
        'body': json.dumps({
            "redirect_url": "index.html",
            "message": {"category": "success", "text": "Your donation has been added successfully"}
        })
    }
