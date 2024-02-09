{"filter":false,"title":"get_donations_code.py","tooltip":"/aws/get_donations_package/get_donations_code.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":53,"column":0},"action":"insert","lines":["import json","import pymysql","import os","from aws_lambda_powertools import Logger","","# Environment variables would be set in your Lambda function's configuration","db_host = os.environ.get('RDS_HOST')","db_user = os.environ.get('RDS_USER')","db_password = os.environ.get('RDS_PASSWORD')","db_name = os.environ.get('RDS_DB_NAME')","","logger = Logger()","","def lambda_handler(event, context):","    # Initialize the database connection","    connection = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)","    ","    try:","        with connection.cursor(pymysql.cursors.DictCursor) as cursor:","            # Execute the SQL query to fetch active donations along with FoodItem and Attachment data","            cursor.execute(\"\"\"","                SELECT D.*, F.*, A.*","                FROM Donations D","                INNER JOIN FoodItems F ON D.FoodItemID = F.ID","                INNER JOIN Attachments A ON F.AttachmentID = A.ID","                WHERE D.Status = 'ACTIVE'","            \"\"\")","            ","            # Fetch all the rows in a list of dictionaries","            active_donations = cursor.fetchall()","            ","            # Log the retrieved active donations","            logger.info(f\"Retrieved {len(active_donations)} active donations with FoodItem and Attachment data from the database\")","    ","    except Exception as e:","        logger.error(f\"Error retrieving active donations: {e}\")","        return {","            'statusCode': 500,","            'body': json.dumps({\"error\": \"Failed to retrieve active donations\"})","        }","    finally:","        # Make sure to close the database connection","        connection.close()","    ","    # Return a successful response with the retrieved active donations as JSON","    return {","        'statusCode': 200,","        'body': json.dumps(active_donations),","        'headers': {","            'Content-Type': 'application/json',","            'Access-Control-Allow-Origin': '*'","        }","    }",""],"id":2}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["logger = Logger()",""],"id":3}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["from aws_lambda_powertools import Logger",""],"id":4}],[{"start":{"row":29,"column":0},"end":{"row":30,"column":0},"action":"remove","lines":["            # Log the retrieved active donations",""],"id":5}],[{"start":{"row":29,"column":0},"end":{"row":30,"column":4},"action":"remove","lines":["            logger.info(f\"Retrieved {len(active_donations)} active donations with FoodItem and Attachment data from the database\")","    "],"id":6}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"remove","lines":["        logger.error(f\"Error retrieving active donations: {e}\")",""],"id":7}],[{"start":{"row":0,"column":0},"end":{"row":48,"column":0},"action":"remove","lines":["import json","import pymysql","import os","","# Environment variables would be set in your Lambda function's configuration","db_host = os.environ.get('RDS_HOST')","db_user = os.environ.get('RDS_USER')","db_password = os.environ.get('RDS_PASSWORD')","db_name = os.environ.get('RDS_DB_NAME')","","","def lambda_handler(event, context):","    # Initialize the database connection","    connection = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)","    ","    try:","        with connection.cursor(pymysql.cursors.DictCursor) as cursor:","            # Execute the SQL query to fetch active donations along with FoodItem and Attachment data","            cursor.execute(\"\"\"","                SELECT D.*, F.*, A.*","                FROM Donations D","                INNER JOIN FoodItems F ON D.FoodItemID = F.ID","                INNER JOIN Attachments A ON F.AttachmentID = A.ID","                WHERE D.Status = 'ACTIVE'","            \"\"\")","            ","            # Fetch all the rows in a list of dictionaries","            active_donations = cursor.fetchall()","            ","","    except Exception as e:","        return {","            'statusCode': 500,","            'body': json.dumps({\"error\": \"Failed to retrieve active donations\"})","        }","    finally:","        # Make sure to close the database connection","        connection.close()","    ","    # Return a successful response with the retrieved active donations as JSON","    return {","        'statusCode': 200,","        'body': json.dumps(active_donations),","        'headers': {","            'Content-Type': 'application/json',","            'Access-Control-Allow-Origin': '*'","        }","    }",""],"id":8},{"start":{"row":0,"column":0},"end":{"row":63,"column":0},"action":"insert","lines":["import json","import pymysql","import os","from datetime import datetime","","# Environment variables would be set in your Lambda function's configuration","db_host = os.environ.get('RDS_HOST')","db_user = os.environ.get('RDS_USER')","db_password = os.environ.get('RDS_PASSWORD')","db_name = os.environ.get('RDS_DB_NAME')","","# Custom JSON encoder to handle datetime objects","class DateTimeEncoder(json.JSONEncoder):","    def default(self, obj):","        if isinstance(obj, datetime):","            return str(obj)","        return super(DateTimeEncoder, self).default(obj)","","def lambda_handler(event, context):","    try:","        # Initialize the database connection","        connection = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)","    ","        with connection.cursor(pymysql.cursors.DictCursor) as cursor:","            # Execute the SQL query to fetch active donations along with FoodItem and Attachment data","            cursor.execute(\"\"\"","                SELECT D.*, F.*, A.*","                FROM Donations D","                INNER JOIN FoodItems F ON D.FoodItemID = F.ID","                INNER JOIN Attachments A ON F.AttachmentID = A.ID","                WHERE D.Status = 'ACTIVE'","            \"\"\")","","            # Fetch all the rows in a list of dictionaries","            active_donations = cursor.fetchall()","","        # Serialize the data to JSON using the custom encoder","        json_data = json.dumps(active_donations, cls=DateTimeEncoder)","","        # Return a successful response with the serialized JSON data","        return {","            'statusCode': 200,","            'body': json_data,","            'headers': {","                'Content-Type': 'application/json',","                'Access-Control-Allow-Origin': '*'","            }","        }","    except Exception as e:","        # Handle exceptions and return a JSON error response","        error_message = str(e)","        return {","            'statusCode': 500,","            'body': json.dumps({\"error\": error_message}),","            'headers': {","                'Content-Type': 'application/json',","                'Access-Control-Allow-Origin': '*'","            }","        }","    finally:","        # Make sure to close the database connection","        if 'connection' in locals() and connection is not None:","            connection.close()",""]}],[{"start":{"row":0,"column":0},"end":{"row":63,"column":0},"action":"remove","lines":["import json","import pymysql","import os","from datetime import datetime","","# Environment variables would be set in your Lambda function's configuration","db_host = os.environ.get('RDS_HOST')","db_user = os.environ.get('RDS_USER')","db_password = os.environ.get('RDS_PASSWORD')","db_name = os.environ.get('RDS_DB_NAME')","","# Custom JSON encoder to handle datetime objects","class DateTimeEncoder(json.JSONEncoder):","    def default(self, obj):","        if isinstance(obj, datetime):","            return str(obj)","        return super(DateTimeEncoder, self).default(obj)","","def lambda_handler(event, context):","    try:","        # Initialize the database connection","        connection = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)","    ","        with connection.cursor(pymysql.cursors.DictCursor) as cursor:","            # Execute the SQL query to fetch active donations along with FoodItem and Attachment data","            cursor.execute(\"\"\"","                SELECT D.*, F.*, A.*","                FROM Donations D","                INNER JOIN FoodItems F ON D.FoodItemID = F.ID","                INNER JOIN Attachments A ON F.AttachmentID = A.ID","                WHERE D.Status = 'ACTIVE'","            \"\"\")","","            # Fetch all the rows in a list of dictionaries","            active_donations = cursor.fetchall()","","        # Serialize the data to JSON using the custom encoder","        json_data = json.dumps(active_donations, cls=DateTimeEncoder)","","        # Return a successful response with the serialized JSON data","        return {","            'statusCode': 200,","            'body': json_data,","            'headers': {","                'Content-Type': 'application/json',","                'Access-Control-Allow-Origin': '*'","            }","        }","    except Exception as e:","        # Handle exceptions and return a JSON error response","        error_message = str(e)","        return {","            'statusCode': 500,","            'body': json.dumps({\"error\": error_message}),","            'headers': {","                'Content-Type': 'application/json',","                'Access-Control-Allow-Origin': '*'","            }","        }","    finally:","        # Make sure to close the database connection","        if 'connection' in locals() and connection is not None:","            connection.close()",""],"id":9}],[{"start":{"row":0,"column":0},"end":{"row":101,"column":0},"action":"insert","lines":["import json","import pymysql","import os","from datetime import datetime","","# Environment variables would be set in your Lambda function's configuration","db_host = os.environ.get('RDS_HOST')","db_user = os.environ.get('RDS_USER')","db_password = os.environ.get('RDS_PASSWORD')","db_name = os.environ.get('RDS_DB_NAME')","","# Custom JSON encoder to handle datetime objects","class DateTimeEncoder(json.JSONEncoder):","    def default(self, obj):","        if isinstance(obj, datetime):","            return str(obj)","        return super(DateTimeEncoder, self).default(obj)","","def lambda_handler(event, context):","    try:","        # Initialize the database connection","        connection = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)","    ","        with connection.cursor(pymysql.cursors.DictCursor) as cursor:","            # Execute the SQL query to fetch active donations along with specific fields for Donations, FoodItems, Attachments, and Categories","            cursor.execute(\"\"\"","                SELECT D.Id AS DonationId, D.Status, D.CreatedDate, D.UpdatedDate, D.MeetUpLocation,","                       D.UserId, D.Username,","                       F.Id AS FoodItemId, F.Name AS FoodItemName, F.Description AS FoodItemDescription, F.CategoryID, F.ExpiryDate,","                       A.Id AS AttachmentId, A.FileName, A.ContentType, A.FileSize, A.FilePath, A.PublicAccessURL,","                       C.Id AS CategoryId, C.Name AS CategoryName","                FROM Donations D","                INNER JOIN FoodItems F ON D.FoodItemID = F.ID","                INNER JOIN Attachments A ON F.AttachmentID = A.ID","                INNER JOIN FoodItemCategories C ON F.CategoryID = C.ID","                WHERE D.Status = 'ACTIVE'","            \"\"\")","","            # Fetch all the rows in a list of dictionaries","            active_donations = cursor.fetchall()","","        # Transform the data into the desired structure","        transformed_data = []","        for donation in active_donations:","            transformed_donation = {","                \"Id\": donation[\"DonationId\"],","                \"Status\": donation[\"Status\"],","                \"CreatedDate\": str(donation[\"CreatedDate\"]),","                \"UpdatedDate\": str(donation[\"UpdatedDate\"]),","                \"MeetUpLocation\": donation[\"MeetUpLocation\"],","                \"UserId\": donation[\"UserId\"],","                \"Username\": donation[\"Username\"],","                \"FoodItem\": {","                    \"Id\": donation[\"FoodItemId\"],","                    \"Name\": donation[\"FoodItemName\"],","                    \"Description\": donation[\"FoodItemDescription\"],","                    \"CategoryID\": donation[\"CategoryID\"],","                    \"ExpiryDate\": str(donation[\"ExpiryDate\"]),","                    \"Attachment\": {","                        \"Id\": donation[\"AttachmentId\"],","                        \"FileName\": donation[\"FileName\"],","                        \"ContentType\": donation[\"ContentType\"],","                        \"FileSize\": donation[\"FileSize\"],","                        \"FilePath\": donation[\"FilePath\"],","                        \"PublicAccessURL\": donation[\"PublicAccessURL\"]","                    },","                    \"Category\": {","                        \"Id\": donation[\"CategoryId\"],","                        \"Name\": donation[\"CategoryName\"]","                    }","                }","            }","            transformed_data.append(transformed_donation)","","        # Serialize the transformed data to JSON using the custom encoder","        json_data = json.dumps(transformed_data, cls=DateTimeEncoder)","","        # Return a successful response with the serialized JSON data","        return {","            'statusCode': 200,","            'body': json_data,","            'headers': {","                'Content-Type': 'application/json',","                'Access-Control-Allow-Origin': '*'","            }","        }","    except Exception as e:","        # Handle exceptions and return a JSON error response","        error_message = str(e)","        return {","            'statusCode': 500,","            'body': json.dumps({\"error\": error_message}),","            'headers': {","                'Content-Type': 'application/json',","                'Access-Control-Allow-Origin': '*'","            }","        }","    finally:","        # Make sure to close the database connection","        if 'connection' in locals() and connection is not None:","            connection.close()",""],"id":10}]]},"ace":{"folds":[],"scrolltop":901,"scrollleft":0,"selection":{"start":{"row":101,"column":0},"end":{"row":101,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":63,"state":"start","mode":"ace/mode/python"}},"timestamp":1707139458153,"hash":"f16e9f0a614846a53785d2132d7d2ce6d86d4d32"}