import boto3
import os
from PIL import Image
from io import BytesIO
from urllib.parse import unquote_plus

s3 = boto3.client("s3")

def lambda_handler(event, context):

    for record in event["Records"]:

        bucket = record["s3"]["bucket"]["name"]
        key = unquote_plus(record["s3"]["object"]["key"])

        # Avoid resizing files already inside the resized folder
        if key.startswith("resized/"):
            continue

        # Get the image from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        image_data = response["Body"].read()

        # Open image
        image = Image.open(BytesIO(image_data))

        # Resize image
        image.thumbnail((800, 800))

        # Save resized image in memory
        output = BytesIO()
        image_format = image.format if image.format else "JPEG"

        if image_format.upper() == "JPEG":
            image.save(output, format="JPEG", quality=85)
        else:
            image.save(output, format=image_format)

        output.seek(0)

        # Create resized file
        filename = os.path.basename(key)
        resized_key = "resized/" + filename

        # Upload resized image
        s3.put_object(
            Bucket=bucket,
            Key=resized_key,
            Body=output,
            ContentType=response.get(
                "ContentType",
                "image/jpeg"
            )
        )

    return {
        "statusCode": 200,
        "body": "Image resized successfully"
    }