import json
import logging
import urllib.request as request
import urllib.error as error

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    path = event['pathParameters']['path']
    title = event['queryStringParameters']['title']
    description = event['queryStringParameters']['description']
    
    api_url = f'https://api-nightly.relmak.com/api/merchant_page_initial_data/{path}?title={title}&description={description}'
    
    try:
        response = request.urlopen(api_url)
        response_data = response.read().decode('utf-8')
        json_data = json.loads(response_data)
        return {"statusCode": 200, "body": json.dumps(json_data)}
    except error.HTTPError as e:
        error_message = e.read().decode('utf-8')
        logger.error(f"Error calling API: {api_url}, status code: {e.code}, message: {error_message}")
        return {"statusCode": e.code, "body": json.dumps({"errorMessage": f"Error calling API: {error_message}"})}
    except error.URLError as e:
        logger.error("Error calling API: {}, reason: {}".format(api_url, e.reason))
        return {"statusCode": 500, "body": json.dumps({"errorMessage": "Error calling API."})}
    except Exception as e:
        logger.error("Unexpected error: {}".format(str(e)))
        return {"statusCode": 500, "body": json.dumps({"errorMessage": "Unexpected error occurred."})}
