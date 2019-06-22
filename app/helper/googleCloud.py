from google.oauth2 import service_account
from googleapiclient import discovery
from googleapiclient.errors import HttpError

class GoogleHelper : 
    def __init__ (self,project_id,cloud_region,service_account_json) : 
        self.project_id = project_id
        self.cloud_region = cloud_region
        self.service_account_json = service_account_json
        self.client = self.get_client()


    def get_client(self):
        """Returns an authorized API client by discovering the IoT API and creating
        a service object using the service account credentials JSON."""
        api_scopes = ['https://www.googleapis.com/auth/cloud-platform']
        api_version = 'v1'
        discovery_api = 'https://cloudiot.googleapis.com/$discovery/rest'
        service_name = 'cloudiotcore'
        credentials = service_account.Credentials.from_service_account_file(
                self.service_account_json)
        scoped_credentials = credentials.with_scopes(api_scopes)

        discovery_url = '{}?version={}'.format(
                discovery_api, api_version)

        return discovery.build(
                service_name,
                api_version,
                discoveryServiceUrl=discovery_url,
                credentials=scoped_credentials)


    def getDevices(self,registry_id) : 
    
        registry_path = 'projects/{}/locations/{}/registries/{}'.format(
                self.project_id, self.cloud_region, registry_id)
        
        devices = self.client.projects().locations().registries().devices(
               ).list(parent=registry_path).execute().get('devices', [])

        for device in devices:
                print('Device: {} : {}'.format(
                        device.get('numId'),
                        device.get('id')))
        return devices
        