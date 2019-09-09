import os
import boto3
import time

from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime, timedelta

REGION = os.environ.get('REGION', 'eu-west-1')
TOWER = 'people'
CREATED_INDEX = 'CreatedDateIndex'


def get_ssm_parameter(param_name: str) -> str:
    ssm = boto3.client(
        'ssm',
        region_name=REGION
    )
    return ssm.get_parameter(Name=param_name, WithDecryption=True)['Parameter']['Value']


def delete_record_from_response(response, table, primary_partition_key):
    for item in response['Items']:
        primary_partition_key_val = item[primary_partition_key]
        print(f"--{primary_partition_key} -- -- --       {item[primary_partition_key]}")
        table.delete_item(Key={primary_partition_key: primary_partition_key_val})


def query_table_for_records(table, index_key, records_to_keep_days):
    ttl_date = (datetime.now() - timedelta(days=records_to_keep_days)).date().isoformat()
    print(f'-----{table} ')
    print(f'-----{index_key} ')
    print(f'-----{ttl_date} ')
    response = table.query(
        # Add the name of the index you want to use in your query.
        IndexName=CREATED_INDEX,
        KeyConditionExpression=Key(index_key).eq(ttl_date)
    )
    print(response)


def delete_record_from_table(table, records_to_keep_days):
    print(f'Delete record from table starts from {table}')
    ttl_date = (datetime.now() - timedelta(days=records_to_keep_days)).date().isoformat()
    scan_limit = 5
    key_schema = table.key_schema
    for map_key_schema in key_schema:
        if map_key_schema['KeyType'] == 'HASH':
            primary_partition_key = map_key_schema['AttributeName']

    # filter_expression = Attr(attribute).lt(ttl_date)
    # no_of_record_deleted = 0
    # print(table.global_secondary_indexes)

    index_loading = True
    while index_loading:
        if not table.global_secondary_indexes:
            print('Waiting for index to backfill...')
            time.sleep(5)
            table.reload()
            continue
        for index in table.global_secondary_indexes:
            if index['IndexName'] == CREATED_INDEX:
                if index['IndexStatus'] == 'ACTIVE':
                    key_schema = index['KeySchema']
                    for map_key_schema in key_schema:
                        if map_key_schema['KeyType'] == 'HASH':
                            index_key = map_key_schema['AttributeName']
                            query_table_for_records(table, index_key, records_to_keep_days)
                    index_loading = False
                    break
                else:
                    print('Waiting for index to backfill...')
                    time.sleep(5)
                    table.reload()
                    break


def clean_dynamo_db():
    dynamodb = boto3.resource(
        'dynamodb',
        region_name=REGION
    )

    dynamodb_records_to_keep_days = 112
    integration_task_record = get_ssm_parameter(f'/PEACOCK/DEV/HCMADAPTER/DB-INTEGRATION_TASK_RECORD')
    runtime_reference_record = get_ssm_parameter(f'/PEACOCK/DEV/HCMADAPTER/DB-RUNTIME_REFERENCE_DATA_RECORD')
    app_adapter_task_record = get_ssm_parameter(f'/PEACOCK/DEV/APP_ADAPTER_TASK_RECORD_TABLE')

    # dynamodb_records_to_keep_days = int(get_ssm_parameter(f'/PEACOCK/{RUN_MODE}/JANITOR/DYNAMODB_TTL_DAYS'))
    # integration_task_record = get_ssm_parameter(f'/PEACOCK/{RUN_MODE}/HCMADAPTER/DB-INTEGRATION_TASK_RECORD')
    # runtime_reference_record = int(get_ssm_parameter(f'/PEACOCK/{RUN_MODE}/HCMADAPTER/DB-RUNTIME_REFERENCE_DATA_RECORD'))
    # app_adapter_task_record = int(get_ssm_parameter(f'/PEACOCK/{RUN_MODE}/APP_ADAPTER_TASK_RECORD_TABLE'))
    # dynamodb = dynamodb_resource()

    # delete_record_from_table(dynamodb.Table(integration_task_record), dynamodb_records_to_keep_days)
    # delete_record_from_table(dynamodb.Table(runtime_reference_record), dynamodb_records_to_keep_days)
    delete_record_from_table(dynamodb.Table(app_adapter_task_record), dynamodb_records_to_keep_days)


if __name__ == '__main__':
    clean_dynamo_db()
