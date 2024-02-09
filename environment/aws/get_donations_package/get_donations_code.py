import json
import pymysql
import os
from datetime import datetime

# Environment variables would be set in your Lambda function's configuration
db_host = os.environ.get('RDS_HOST')
db_user = os.environ.get('RDS_USER')
db_password = os.environ.get('RDS_PASSWORD')
db_name = os.environ.get('RDS_DB_NAME')

# Custom JSON encoder to handle datetime objects
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return str(obj)
        return super(DateTimeEncoder, self).default(obj)

def lambda_handler(event, context):
    try:
        # Initialize the database connection
        connection = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
    
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            # Execute the SQL query to fetch active donations along with specific fields for Donations, FoodItems, Attachments, and Categories
            cursor.execute("""
                SELECT D.Id AS DonationId, D.Status, D.CreatedDate, D.UpdatedDate, D.MeetUpLocation,
                       D.UserId, D.Username,
                       F.Id AS FoodItemId, F.Name AS FoodItemName, F.Description AS FoodItemDescription, F.CategoryID, F.ExpiryDate,
                       A.Id AS AttachmentId, A.FileName, A.ContentType, A.FileSize, A.FilePath, A.PublicAccessURL,
                       C.Id AS CategoryId, C.Name AS CategoryName
                FROM Donations D
                INNER JOIN FoodItems F ON D.FoodItemID = F.ID
                INNER JOIN Attachments A ON F.AttachmentID = A.ID
                INNER JOIN FoodItemCategories C ON F.CategoryID = C.ID
                WHERE D.Status = 'ACTIVE'
            """)

            # Fetch all the rows in a list of dictionaries
            active_donations = cursor.fetchall()

        # Transform the data into the desired structure
        transformed_data = []
        for donation in active_donations:
            transformed_donation = {
                "Id": donation["DonationId"],
                "Status": donation["Status"],
                "CreatedDate": str(donation["CreatedDate"]),
                "UpdatedDate": str(donation["UpdatedDate"]),
                "MeetUpLocation": donation["MeetUpLocation"],
                "UserId": donation["UserId"],
                "Username": donation["Username"],
                "FoodItem": {
                    "Id": donation["FoodItemId"],
                    "Name": donation["FoodItemName"],
                    "Description": donation["FoodItemDescription"],
                    "CategoryID": donation["CategoryID"],
                    "ExpiryDate": str(donation["ExpiryDate"]),
                    "Attachment": {
                        "Id": donation["AttachmentId"],
                        "FileName": donation["FileName"],
                        "ContentType": donation["ContentType"],
                        "FileSize": donation["FileSize"],
                        "FilePath": donation["FilePath"],
                        "PublicAccessURL": donation["PublicAccessURL"]
                    },
                    "Category": {
                        "Id": donation["CategoryId"],
                        "Name": donation["CategoryName"]
                    }
                }
            }
            transformed_data.append(transformed_donation)

        # Serialize the transformed data to JSON using the custom encoder
        json_data = json.dumps(transformed_data, cls=DateTimeEncoder)

        # Return a successful response with the serialized JSON data
        return {
            'statusCode': 200,
            'body': json_data,
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
