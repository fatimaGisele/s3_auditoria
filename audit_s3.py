import boto3
from botocore.exceptions import ClientError

def audit_s3():
    s3 = boto3.client("s3")


    # session = boto3.session.Session()
    # print(boto3.Session().get_credentials())
    # creds = session.get_credentials()

    # if creds:
    #     frozen = creds.get_frozen_credentials()
    #     print("Access Key:", frozen.access_key)
    #     print("Secret Key:", frozen.secret_key)
    #     print("Token:", frozen.token)
    # else:
    #     print("No se encontraron credenciales")
    
    response = s3.list_buckets()
    buckets = response.get("Buckets",[])

    print("===AUDITORIA===\n")
    for b in buckets:
        name = b["Name"]
        print(f"bucket: {name}")

        try:
            version = s3.get_bucket_versioning(Bucket = name)
            status = version.get("Status","Disable")
        except ClientError:
            status = "Error"

        print(f"client status: {status}")

        try:
            lifecycle = s3.get_bucket_lifecycle_configuration(Bucket = name)
            rules = lifecycle.get("Rules", [])
            print(f"lifecycle rules: {len(rules)}")
        except ClientError:
            print("rules: NONE")


if __name__ == "__main__":
    audit_s3()