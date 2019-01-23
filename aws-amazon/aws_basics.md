
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
  * Network Gateway
    - Private Network
  * Network with route tables
    - Route Table:- A route table contains a set of rules, called routes, that are used to determine where 
      network traffic is directed. Each subnet in your VPC must be associated with a route table; 
      the table controls the routing for the subnet.
  * Network access control list
    - NACL
  * Private network with AWS resources like - Amazon EC2 instances, Database, S3 and other.
    - AWS Resources
    
  * Network with specific IP address range.
    - IP address Range
  * Network with subnet
    - Subnetroup
