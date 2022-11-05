import os
import boto3
import argparse
import configparser
from typing import Any, Dict

S3_BUCKET_NAME = "2022-10-ud-denp-cp-data"

config = configparser.ConfigParser()
config.read("dl.cfg")

os.environ["AWS_ACCESS_KEY_ID"] = config["AWS"]["AWS_ACCESS_KEY_ID"]
os.environ["AWS_SECRET_ACCESS_KEY"] = config["AWS"]["AWS_SECRET_ACCESS_KEY"]


def create_s3_bucket(bucket_name=S3_BUCKET_NAME):
    region = "us-west-2"
    s3 = boto3.resource("s3", region_name=region)
    try:
        bucket = s3.create_bucket(
            Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region}
        )
        print(f"Bucket {bucket} created")
        return bucket
    except botocore.exceptions.ClientError as e:
        if e.response != 404:
            return s3.Bucket(bucket_name)
        else:
            raise e


def delete_s3_bucket(bucket_name=S3_BUCKET_NAME):
    region = "us-west-2"
    s3 = boto3.resource("s3", region_name=region)
    try:
        bucket = s3.Bucket(bucket_name)
        bucket.objects.all().delete()
        bucket.delete()
        print(f"Bucket {bucket_name} deleted")
    except Exception as e:
        print(f"ERROR: {e}")


def get_args() -> Dict[str, Any]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--create-s3-bucket",
        action="store_true",
        dest="create",
        help="Create S3 bucket",
    )
    parser.add_argument(
        "-d",
        "--delete-s3-bucket",
        action="store_true",
        dest="delete",
        help="Delete S3 bucket",
    )
    try:
        arguments = vars(parser.parse_args())
        return arguments
    except Exception as e:
        parser.error(str(e))


def main():
    # Parse and get arguments
    args = get_args()

    # Create bucket
    if args.get("create"):
        create_s3_bucket()

    # Delete bucket
    if args.get("delete"):
        delete_s3_bucket()


if __name__ == "__main__":
    main()
