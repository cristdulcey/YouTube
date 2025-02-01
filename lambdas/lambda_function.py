import json
from datetime import datetime
import requests

def lambda_handler(event, context):
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSD'
    date = datetime.now()
    try :
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            # TODO: send data to endpoint
            print(f'[{date}] - Request was successful')
        else:
            print(f'[{date}] - Request was not successful')
            return {
                'statusCode': response.status_code,
                'body': json.dumps(
                    {
                        'error': False,
                        'message': 'Service updated',
                        'date': f'{date}'
                    }
                )
            }

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
    except Exception as error:
        print(f'Error: {error}')
    return {
        'statusCode': response.status_code,
        'body': json.dumps(
            {
                'error': False,
                'message': 'Service updated',
                'date': f'{date}'
            }
        )
    }
