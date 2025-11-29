import json
import boto3
import base64
from botocore.exceptions import ClientError

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    # --- 1) HANDLE CORS PRE-FLIGHT (OPTIONS) ---
    # HTTP API sends method in event["requestContext"]["http"]["method"]
    method = event.get("requestContext", {}).get("http", {}).get("method", "")

    if method.upper() == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': '*'
            },
            'body': json.dumps({'message': 'OK'})
        }

    # --- 2) NORMAL POST REQUEST ---
    try:
        body = json.loads(event.get("body") or "{}")
        image_b64 = body.get("image")

        if not image_b64:
            return cors_response(400, {"error": "No image provided (base64 expected in 'image' field)."})

        # Remove data URL prefix if present
        if ',' in image_b64:
            image_b64 = image_b64.split(',')[1]

        image_bytes = base64.b64decode(image_b64)

        response = rekognition.detect_labels(
            Image={'Bytes': image_bytes},
            MaxLabels=10,
            MinConfidence=70
        )

        labels = [
            {"Name": label["Name"], "Confidence": label["Confidence"]}
            for label in response.get("Labels", [])
        ]

        return cors_response(200, {"labels": labels})

    except ClientError as e:
        return cors_response(500, {"error": str(e)})
    except Exception as e:
        return cors_response(500, {"error": str(e)})

def cors_response(status, body):
    return {
        "statusCode": status,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }