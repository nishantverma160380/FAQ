=================================================================================================================================================================================
LocalStack
=================================================================================================================================================================================

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			|_
LocalStack on Docker	|
-------------------------

$ docker run --env DEBUG=1 --env DEFAULT_REGION=eu-west-1 -it -p 4567-4583:4567-4583 -p 8080:8080  localstack/localstack


=================================================================================================================================================================================

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			|_
DynamoDB Commands	|
-------------------------

The value for annotation attribute DynamoDBTable.tableName must be a constant expression

# When running Docker natively on Linux, you can access host services using the IP address of the docker0 interface. 
# From inside the container, this will be your default route.
# $ ip addr show docker0
# You may need to modify the iptables rules on your host to permit connections from Docker containers. 
# Something like this will do the trick:
# iptables -A INPUT -i docker0 -j ACCEPT
# Dont use localhost / 127.0.0.1
amazon.dynamodb.endpoint=http://172.17.0.1:4569/
amazon.dynamodb.region=local

To Display List of Tables

# When running Docker natively on Linux, you can access host services using the IP address of the docker0 interface. 
# From inside the container, this will be your default route.
# $ ip addr show docker0
# You may need to modify the iptables rules on your host to permit connections from Docker containers. 
# Something like this will do the trick:
# iptables -A INPUT -i docker0 -j ACCEPT
# Dont use localhost / 127.0.0.1


//From Configured AWS account
	aws dynamodb list-tables
//From configured local host
	aws dynamodb list-tables --endpoint-url http://172.17.0.1:4569

To Create Table :

aws dynamodb create-table \
    --table-name adapter-task-record \
    --attribute-definitions \
        AttributeName=adapter_task_id,AttributeType=S \
    --key-schema AttributeName=adapter_task_id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --region local \
    --endpoint-url http://172.17.0.1:4569


aws dynamodb create-table \
    --table-name adapter-task-record \
    --attribute-definitions \
        AttributeName=adapter_task_id,AttributeType=S \
    --key-schema AttributeName=adapter_task_id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --region eu-west-1 \
    --endpoint-url http://172.17.0.1:4569


aws dynamodb create-table \
	--table-name MusicCollection \
	--attribute-definitions \
		AttributeName=Artist,AttributeType=S \
		AttributeName=SongTitle,AttributeType=S \
	--key-schema AttributeName=Artist,KeyType=HASH \
		AttributeName=SongTitle,KeyType=RANGE \
	--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \

aws dynamodb create-table \
    --table-name dev-peacock-reference-data-record \
    --attribute-definitions \
        AttributeName=integration_id,AttributeType=S \
        AttributeName=task_operation,AttributeType=S \
    --key-schema AttributeName=integration_id,KeyType=HASH \
		AttributeName=task_operation,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --region local \
    --endpoint-url http://172.17.0.1:4569

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
aws dynamodb create-table \
    --table-name adapter-task-record \
    --attribute-definitions \
        AttributeName=adapter_task_id,AttributeType=S AttributeName=integration_id,AttributeType=S \
    --key-schema AttributeName=adapter_task_id,KeyType=HASH AttributeName=integration_id,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --region local \
    --endpoint-url http://172.17.0.1:4569

To Scan for items
//From Configured AWS account
	aws dynamodb scan --table-name record
//From configured local host
	aws dynamodb scan --table-name record --endpoint-url http://172.17.0.1:4569

To modify a table's provisioned throughput
	aws dynamodb update-table --table-name record --provisioned-throughput ReadCapacityUnits=10,WriteCapacityUnits=10

To Delete a table
//From Configured AWS account
	aws dynamodb delete-table --table-name record
//From configured local host
	aws dynamodb delete-table --table-name dev-peacock-adapter-task-record --endpoint-url http://172.17.0.1:4569

To delete an Iteam from table
	aws dynamodb delete-item --table-name adapter-task-record --key '{"adapter_task_id": {"S": "e1c385a9-4c12-4fac-8851-cdbc404a8fd8"}}' --endpoint-url http://172.17.0.1:4569

Information about the table, including the current status of the table, when it was created, the primary key schema, and any indexes on the table.
	aws dynamodb describe-table --table-name adapter-task-record --endpoint-url http://172.17.0.1:4569


AWS CLI insert value in the table. 
aws dynamodb put-item --table-name request-parameter-record --item '{"integration_id":{"S":"INT_101"}, "flow_parameter_name_values":{"L": [ {"name":"name", "href":"href"} ]}}' --region local --endpoint-url http://172.17.0.1:4569


AWS CLI can read JSON files and insert value in the table. 
////////
aws dynamodb put-item \
    --table-name dev-peacock-reference-data-record \
    --item file://reference-data-upload.json \
    --region local \
    --endpoint-url http://172.17.0.1:4569

aws dynamodb put-item \
    --table-name dev-peacock-reference-data-record \
    --item file://reference-data-extract.json \
    --region local \
    --endpoint-url http://172.17.0.1:4569

aws dynamodb put-item \
    --table-name dev-peacock-reference-data-record \
    --item file://reference-data-bip.json \
    --region local \
    --endpoint-url http://172.17.0.1:4569



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			|_
JAVA CODE		|
-------------------------

this.client = AmazonDynamoDBClientBuilder.standard().withEndpointConfiguration(new AwsClientBuilder.EndpointConfiguration("http://localhost:8000", "us-east-1")).build();

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
=================================================================================================================================================================================
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			|_
S3 Bucket		|
-------------------------

# When running Docker natively on Linux, you can access host services using the IP address of the docker0 interface. 
# From inside the container, this will be your default route.
# $ ip addr show docker0
# You may need to modify the iptables rules on your host to permit connections from Docker containers. 
# Something like this will do the trick:
# iptables -A INPUT -i docker0 -j ACCEPT
# Dont use localhost / 127.0.0.1

To Create an S3 bucket
	aws s3 mb s3://peacock-poc-hcm-extract --endpoint-url=http://172.17.0.1:4572 --region local 

To List all S3 buckets
	aws s3 ls --endpoint-url=http://172.17.0.1:4572

To list the contents of a bucket
	aws s3 ls s3://peacock-poc-hcm-extract --endpoint-url=http://172.17.0.1:4572/

To remove a bucket for s3
	aws --endpoint-url=http://172.17.0.1:4572 s3 rb s3://peacock-poc-hcm-extract

To copy files from s3 
	//To copy all contents for s3 bucket in current folder
	aws s3 cp --endpoint-url http://172.17.0.1:4572 s3://peacock-poc-hcm-extract/ ./ --recursive
	//To copy all contents for s3 bucket to an s3 folder created in current folder
	aws s3 cp --endpoint-url http://172.17.0.1:4572 s3://peacock-poc-hcm-extract/ ./s3/ --recursive
	//To copy all contents for FOLDER_NAME folder to an s3 folder
	aws s3 cp --endpoint-url http://172.17.0.1:4572 s3://peacock-poc-hcm-extract/FOLDER_NAME ./s3/ --recursive


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			|_
JAVA CODE		|
-------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
=================================================================================================================================================================================
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			|_
SSM System MAnager	|
-------------------------

Create a parameter:
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/HCM_ADPTER_TABLE" --value "adapter-task-record" --description "HCM Adapter Table Name" --type String --endpoint-url http://172.17.0.1:4583 

Get a Parameter:
aws ssm get-parameter --name "/PEACOCK/HCMADAPTER/ECS_CLUSTER_NAME" --endpoint-url http://172.17.0.1:4583


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			|_
JAVA CODE		|
-------------------------


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
=================================================================================================================================================================================

OPERATION=upload FILENAME=INT_TEST_PERSON-13082018025539.csv BUCKETNAME=peacock-poc-hcm-extract FILEARN=INT_TEST_PERSON-13082018025539
=================================================================================================================================================================================


docker run -it -p 4567-4583:4567-4583 -p 8080:8080  localstack/localstack


aws dynamodb create-table \
    --table-name dev-peacock-integration-task-record \
    --attribute-definitions \
        AttributeName=integration_task_uuid,AttributeType=S \
    --key-schema AttributeName=integration_task_uuid,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --region local \
    --endpoint-url http://172.17.0.1:4569
aws dynamodb create-table \
    --table-name dev-peacock-reference-data-record \
    --attribute-definitions \
        AttributeName=integration_id,AttributeType=S \
    --key-schema AttributeName=integration_id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --region local \
    --endpoint-url http://172.17.0.1:4569
aws dynamodb create-table \
    --table-name dev-peacock-runtime-reference-data-record \
    --attribute-definitions \
        AttributeName=runtime_reference_uuid,AttributeType=S \
    --key-schema AttributeName=runtime_reference_uuid,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --region local \
    --endpoint-url http://172.17.0.1:4569
aws s3 mb s3://peacock-poc-hcm-extract --endpoint-url=http://172.17.0.1:4572 --region local
aws s3 mb s3://mdev.peacock.people.extract.zeawpttbsz --endpoint-url=http://172.17.0.1:4572 --region local
aws s3 mb s3://mdev.peacock.people.upload.exgafhwvmu --endpoint-url=http://172.17.0.1:4572 --region local
aws --endpoint-url=http://localhost:4572 s3 cp ../Location.dat s3://mdev.peacock.people.upload.exgafhwvmu
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/ECS_CLUSTER_NAME" --value "peacock_ecs_cluster" --description "Peacock ECS Cluster Name" --type String --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/HCM_WS_USERNAME" --value "HCM_INTEGRATION_USER" --description "HCM Integration user" --type String  --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/HCM_WS_PASSWORD" --value "Welcome#123" --description "HCM Integration user password" --type String --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/HCM_EXTRACT_ENDPOINT" --value "https:\/\/eicg-dev1.fa.em2.oraclecloud.com:443\/hcmService\/FlowActionsService" --description "HCM Extract endpoint" --type String --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/HCM_HDL_ENDPOINT" --value "https:\/\/eicg-dev1.fa.em2.oraclecloud.com\/hcmCommonDataLoader\/HCMDataLoader" --description "HCM Extract endpoint" --type String --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/HCM_BIP_ENDPOINT" --value "https:\/\/eicg-dev1.fa.em2.oraclecloud.com:443\/xmlpserver/services\/v2\/ScheduleService" --description "HCM BIP endpoint" --type String --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/HCM_UCM_ENDPOINT" --value "https:\/\/eicg-dev1.fa.em2.oraclecloud.com\/idcws\/GenericSoapPort?WSDL" --description "HCM UCM endpoint" --type String --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/ECS_TASK_NAME" --value "peacock_ecs_task" --description "Peacock ECS Task Name" --type String --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/ECS_CONTAINER_NAME" --value "peacock_ecs_container" --description "Peacock ECS Container Name" --type String --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/HCM_ADPTER_EXTRACT_API_GW_EP" --value "https:\/\/drcaolzwdl.execute-api.eu-west-1.amazonaws.com\/poc\/extract" --description "HCM Adapter Extract API Gateway Endpoint" --type String --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/HCM_ADPTER_LOAD_API_GW_EP" --value "TODO-set endpoint" --description "HCM Adapter Load API Gateway Endpoint" --type String --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/HCM_EXTRACT_PEACOCK_S3" --value "peacock-poc-hcm-extract" --description "peacock hcm extract s3 bucket" --type String  --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/HCM_ADPTER_TABLE" --value "adapter-task-record" --description "HCM Adapter Table Name" --type String --endpoint-url http://172.17.0.1:4583
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/EXTRACT_BUCKET" --value "mdev.peacock.people.extract.zeawpttbsz" --description "mdev.peacock.people.extract.zeawpttbsz peacock hcm extract s3 bucket" --type String  --endpoint-url http://172.17.0.1:4583 
aws ssm put-parameter --name "/PEACOCK/HCMADAPTER/UPLOAD_BUCKET" --value "mdev.peacock.people.upload.exgafhwvmu" --description "mdev.peacock.people.upload.exgafhwvmu peacock hcm upload s3 bucket" --type String  --endpoint-url http://172.17.0.1:4583 
aws dynamodb put-item --table-name dev-peacock-reference-data-record --item file://reference-data-extract.json --region local --endpoint-url http://172.17.0.1:4569
aws dynamodb put-item --table-name dev-peacock-reference-data-record --item file://reference-data-upload.json --region local --endpoint-url http://172.17.0.1:4569
aws dynamodb put-item --table-name dev-peacock-reference-data-record --item file://reference-data-bip.json --region local --endpoint-url http://172.17.0.1:4569

aws dynamodb put-item --table-name dev-peacock-runtime-reference-data-record --item file://Extract_RUNTIME_Data.json --region local --endpoint-url http://172.17.0.1:4569
aws dynamodb put-item --table-name dev-peacock-integration-task-record --item file://Extract_INT_Data.json --region local --endpoint-url http://172.17.0.1:4569

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

   private final Map<String,String> vars;
    public EnvironmentVariableConfiguration(){
        vars = System.getenv();
        AWS_REGION_NAME = getVar("AWS_REGION_NAME");
        DYNAMO_ENDPOINT = getVar("DYNAMO_ENDPOINT");
    }
    private String getVar(String name){
        if(!vars.containsKey(name)){
            throw new RuntimeException("Missing environment variable " + name);
        }e
        return vars.get(name);
    }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	private Map<String, String> vars = System.getenv();
	public S3ClientImpl(@Value("${amazon.s3.endpoint}") String s3Endpoint, @Value("${amazon.s3.region}") String s3Region) {
		
		String S3_REGION_NAME = vars.get("S3_REGION_NAME");
		String S3_ENDPOINT = vars.get("S3_ENDPOINT");
	}


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

echo "export NAME='ENVY'" >> .bashrc
source .bashrc

/////////////////////////////////////////////////////////////////////


EXTRACT:
	submitFlow
	getFlowTaskInstanceStatus
	getIntegrationContentId
	genericSoapOperation


PARAMETER FOR EXTRACT:

{
    "extractId": "INT_TEST_PERSON",
    "providerLocation": "mdev.peacock.people.extract.zeawpttbsz/HCM/1234",
    "parameters": [
        {
            "paramName": "Effective Date" ,
            "paramValue": "2018-10-25"
        }
    ]
}


{
    "extractId": "INT_101",
    "providerLocation": "mdev.peacock.people.extract.zeawpttbsz/HCM/INT_101/a6a6a660-6aaa-666a-6a6a-6aa666a6aa6a",
    "parameters": [
        {
            "paramName": "Effective Date" ,
            "paramValue": "2018-10-25"
        },
	{
		"paramName": "PAYROLL" ,
		"paramValue": "300000030910485"
	},
	{
		"paramName": "PAY_PERIOD" ,
		"paramValue": "300000030910558"
	}
    ]
}


{
    "extractId": "INT_131",
    "providerLocation": "mdev.peacock.people.extract.zeawpttbsz/HCM/INT_131/a6a6a660-6aaa-666a-6a6a-6aa-666a6aa6a",
    "parameters": [
        {
            "paramName": "Effective Date" ,
            "paramValue": "2018-12-10"
        },
	{
		"paramName": "Changes only" ,
		"paramValue": "N"
	}
    ]
}

{ 
	"extractId": "CONSOLIDATED-FULL-EXTRACT", 
	"providerLocation": "mdev.peacock.people.extract.zeawpttbsz/HCM/CONSOLIDATED-FULL-EXTRACT/73a6542c-1223-484f-9206-1710858c848c", 
	"parameters": [ 
		{ 
			"paramName": "Effective Date", 
			"paramValue": "2018-11-07" 
		} 
	] 
}


PARAMETER FOR BIP:

{
    "extractId": "INT-TESTPER_BIP",
    "providerLocation": "mdev.peacock.people.extract.zeawpttbsz/HCM/INT_TESTPER_BIP/a6a6a660-6aaa-666a-6a6a-6aa666a6aa6a",
    "parameters": [
        {
            "paramName": "Effective Date" ,
            "paramValue": "2019-01-01"
        }
    ]
}


PARAMETER FOR UPLOAD:

{
	"uploadId": "INT_165", 
	"uploadFileName": [
		{
			"filename": "Bank.dat"
		},
		{
			"filename": "BankBranch.dat"
		}
	],
	"providerLocation": "mdev.peacock.people.upload.exgafhwvmu", 
	"parameters": [
		{
		"paramName": "fileHref", 
		"paramValue": "Location_test1.zip"
		}
	]
}



Start Soap UI 
  ./SoapUI-5.4.0/bin/soapui.sh
Or ./soapui.sh from SoapUI-5.4.0/bin/

Jenkins
systemctl status jenkins

public class HCMExtractConnectionConfiguration
	extractDefaultUri = "https://eicg-dev1.fa.em2.oraclecloud.com:4433/hcmService/FlowActionsService";


RetrieveExtractFomUCM ----	userMedata.put("x-amz-meta-integrationTaskUUID", integrationTaskRecord.getIntegrationTaskUUID());

RunTimeReferenceDataServiceImplTest

HCMIntegrationDBServiceTest


List<String> names = Arrays.asList(
	"/PEACOCK/DEV/HCMADAPTER/DB-INTEGRATION_TASK_RECORD",
	"/PEACOCK/DEV/HCMADAPTER/DB-RUNTIME_REFERENCE_DATA_RECORD",
	"/PEACOCK/DEV/DB-REFERENCE_DATA_RECORD",
	
	"/PEACOCK/DEV/HCMADAPTER/ECS_CONTAINER_NAME",
	"/PEACOCK/DEV/HCMADAPTER/ECS_TASK_NAME",
	"/PEACOCK/DEV/ECS_CLUSTER_NAME",
	
	"/PEACOCK/DEV/EXTRACT_BUCKET",
	"/PEACOCK/DEV/HCMADAPTER/HCM_ADPTER_EXTRACT_API_GW_EP",
	
	"/PEACOCK/DEV/HCMADAPTER/HCM_BIP_ENDPOINT",
	"/PEACOCK/DEV/HCMADAPTER/HCM_EXTRACT_ENDPOINT",
	"/PEACOCK/DEV/HCMADAPTER/HCM_UCM_ENDPOINT",
	"/PEACOCK/DEV/HCM_WS_PASSWORD",
	"/PEACOCK/DEV/HCM_WS_USERNAME",
	"/PEACOCK/DEV/HCMADAPTER/HCM_HDL_ENDPOINT",
	"/PEACOCK/DEV/APP_ADAPTER_STATIC_DEPENDENCY_TABLE",
	"/PEACOCK/DEV/APP_ADAPTER_TASK_RECORD_TABLE",
	"/PEACOCK/DEV/SFTP_PASSWD",
	"/PEACOCK/DEV/SFTP_PORT",
	"/PEACOCK/DEV/SFTP_SERVER",
	"/PEACOCK/DEV/SFTP_USR",
	"/PEACOCK/DEV/UPLOAD_BUCKET",
	"/PEACOCK/DEV/HCM_REST_SELF_URL"
);



<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v2="http://xmlns.oracle.com/oxp/service/v2">
   <soapenv:Header/>
   <soapenv:Body>
      <v2:getAllScheduledReportHistory>
         <v2:filter>
            <v2:jobId>38322</v2:jobId>
         </v2:filter>
         <v2:beginIdx>1</v2:beginIdx>
         <v2:userID>HCM_INTEGRATION_USER</v2:userID>
         <v2:password>Welcome#123</v2:password>
      </v2:getAllScheduledReportHistory>
   </soapenv:Body>
</soapenv:Envelope>



Python Project

make venv
make init




