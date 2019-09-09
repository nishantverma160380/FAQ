

/PEACOCK/COEX/CUSTOMER_KEY_PRIV

/PEACOCK/COEX/FUSION_KEY_PUB


---------------------------------------------------------""-------------------------------------------------------------------------
Terraform:


make init  . .venv/bin/activate

. .venv/bin/activate
	
	Command prompt changes to :		(.venv) nishant@oem-HP-EliteBook-840-G3:~/project/peacock/interfaces/people-hcm-adapter$ 

make terrafile args='./terrafile -u hardikashar -p Akanksha1410'


Go to dev folder

terraform init -var-file=vars/dev.tfvars -backend-config=conf/dev.backend.conf

terraform workspace select dev


terraform plan -var-file=vars/dev.tfvars


terraform import aws_cloudwatch_log_group.main clg-euw1-ops-people-hcm-adapter-001

terraform import aws_cloudwatch_log_group.cloudwatch_log_group_task_trigger_lmb '/aws/lambda/lmb-euw1-ops-people-hcm-task-trigger-peacock-001'

terraform import aws_cloudwatch_log_group.cloudwatch_log_group_retry_lmb '/aws/lambda/lmb-euw1-ops-people-retry-integration-task-peacock-001'


Remove any resource from terraform

terraform state rm 'aws_cloudwatch_event_rule.every_day'


resource "aws_cloudwatch_log_group" "example" {
	name = "/aws/lambda/${var.lambda_function_name}"
	retention_in_days = 14 
}
---------------------------------------------------------""-------------------------------------------------------------------------




S3
-------------------------------------------------------------------------------------------------------------------------------------------

/<Integration ID>/
/HCM/<Integration ID>/<task id>/												/HCM/INT_101/<task id>/
/HCM/<Integration ID>/<task id>/reportA/										/HCM/INT_128/<task id>/reportA/
/HCM/<Integration ID>/<task id>/reportB/										/HCM/INT_128/<task id>/reportB/

/<Integration ID>/<Integration ID>_EPG/pending/									/INT_128/INT_128_EPG/pending/
/<Integration ID>/<Integration ID>_SAILPOINT/pending/							/INT_149/INT_149_SAILPOINT/pending/




EXTRACT

/HCM/<Integration ID>/<task id>/												/HCM/INT_101/<task id>/
/<Integration ID>/<date>/<task id>/processing/transformed						/INT_107/<date>/<task id>/processing/transformed
/<Integration ID>/<date>/<task id>/archive/transformed							/INT_107/<date>/<task id>/archive/transformed




UPLOAD
/<Integration ID>/<date>/<task id>/processing/transformed						/INT_107/<date>/<task id>/processing/transformed
/<Integration ID>/<date>/<task id>/processing/transformed/joiner/				/INT_178/<date>/<task id>/processing/transformed/joiner/
/<Integration ID>/<date>/<task id>/processing/transformed/leaver/				/INT_178/<date>/<task id>/processing/transformed/leaver/

/<Integration ID>/<date>/<task id>/archive/transformed							/INT_107/<date>/<task id>/archive/transformed
/<Integration ID>/<date>/<task id>/archive/transformed/joiner/					/INT_178/<date>/<task id>/archive/transformed/joiner/
/<Integration ID>/<date>/<task id>/archive/transformed/leaver/					/INT_178/<date>/<task id>/archive/transformed/leaver/

-------------------------------------------------------------------------------------------------------------------------------------------




Sample Request Body:

Extract:	
{  
   "extractId":"INT_101",
   "providerLocation":"msit.peacock.people.extract.jcukdstciv/HCM/INT_101/2b823788-d09e-4419-9e67-ad820c67812e",
   "parameters":[  
      {  
         "paramName":"Effective Date",
         "paramValue":"2019-05-10"
      },
      {  
         "paramName":"Start Date",
         "paramValue":"2019-05-10"
      },
      {  
         "paramName":"Payroll",
         "paramValue":"300000015324610"
      }
   ]
}

Upload:

{  
   "uploadId":"INT_165",
   "uploadFileName": [
   		{
   			         "filename":"testFile.txt"
   		}
   	],
   "providerLocation":"msit.peacock.people.upload.rclpymmbtj/INT_165/2019-08-02/e75db8af-2f69-4dc5-b4ab-d423ed559064/processing/transformed",
   "parameters":[  
      {  
         "paramName":"fileHref",
         "paramValue":"RUNTIME_AA"
      }
   ]
}


{  
   "uploadId":"INT_165",
   "uploadFileName": [
   		{
   			"filename":"INT165_bankwizard_corehr_20190529135829.zip"
   		}
   	],
   "providerLocation":"mdev.peacock.people.upload.exgafhwvmu/INT_165/2019-05-29/924cad7c-f9e7-4a25-a46c-f931171f14db/processing/transformed",
   "parameters":[  
      {  
         "paramName":"fileHref",
         "paramValue":"RUNTIME_AA"
      }
   ]
}
            
 
