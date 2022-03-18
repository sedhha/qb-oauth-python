from qbClient import AuthClient
import constants as cfg
import requests
from jsonDumper import dumpDataToJson,readJsonByKey,readWholeJson
from datetime import datetime
auth_client = AuthClient(**cfg.client_secrets)

# Checks if the access token is expired.
# Max expiry time is 3600s hence must be less than that.
refreshCheckFrequency = 10 #Renew access token every 300s

def getCustomerData(accessToken):
    #making Request
    base_url = 'https://sandbox-quickbooks.api.intuit.com'
    url = '{0}/v3/company/{1}/companyinfo/{1}'.format(base_url, cfg.qBData["realm_id"])
    auth_header = 'Bearer {0}'.format(accessToken)
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    print(response.json())
    return response

def refresh_token():
    currentTs = int(datetime.now().timestamp())
    data = readWholeJson('refresh-credentials.json')
    if 'expires_in' not in data or 'refresh_token' not in data:
        raise ValueError('No expiry time/refresh_token found in refresh-credentials.json. Invalid Json or Json Path. Kindly Retry')
    
    refreshCredentials = data['expires_in']
    if refreshCheckFrequency < 0 or refreshCheckFrequency > 3600:
        raise ValueError('Refresh check frequency must be between 0 and 3600s')
    
    if refreshCredentials <= currentTs + refreshCheckFrequency:
        response = auth_client.refresh(refresh_token=data['refresh_token'])
        if "expires_in" not in response:
            raise ValueError("Un Authentcated Request: ",response)
        response["expires_in"] = currentTs + response["expires_in"]
        dumpDataToJson(response,"refresh-credentials.json")
        return response
    else:
        return data
    

def getPaymentData(accessToken):
    #making Request
    base_url = f'https://sandbox.api.intuit.com/quickbooks/v4/payments/charges/'
    auth_header = 'Bearer {0}'.format(accessToken)
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json;charset=UTF-8',
        'Content-type': '*/*'
    }
    response = requests.get(base_url, headers=headers)
    print(response.json())
    return response


if __name__ == "__main__":
    # fetchData()
    response = refresh_token()
    getCustomerData(accessToken = response["access_token"])
    getPaymentData(accessToken = response["access_token"])
    response2 = auth_client.get_user_info(access_token=response["access_token"])
    getPaymentData(accessToken = response["access_token"])
