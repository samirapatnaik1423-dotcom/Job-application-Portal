Job Application Portal (Serverless Web Application)
Project Overview

This project is a serverless Job Application Portal built using AWS services. Users can view job details and submit job applications through a web form. The system processes data using AWS Lambda and stores it in DynamoDB without using any traditional backend server.

Architecture

User → Nginx (VPS) → Frontend (HTML/CSS/JS) → API Gateway → AWS Lambda → DynamoDB

AWS Services Used

AWS Lambda (Backend logic)
Amazon API Gateway (REST API)
Amazon DynamoDB (Database)
Amazon CloudWatch (Logging)

Infrastructure Used

Linux VPS (AWS Lightsail / EC2)
Nginx Web Server
GitHub (Version Control)

Features

Display job details (static section)
Job application form
Form validation
Submit application via API
Store data in DynamoDB
Generate unique application ID
Timestamp for each submission

Database Structure (DynamoDB)

Table Name: JobApplications

Attributes:
applicationId (Primary Key)
fullName
email
phoneNumber
qualification
experience
skills
coverLetter
appliedDate

API Endpoint

POST /apply

Example:
https://your-api-id.execute-api.region.amazonaws.com/prod/apply

Sample Request
{
  "fullName": "John Doe",
  "email": "john@example.com",
  "phoneNumber": "9876543210",
  "qualification": "BTech",
  "experience": "2",
  "skills": "HTML, CSS, JS",
  "coverLetter": "I am interested in this role"
}
Sample Response
{
  "message": "Application submitted successfully",
  "applicationId": "a1b2c3d4",
  "appliedDate": "2026-06-03T10:00:00Z"
}
Frontend Technologies

HTML5
CSS3
JavaScript (Fetch API)

Security & Validation

Input validation in Lambda
Required fields check
CORS enabled in API Gateway

Future Improvements

Resume upload using AWS S3
Email notifications using SES
Admin dashboard for applications
Authentication system (Cognito)

Author

Behera Samira Patnaik
ECE, AITAM College
