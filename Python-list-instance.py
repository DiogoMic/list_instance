import boto3

# Create an EC2 client
ec2_client = boto3.client('ec2')

# Get a list of all regions
regions = ec2_client.describe_regions()['Regions']

# Loop through each region and list instances
for region in regions:
    region_name = region['RegionName']
    print(f"Listing instances in region: {region_name}")
    ec2 = boto3.client('ec2', region_name=region_name)
    instances = ec2.describe_instances()

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_state = instance['State']['Name']
            instance_type = instance['InstanceType']
            instance_name = None
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
                    break
            print(f"Instance ID: {instance_id}, State: {instance_state}, Type: {instance_type}, Name: {instance_name}")

