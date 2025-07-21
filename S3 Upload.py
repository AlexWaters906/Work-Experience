import boto3

# The access credentials (for my AWS account) are located in a file called credentials located in the folder ~/.aws
# More info for setting AWS access credentials can be found here https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
# The access keys in my credentials file are for an "IAM User" that I've created in AWS and which I have granted access to S3s3 = boto3.resource("s3")


bucket = s3.Bucket("alexwbucket1")

filename = 'sample-payment.json'

obj = bucket.Object(filename)
obj.upload_file(filename)

for o in bucket.objects.all():
    print(f"\t{o.key}")
