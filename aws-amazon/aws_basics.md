
# AWS

## ECS - Elastic Container service

## VPC - Virtual Private Cloude
Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined. 
This virtual network closely resembles a traditional network that you'd operate in your own data center, 
with the benefits of using the scalable infrastructure of AWS.

VPCs and Subnets
A virtual private cloud (VPC) is a virtual network dedicated to your AWS account. 
It is logically isolated from other virtual networks in the AWS Cloud. 
You can launch your AWS resources, such as Amazon EC2 instances, into your VPC.
You can specify an IP address range for the VPC, add subnets, associate security groups, and configure route tables.

A subnet is a range of IP addresses in your VPC. You can launch AWS resources into a specified subnet. 
Use a public subnet for resources that must be connected to the internet, 
and a private subnet for resources that won't be connected to the internet.

  * VPC
    - Private Cloud
  * Subnet and Route Table
    - Subnetgroup
    - subnet has to be in one availibility zone
    - Full tolerence redundency and dependencies
    - Subnet always attached with a route table
    - Public Subnet - Route table attached to the subnet will be attached to an Internet Gateway
    - Private Subnet - Route table attached to the subnet with no Internet Gateway attached
      - Route Table for private subnet: 
        - New Route Table:
          - Create Route Table {Name-tag: name of the route table, VPC: VPC for the subnet}
          - Press: Yes, Create
        - Created subnet does not have any Internet Gateway Attached
        - To create a private subnet associate a subnet to the above created route table       
        - AsTsociate a subnet with created route table:
          - Select the route table created in the list of route table
          - Select "Subnet Associations" tab below
          - Click EDIT
          - Select a subnet which are going to be a private subnet.
          - Press: Save
        - If there is a route table with main: Yes
          - Any subnet which are not associated with any route table are by default associated with the main route table.    
  * Internet Gateway
    - Private Network
  * Network with route tables
    - Route Table:- A route table contains a set of rules, called routes, that are used to determine where 
      network traffic is directed. Each subnet in your VPC must be associated with a route table; 
      the table controls the routing for the subnet.
      - Create Route Table:
        - Create Route Table {Name-tag: name of the route table, VPC: VPC for the subnet}
        - Press: Yes, Create
          - Created route table will be available in the list of route tables
          - select the created route table
            - Select the "Route" tab below
            - A default entry is available which shows the destination IP's within the APC that a subnet can connect.
            - Click "Edit" button
              - A new button appeard below with label "Add another route"
              - Click the "Add another route", a new row will appear.
              - Enter: Destination, Target
                - In case of Internet Gateway:- Destination:0.0.0.0/0, Target: Internet_Gateway_ID
                - One VPC Peered to Specific Subnets:- Destination:Destination_IP, Target: VPC_ID
  * Network access control list
    - NACL
  * Private network with AWS resources like - Amazon EC2 instances, Database, S3 and other.
    - AWS Resources
    

