import boto3

s3 = boto3.client("s3")

bucket_name = input("Enter Bucket Name : ")
file_path = input("Enter File Path : ")

try:
    s3.upload_file(file_path, bucket_name, file_path.split("\\")[-1])

    print("File uploaded successfully!")

    response = s3.list_objects_v2(Bucket=bucket_name)

    print("\nFiles in the bucket:")

    # Check if the bucket contains any objects
    if "Contents" in response:
        for obj in response["Contents"]:
            print(obj["Key"])
    else:
        print("Bucket is empty.")
except Exception as e:
    print("Upload failed.")
    print(e)
