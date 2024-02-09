import boto3
import botocore
import json
import base64

rekognition_client = boto3.client('rekognition', region_name="us-east-1")

def lambda_handler(event, context):
    try:
        # Check if the event contains the image bytes
        if 'body' not in event:
            return {
                'statusCode': 400,
                'body': json.dumps({"error": "Image bytes not found in the event body"})
            }

        # Get the image bytes from the event body
        base64_data = event['body']
        image_bytes = base64.b64decode(base64_data)
        labels, inappropriate_labels = detect_objects_and_moderate(image_bytes)

        if inappropriate_labels:
            return {
                'statusCode': 400,
                'body': json.dumps({"message": "Inappropriate content detected. Please upload another image to avoid a ban."})
            }
        else:
            return {
                'statusCode': 200,
                'body': json.dumps({"labels": labels})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
    
    
    
    
def detect_objects_and_moderate(image_bytes):
    # Use DetectModerationLabels API to identify potential inappropriate content
    response_moderation = rekognition_client.detect_moderation_labels(
        Image={'Bytes': image_bytes},
        MinConfidence=70
    )
    
    # Get detected moderation labels
    moderation_labels = response_moderation.get('ModerationLabels', [])

    # If no moderation labels are detected, use DetectLabels API to identify normal objects
    if not moderation_labels:
        response_labels = rekognition_client.detect_labels(
            Image={'Bytes': image_bytes},
            MaxLabels=5,
            MinConfidence=70
        )

        # Get detected labels
        labels = [{'Name': label['Name'], 'Confidence': label['Confidence']} for label in response_labels['Labels']]

        # Return normal labels and set contains_inappropriate to False
        # return labels, [], False
        return labels, []

    return [], moderation_labels




