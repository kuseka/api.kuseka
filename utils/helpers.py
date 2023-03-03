import secrets
import string
import struct
import base64
import random
import boto3
import os
import json

# Create your models here.

def generate_hex_string(length=10):
    hex_chars = string.hexdigits[:-6]  # Get the characters that can appear in a hexadecimal string
    hex_string = ''.join(secrets.choice(hex_chars) for _ in range(length))  # Generate a random string of length `length`
    return hex_string

def generate_64bit_encoded_string():
    # Generate a 64-bit random number
    n = random.getrandbits(64)

    # Pack the number into a binary string using big-endian byte order
    binary_string = struct.pack('>Q', n)

    # Encode the binary string in base64 and replace + with #
    encoded_string = base64.b64encode(binary_string).decode('utf-8').replace('+', '#')

    return encoded_string


def s3_bucket_upload(file,subfolder="",):
    bucket_name = "kuseka"

    s3 = boto3.client("s3")

    assets = os.listdir("../img")
    count =0
    for asset in assets:
        s3.upload_file(
        Filename="../img/"+asset,
        Bucket=bucket_name,
        Key="images/api/"+asset,)
        count+=1
        print(f"Uploading completed {round(count/len(assets)*100)}")
        break