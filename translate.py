import datetime
import json
import boto3

translate = boto3.client('translate')
dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
    input_text = event['queryStringParameters']['input_text']

    response = translate.translate_text(
        Text=input_text,
        SourceLanguageCode='ja',
        TargetLanguageCode='en',
    )

    output_text = response.get('TranslatedText')

    dynamodb.put_item(
        TableName='translate-history',
        Item={
            'timestamp': {'S': datetime.datetime.now().strftime('%Y%m%d%H%M%S')},
            'input_text': {'S': input_text},
            'output_text': {'S': output_text}
        })

    return {
        'statusCode': 200,
        'body': json.dumps({
            'output_text': output_text
        }),
        'isBase64Encoded': False,
        'headers': {}
    }
