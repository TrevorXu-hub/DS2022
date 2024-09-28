import boto3
import requests


bucket_name = 'bucketlab4'  
object_name = 'googe.png' 
expires_in = 604800 

response = requests.get('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')
if response.status_code == 200:
    with open('google.png', 'wb') as f:
        f.write(response.content)
    print(f"File '{'google.png'}' successfully downloaded from the internet.")
else:
    print("Failed to download the file.")
    exit()


s3 = boto3.client('s3', region_name='us-east-1')
bucket = 'bucketlab4'
local_file = 'google.png'

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = local_file,
    ACL = 'public-read',
)

try:
    presigned_url = s3.generate_presigned_url(
        'googlelab4',
        Params={'Bucket': bucketlab4, 'Key': google.png},
        ExpiresIn=expires_in
    )
    print(f"Presigned URL for the file (valid for 7 days): {presigned_url}")
except Exception as e:
    print(f"Failed to generate a presigned URL: {e}")
