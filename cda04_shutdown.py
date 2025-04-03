import boto3
import time

# Configuration
AWS_REGION = 'us-east-1'
RDS_INSTANCE_IDENTIFIER = 'joomla-rds'
EC2_INSTANCE_NAME = 'joomla-ec2'
JOOMLA_SECURITY_GROUP_NAME = 'joomla-sg'
RDS_SECURITY_GROUP_NAME = 'rds-sg'
VPC_NAME = 'joomla-vpc'
IGW_NAME = 'joomla-igw'
PUBLIC_ROUTE_TABLE_NAME = 'joomla-public-route-table'
PRIVATE_ROUTE_TABLE_NAME = 'joomla-private-route-table'
PUBLIC_SUBNET1_NAME = 'joomla-public-subnet-1'
PUBLIC_SUBNET2_NAME = 'joomla-public-subnet-2'
PRIVATE_SUBNET1_NAME = 'joomla-private-subnet-1'
PRIVATE_SUBNET2_NAME = 'joomla-private-subnet-2'
PRIVATE_SUBNET3_NAME = 'joomla-private-subnet-3'
DB_SUBNET_GROUP_NAME = 'joomla-rds-subnet-group'

ec2 = boto3.resource('ec2', region_name=AWS_REGION)
client = boto3.client('ec2', region_name=AWS_REGION)
rds = boto3.client('rds', region_name=AWS_REGION)

def shutdown_all_resources():
    """Shuts down all resources created by the script."""

    try:
        # 1. Delete RDS Instance
        print("Deleting RDS Instance...")
        rds.delete_db_instance(DBInstanceIdentifier=RDS_INSTANCE_IDENTIFIER, SkipFinalSnapshot=True)
        waiter = rds.get_waiter('db_instance_deleted')
        waiter.wait(DBInstanceIdentifier=RDS_INSTANCE_IDENTIFIER)

        # 2. Delete RDS Subnet Group
        print("Deleting RDS Subnet Group...")
        rds.delete_db_subnet_group(DBSubnetGroupName=DB_SUBNET_GROUP_NAME)

    except rds.exceptions.DBInstanceNotFoundFault:
        print(f"RDS instance '{RDS_INSTANCE_IDENTIFIER}' not found.")
    except rds.exceptions.DBSubnetGroupNotFoundFault:
        print(f"RDS Subnet group '{DB_SUBNET_GROUP_NAME}' not found.")
    except Exception as e:
        print(f"Error deleting RDS resources: {e}")

    try:
        # 3. Terminate EC2 Instance
        print("Terminating EC2 Instance...")
        instances = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': [EC2_INSTANCE_NAME]}])
        for instance in instances:
            instance.terminate()
            instance.wait_until_terminated()

        # 4. Delete Security Groups
        print("Deleting Security Groups...")
        security_groups = client.describe_security_groups(Filters=[{'Name': 'group-name', 'Values': [JOOMLA_SECURITY_GROUP_NAME, RDS_SECURITY_GROUP_NAME]}])['SecurityGroups']
        for sg in security_groups:
            client.delete_security_group(GroupId=sg['GroupId'])

        # 5. Delete Subnets
        print("Deleting Subnets...")
        subnets = client.describe_subnets(Filters=[{'Name': 'tag:Name', 'Values': [PUBLIC_SUBNET1_NAME, PUBLIC_SUBNET2_NAME, PRIVATE_SUBNET1_NAME, PRIVATE_SUBNET2_NAME, PRIVATE_SUBNET3_NAME]}])['Subnets']
        for subnet in subnets:
            client.delete_subnet(SubnetId=subnet['SubnetId'])

        # 6. Delete Route Tables
        print("Deleting Route Tables...")
        route_tables = client.describe_route_tables(Filters=[{'Name': 'tag:Name', 'Values': [PUBLIC_ROUTE_TABLE_NAME, PRIVATE_ROUTE_TABLE_NAME]}])['RouteTables']
        for rt in route_tables:
            if not rt.get('Associations'): #do not delete the main routing table.
                client.delete_route_table(RouteTableId=rt['RouteTableId'])

        # 7. Delete Internet Gateway
        print("Deleting Internet Gateway...")
        igws = client.describe_internet_gateways(Filters=[{'Name': 'tag:Name', 'Values': [IGW_NAME]}])['InternetGateways']
        for igw in igws:
            igw_id = igw['InternetGatewayId']
            vpc_id = client.describe_vpcs(Filters=[{'Name': 'tag:Name', 'Values': [VPC_NAME]}])['Vpcs'][0]['VpcId']
            attachments = igw.get('Attachments', [])
            if any(attachment['VpcId'] == vpc_id for attachment in attachments):
                client.detach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
            route_tables = client.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])['RouteTables']
            for rt in route_tables:
                for route in rt.get('Routes', []):
                    if 'GatewayId' in route and route['GatewayId'] == igw_id:
                        client.delete_route(RouteTableId=rt['RouteTableId'], DestinationCidrBlock=route['DestinationCidrBlock'])
            client.delete_internet_gateway(InternetGatewayId=igw_id)

        # 8. Delete VPC
        print("Deleting VPC...")
        vpcs = client.describe_vpcs(Filters=[{'Name': 'tag:Name', 'Values': [VPC_NAME]}])['Vpcs']
        for vpc in vpcs:
            client.delete_vpc(VpcId=vpc['VpcId'])

    except Exception as e:
        print(f"Error deleting EC2/VPC resources: {e}")

# Call the shutdown function
shutdown_all_resources()

print("All resources have been shut down. Please remember to run the main creation script when you return.")