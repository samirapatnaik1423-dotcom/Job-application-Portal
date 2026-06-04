import json
import boto3
from datetime import datetime
import uuid

# DynamoDB setup
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('JobApplications')


def lambda_handler(event, context):
    try:
        print("EVENT:", event)

        # -------------------------
        # Parse request body
        # -------------------------
        body = {}

        if event.get("body"):
            body = json.loads(event["body"])

        fullName = body.get("fullName")
        email = body.get("email")
        phoneNumber = body.get("phoneNumber")
        qualification = body.get("qualification", "")
        experience = body.get("experience", "")
        skills = body.get("skills", "")
        coverLetter = body.get("coverLetter", "")

        # -------------------------
        # Validation
        # -------------------------
        if not fullName or not email or not phoneNumber:
            return {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({
                    "message": "fullName, email, phoneNumber are required"
                })
            }

        # -------------------------
        # Create item
        # -------------------------
        applicationId = str(uuid.uuid4())
        appliedDate = datetime.utcnow().isoformat()

        item = {
            "applicationId": applicationId,
            "fullName": fullName,
            "email": email,
            "phoneNumber": phoneNumber,
            "qualification": qualification,
            "experience": experience,
            "skills": skills,
            "coverLetter": coverLetter,
            "appliedDate": appliedDate
        }

        # -------------------------
        # Save to DynamoDB
        # -------------------------
        table.put_item(Item=item)

        print("Saved to DynamoDB")

        # -------------------------
        # Success response
        # -------------------------
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({
                "message": "Application submitted successfully",
                "applicationId": applicationId,
                "appliedDate": appliedDate
            })
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "Internal server error",
                "error": str(e)
            })
        }