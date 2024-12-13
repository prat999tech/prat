import json
import logging
import boto3
from botocore.exceptions import ClientError

def get_upload_url(event):
    """Generates a presigned URL for uploading a .docx file to S3."""

    try:
        s3_client = boto3.client('s3', region_name=os.environ['AWS_REGION'])

        # Create a unique file name with random ID
        random_id = int(random.random() * 10000000)
        key = f"{random_id}.docx"

        # Set S3 parameters for the presigned URL
        s3_params = {
            'Bucket': os.environ['UploadBucket'],
            'Key': key,
            'ExpiresIn': 300,  # URL expiration in seconds
            'ContentType': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'ACL': 'public-read'  # Make uploaded object publicly readable
        }

        # Generate the presigned URL
        upload_url = s3_client.generate_presigned_url('putObject', Params=s3_params)

        # Construct the response
        response = {
            "statusCode": 200,
            "headers": {
                "Key": key
            },
            "body": json.dumps({"uploadURL": upload_url, "Key": key}),
            "isBase64Encoded": False
        }

        return response

    except ClientError as e:
        logging.error(e)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Failed to generate presigned URL"})
        }

def lambda_handler(event, context):
    """Main Lambda entry point."""

    return get_upload_url(event)
