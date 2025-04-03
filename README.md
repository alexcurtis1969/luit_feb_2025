# Joomla Deployment on AWS with RDS PostgreSQL

This project automates the deployment of a Joomla website on AWS, utilizing EC2 for the application server and RDS PostgreSQL for the database.

## Architecture

The architecture consists of a two-tier setup:

* **Web Tier:** An EC2 instance running Apache, PHP, and Joomla.
* **Database Tier:** An RDS PostgreSQL instance for data storage.

## Prerequisites

* An AWS account with appropriate permissions.
* Boto3 library installed (`pip install boto3`).
* An EC2 Key Pair (`LUIT_Key_01` in this script) in the `us-east-1` region.
* Basic understanding of AWS services (VPC, EC2, RDS, Security Groups, Route Tables, etc.).

## Configuration

The script uses the following configuration variables:

* `AWS_REGION`: AWS region for deployment (default: `us-east-1`).
* `VPC_CIDR`: CIDR block for the VPC.
* `PUBLIC_SUBNET1_CIDR`, `PUBLIC_SUBNET2_CIDR`: CIDR blocks for public subnets.
* `PRIVATE_SUBNET1_CIDR`, `PRIVATE_SUBNET2_CIDR`, `PRIVATE_SUBNET3_CIDR`: CIDR blocks for private subnets.
* `KEY_NAME`: Name of the EC2 key pair.
* `INSTANCE_TYPE`: EC2 instance type.
* `RDS_INSTANCE_TYPE`: RDS instance type.
* `RDS_INSTANCE_IDENTIFIER`: RDS instance identifier.
* `DB_NAME`: RDS database name.
* `DB_USER`: RDS database user.
* `DB_ENGINE`: RDS database engine.
* `DB_ENGINE_VERSION`: RDS database engine version.
* `JOOMLA_SECURITY_GROUP_NAME`, `RDS_SECURITY_GROUP_NAME`: Security group names.
* `JOOMLA_AMI`: AMI for the Joomla EC2 instance.
* `MYSQL_PORT`: PostgreSQL port.
* `VPC_NAME`, `IGW_NAME`, `PUBLIC_ROUTE_TABLE_NAME`, `PRIVATE_ROUTE_TABLE_NAME`, `PUBLIC_SUBNET1_NAME`, `PUBLIC_SUBNET2_NAME`, `PRIVATE_SUBNET1_NAME`, `PRIVATE_SUBNET2_NAME`, `PRIVATE_SUBNET3_NAME`, `EC2_INSTANCE_NAME`, `DB_SUBNET_GROUP_NAME`: Resource names.

## Usage

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install Boto3:**
    ```bash
    pip install boto3
    ```

3.  **Run the Script:**
    ```bash
    python <script_name>.py
    ```

4.  **Follow the Output:**
    * The script will output the RDS database password and the public IP address of the EC2 instance.
    * SSH into the EC2 instance to install Apache, PHP, PostgreSQL client, and Joomla.
    * Use the provided RDS credentials during the Joomla installation.

5.  **Access Joomla:**
    * Open your web browser and navigate to the EC2 instance's public IP address.

6.  **Cleanup:**
    * The script includes a `delete_all_resources()` function to delete all created AWS resources.

## Script Functionality

The script performs the following actions:

1.  **Networking Setup:**
    * Creates a VPC, Internet Gateway, public and private subnets, and route tables.

2.  **Web Tier Setup:**
    * Creates a security group for the EC2 instance.
    * Launches an EC2 instance with the specified AMI and instance type.

3.  **Database Tier Setup:**
    * Creates a security group for the RDS instance.
    * Creates an RDS subnet group.
    * Launches an RDS PostgreSQL instance.

4.  **Output:**
    * Prints the EC2 instance's public IP address and RDS database credentials.

5.  **Manual Steps:**
    * Provides instructions for manually installing Joomla on the EC2 instance.

6.  **Cleanup Function:**
    * `delete_all_resources()` function will delete everything created by the script.

## Benefits of Two-Tier Architecture

* **Improved Security:** Isolates the database layer from public access.
* **Enhanced Scalability:** Allows independent scaling of the web and database tiers.
* **Better Performance:** Reduces network latency between the application and database.

## Important Notes

* Ensure that the EC2 key pair specified in `KEY_NAME` exists in your AWS account.
* The script deletes all resources before creating new ones.
* Manual steps are required to install and configure Joomla on the EC2 instance.
* Review the security group rules to ensure they meet your security requirements.

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues.