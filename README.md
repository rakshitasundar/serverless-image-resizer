# Serverless Image Resizer

## Project Overview

The Serverless Image Resizer was developed as part of my Cloud Computing Internship at EduTantr using Amazon Web Services (AWS).

The project automatically processes an image uploaded to Amazon S3 using an S3 event trigger and AWS Lambda. The image is resized using Python and Pillow, and the resized image is stored back in Amazon S3 inside the `resized/` location.

## Objectives

- Upload images to Amazon S3.
- Automatically trigger AWS Lambda when an image is uploaded.
- Process the image using Python and Pillow.
- Resize the image to a maximum dimension of 800 × 800 pixels.
- Store the resized image in the `resized/` location.
- Monitor Lambda execution using Amazon CloudWatch.

## AWS Services and Technologies Used

- Amazon S3
- AWS Lambda
- AWS IAM
- Amazon CloudWatch
- Python
- Pillow

## System Workflow

User → Input Image → Amazon S3 → S3 ObjectCreated Trigger → AWS Lambda → Python + Pillow → Resize Image → Resized Image → Amazon S3 → CloudWatch Logs

## Implementation

The Lambda function reads the image uploaded to the S3 bucket through the S3 event notification.

The image is retrieved from S3 and processed using Python and Pillow. The image is resized while maintaining its aspect ratio and the output is stored in the `resized/` location in the S3 bucket.

The Lambda function also skips files already stored inside the `resized/` location to avoid repeated processing.

## Testing

The system was tested by uploading an image to the S3 bucket and verifying that the resized image was automatically generated and stored in the `resized/` location.

Lambda execution was also verified through successful execution and Amazon CloudWatch logs.

## Result

The uploaded image was successfully processed by AWS Lambda and the resized image was generated and stored in the S3 `resized/` location.

## Internship

**Domain:** Cloud Computing  
**Organization:** EduTantr

## Author

**Rakshita S K S**
