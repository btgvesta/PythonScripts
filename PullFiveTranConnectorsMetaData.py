import requests
import base64

# Plug in API key and secret here before running.
api_key = ''
api_secret = ''

auth_string = f"{api_key}:{api_secret}"
encoded_auth = base64.b64encode(auth_string.encode()).decode()

headers = {
    'Authorization': f'Basic {encoded_auth}'
}

# FiveTran API endpoint for connectors
url = 'https://api.fivetran.com/v1/connectors'

params = {
    'paused': 'false'
}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    connectors = response.json()['data']['items']
    print(f"Found {len(connectors)} connectors.")
    print("=" * 32)

    print("--- Active Fivetran Connectors ---")
    active_count = 0
    for connector in connectors:
        if not connector.get('paused'):
            active_count += 1
            connector_name = connector.get('schema')
            source_type = connector.get('service')
            sync_frequency = connector.get('sync_frequency')

            print(f"\nConnector Name: {connector_name}")
            print(f"  Source Type: {source_type}")
            print(f"  Sync Schedule (minutes): every {sync_frequency} minutes")

    print("-" * 32)
    print(f"Found {active_count} active connectors.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")