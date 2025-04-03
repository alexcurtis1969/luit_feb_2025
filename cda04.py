import boto3
import time
import secrets
import string
import botocore

# Configuration - Define AWS resources and their properties
AWS_REGION = 'us-east-1'  # AWS region where resources will be created
VPC_CIDR = '10.0.0.0/16'  # CIDR block for the VPC
PUBLIC_SUBNET1_CIDR = '10.0.1.0/24'  # CIDR block for public subnet 1
PUBLIC_SUBNET2_CIDR = '10.0.2.0/24'  # CIDR block for public subnet 2
PRIVATE_SUBNET1_CIDR = '10.0.3.0/24' # CIDR block for private subnet 1
PRIVATE_SUBNET2_CIDR = '10.0.4.0/24' # CIDR block for private subnet 2
PRIVATE_SUBNET3_CIDR = '10.0.5.0/24' # CIDR block for private subnet 3
KEY_NAME = 'LUIT_Key_01'  # Name of the EC2 key pair
INSTANCE_TYPE = 't2.micro' # EC2 instance type
RDS_INSTANCE_TYPE = 'db.t3.small' # RDS instance type
RDS_INSTANCE_IDENTIFIER = 'joomla-rds' # RDS instance identifier
DB_NAME = 'joomladb' # RDS database name
DB_USER = 'joomlauser' # RDS database user
DB_ENGINE = 'postgres' # RDS database engine
DB_ENGINE_VERSION = '17.2' # RDS database engine version
JOOMLA_SECURITY_GROUP_NAME = 'joomla-sg' # Security group for Joomla EC2 instance
RDS_SECURITY_GROUP_NAME = 'rds-sg' # Security group for RDS instance
JOOMLA_AMI = 'ami-084568db4383264d4' # AMI for Joomla EC2 instance
MYSQL_PORT = 5432 # PostgreSQL port
VPC_NAME = 'joomla-vpc' # Name of the VPC
IGW_NAME = 'joomla-igw' # Name of the Internet Gateway
PUBLIC_ROUTE_TABLE_NAME = 'joomla-public-route-table' # Name of the public route table
PRIVATE_ROUTE_TABLE_NAME = 'joomla-private-route-table' # Name of the private route table
PUBLIC_SUBNET1_NAME = 'joomla-public-subnet-1' # Name of public subnet 1
PUBLIC_SUBNET2_NAME = 'joomla-public-subnet-2' # Name of public subnet 2
PRIVATE_SUBNET1_NAME = 'joomla-private-subnet-1' # Name of private subnet 1
PRIVATE_SUBNET2_NAME = 'joomla-private-subnet-2' # Name of private subnet 2
PRIVATE_SUBNET3_NAME = 'joomla-private-subnet-3' # Name of private subnet 3
EC2_INSTANCE_NAME = 'joomla-ec2' # Name of the EC2 instance
DB_SUBNET_GROUP_NAME = 'joomla-rds-subnet-group' # Name of the RDS subnet group

PRIVATE_SUBNET1_AZ = AWS_REGION + 'a' # Availability Zone for private subnet 1
PRIVATE_SUBNET2_AZ = AWS_REGION + 'b' # Availability Zone for private subnet 2
PRIVATE_SUBNET3_AZ = AWS_REGION + 'c' # Availability Zone for private subnet 3

# Initialize Boto3 clients and resources
ec2 = boto3.resource('ec2', region_name=AWS_REGION) # EC2 resource
client = boto3.client('ec2', region_name=AWS_REGION) # EC2 client
rds = boto3.client('rds', region_name=AWS_REGION) # RDS client

def delete_all_resources():
    """Deletes all resources created by the script."""

    try:
        # 1. Delete RDS Instance
        print("Deleting RDS Instance...")
        rds.delete_db_instance(DBInstanceIdentifier=RDS_INSTANCE_IDENTIFIER, SkipFinalSnapshot=True) # Delete the RDS instance without creating a final snapshot
        waiter = rds.get_waiter('db_instance_deleted') # Wait for the RDS instance to be deleted
        waiter.wait(DBInstanceIdentifier=RDS_INSTANCE_IDENTIFIER)

        # 2. Delete RDS Subnet Group
        print("Deleting RDS Subnet Group...")
        rds.delete_db_subnet_group(DBSubnetGroupName=DB_SUBNET_GROUP_NAME) # Delete the RDS subnet group

    except rds.exceptions.DBInstanceNotFoundFault:
        print(f"RDS instance '{RDS_INSTANCE_IDENTIFIER}' not found.")
    except rds.exceptions.DBSubnetGroupNotFoundFault:
        print(f"RDS Subnet group '{DB_SUBNET_GROUP_NAME}' not found.")
    except Exception as e:
        print(f"Error deleting RDS resources: {e}")

    try:
        # 3. Terminate EC2 Instance
        print("Terminating EC2 Instance...")
        instances = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': [EC2_INSTANCE_NAME]}]) # Filter instances by name tag
        for instance in instances:
            instance.terminate() # Terminate the EC2 instance
            instance.wait_until_terminated() # Wait for the instance to terminate

        # 4. Delete Security Groups
        print("Deleting Security Groups...")
        security_groups = client.describe_security_groups(Filters=[{'Name': 'group-name', 'Values': [JOOMLA_SECURITY_GROUP_NAME, RDS_SECURITY_GROUP_NAME]}])['SecurityGroups'] # Describe security groups with specific names
        for sg in security_groups:
            client.delete_security_group(GroupId=sg['GroupId']) # Delete the security group

        # 5. Delete Subnets
        print("Deleting Subnets...")
        subnets = client.describe_subnets(Filters=[{'Name': 'tag:Name', 'Values': [PUBLIC_SUBNET1_NAME, PUBLIC_SUBNET2_NAME, PRIVATE_SUBNET1_NAME, PRIVATE_SUBNET2_NAME, PRIVATE_SUBNET3_NAME]}])['Subnets'] # Describe subnets with specific names
        for subnet in subnets:
            client.delete_subnet(SubnetId=subnet['SubnetId']) # Delete the subnet

        # 6. Delete Route Tables
        print("Deleting Route Tables...")
        route_tables = client.describe_route_tables(Filters=[{'Name': 'tag:Name', 'Values': [PUBLIC_ROUTE_TABLE_NAME, PRIVATE_ROUTE_TABLE_NAME]}])['RouteTables'] # Describe route tables with specific names
        for rt in route_tables:
            if not rt.get('Associations'): #do not delete the main routing table.
                client.delete_route_table(RouteTableId=rt['RouteTableId']) # Delete the route table

        # 7. Delete Internet Gateway
        print("Deleting Internet Gateway...")
        igws = client.describe_internet_gateways(Filters=[{'Name': 'tag:Name', 'Values': [IGW_NAME]}])['InternetGateways'] # Describe internet gateways with specific names
        for igw in igws:
            igw_id = igw['InternetGatewayId']
            vpc_id = client.describe_vpcs(Filters=[{'Name': 'tag:Name', 'Values': [VPC_NAME]}])['Vpcs'][0]['VpcId'] # Get the VPC ID
            attachments = igw.get('Attachments', [])
            if any(attachment['VpcId'] == vpc_id for attachment in attachments):
                client.detach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id) # Detach the internet gateway from the VPC
            route_tables = client.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])['RouteTables']
            for rt in route_tables:
                for route in rt.get('Routes', []):
                    if 'GatewayId' in route and route['GatewayId'] == igw_id:
                        client.delete_route(RouteTableId=rt['RouteTableId'], DestinationCidrBlock=route['DestinationCidrBlock']) # Delete routes associated with the internet gateway
            client.delete_internet_gateway(InternetGatewayId=igw_id) # Delete the internet gateway

        # 8. Delete VPC
        print("Deleting VPC...")
        vpcs = client.describe_vpcs(Filters=[{'Name': 'tag:Name', 'Values': [VPC_NAME]}])['Vpcs'] # Describe VPCs with specific names
        for vpc in vpcs:
            client.delete_vpc(VpcId=vpc['VpcId']) # Delete the VPC

    except Exception as e:
        print(f"Error deleting EC2/VPC resources: {e}")

def generate_password(length=16):
    """Generates a random password."""
    allowed_chars = string.ascii_letters + string.digits + "!#$%&*()+-.:;<=>?[]^_`{|}~"
    password = ''.join(secrets.choice(allowed_chars) for i in range(length))
    return password

def create_rds_instance_with_retry(rds, rds_instance_params, max_retries=5, delay=5):
    """Creates an RDS instance with retry logic."""
    retries = 0
    while retries < max_retries:
        try:
            rds_instance = rds.create_db_instance(**rds_instance_params) # Create the RDS instance
            return rds_instance
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'InvalidVPCNetworkStateFault':
                retries += 1
                print(f"RDS instance creation failed (attempt {retries}/{max_retries}): {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                raise  # Re-raise other errors

# Delete existing resources first
delete_all_resources()

db_password = generate_password() # Generate a random database password
print(f"Your database password is: {db_password}")

# 1. Set Up Networking
print("Setting up VPC...")
vpc = ec2.create_vpc(CidrBlock=VPC_CIDR) # Create the VPC
vpc.create_tags(Tags=[{'Key': 'Name', 'Value': 'joomla-vpc'}]) # Tag the VPC
vpc.wait_until_available() # Wait for the VPC to become available

print("Creating Internet Gateway...")
internet_gateway = ec2.create_internet_gateway() # Create the internet gateway
internet_gateway.create_tags(Tags=[{'Key': 'Name', 'Value': 'joomla-igw'}]) # Tag the internet gateway
vpc.attach_internet_gateway(InternetGatewayId=internet_gateway.id) # Attach the internet gateway to the VPC

print("Creating public subnets...")
public_subnet1 = vpc.create_subnet(CidrBlock=PUBLIC_SUBNET1_CIDR, AvailabilityZone=AWS_REGION + 'a') # Create public subnet 1
public_subnet1.create_tags(Tags=[{'Key': 'Name', 'Value': 'joomla-public-subnet-1'}]) # Tag public subnet 1
public_subnet2 = vpc.create_subnet(CidrBlock=PUBLIC_SUBNET2_CIDR, AvailabilityZone=AWS_REGION + 'b') # Create public subnet 2
public_subnet2.create_tags(Tags=[{'Key': 'Name', 'Value': 'joomla-public-subnet-2'}]) # Tag public subnet 2

print("Creating private subnets...")
private_subnet1 = vpc.create_subnet(CidrBlock=PRIVATE_SUBNET1_CIDR, AvailabilityZone=PRIVATE_SUBNET1_AZ) # Create private subnet 1
private_subnet1.create_tags(Tags=[{'Key': 'Name', 'Value': 'joomla-private-subnet-1'}]) # Tag private subnet 1
private_subnet2 = vpc.create_subnet(CidrBlock=PRIVATE_SUBNET2_CIDR, AvailabilityZone=PRIVATE_SUBNET2_AZ) # Create private subnet 2
private_subnet2.create_tags(Tags=[{'Key': 'Name', 'Value': 'joomla-private-subnet-2'}]) # Tag private subnet 2
private_subnet3 = vpc.create_subnet(CidrBlock=PRIVATE_SUBNET3_CIDR, AvailabilityZone=PRIVATE_SUBNET3_AZ) # Create private subnet 3
private_subnet3.create_tags(Tags=[{'Key': 'Name', 'Value': 'joomla-private-subnet-3'}]) # Tag private subnet 3

print("Creating public route table...")
public_route_table = vpc.create_route_table() # Create the public route table
public_route_table.create_tags(Tags=[{'Key': 'Name', 'Value': 'joomla-public-route-table'}]) # Tag the public route table
public_route = public_route_table.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internet_gateway.id) # Create a route to the internet gateway
public_route_table.associate_with_subnet(SubnetId=public_subnet1.id) # Associate public subnet 1 with the route table
public_route_table.associate_with_subnet(SubnetId=public_subnet2.id) # Associate public subnet 2 with the route table

print("Creating private route table...")
private_route_table = vpc.create_route_table() # Create the private route table
private_route_table.create_tags(Tags=[{'Key': 'Name', 'Value': 'joomla-private-route-table'}]) # Tag the private route table
private_route_table.associate_with_subnet(SubnetId=private_subnet1.id) # Associate private subnet 1 with the route table
private_route_table.associate_with_subnet(SubnetId=private_subnet2.id) # Associate private subnet 2 with the route table
private_route_table.associate_with_subnet(SubnetId=private_subnet3.id) # Associate private subnet 3 with the route table

# 2. Set Up the Web Tier
print("Creating Joomla security group...")
joomla_security_group = ec2.create_security_group(
    GroupName=JOOMLA_SECURITY_GROUP_NAME,
    Description='Security group for Joomla EC2 instance',
    VpcId=vpc.id