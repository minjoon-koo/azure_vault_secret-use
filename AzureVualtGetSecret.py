import os ,json,common
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
load_dotenv(".env")

#불러올 보안비밀 정보 확인
os.chdir(os.path.dirname(os.path.realpath(__file__)))
conf = common.common()
KVUri = conf['KVUri']
shell = conf['shell']
ListSecret = conf['ListSecret']
'''ListSecret 예시
{
'AZV에 등록된 키 값': 'ENV에 등록된 이름', 
'AZV-AUTH-TOKEN-TEST': 'AZV_AUTH_TOKEN_TEST', 
'AZV-AUTH-PASSWORD-TEST': 'AZV_AUTH_PASSWORD_TEST', 
'keyvalue3': 'env_name3', 
'keyvalue4': 'env_name4'
}
'''

#검증
CheckSecretDict = {}
CheckFailDict ={}
'''CheckSecretDict 예시
{
    'AZV-AUTH-TOKEN-TEST': {
        'AZV_AUTH_TOKEN_TEST': '1234567890'
        }, 
    'AZV-AUTH-PASSWORD-TEST': {
        'AZV_AUTH_PASSWORD_TEST': '0987654321'
        }
}
'''

#az vault 연결
credential = DefaultAzureCredential()
client = SecretClient(
    vault_url=KVUri,
    credential=credential
    )

#실제 사용할(조회 할) 비밀 값 확인
def checkValue():
    secrets = client.list_properties_of_secrets()
    tmpList = []
    for secret in secrets:
        tmpList.append(secret.name)

    for i in ListSecret.keys():
        if i in tmpList:
            Key = client.get_secret(i)
            CheckSecretDict[i]={ListSecret[i]:Key.value}
        else: 
            CheckFailDict[i]=None
    
#유효한 값을 환경변수로 등록 
def env_create(env_name,env_value):
    cmd = f"echo 'export {env_name}={env_value}' >> ~/.{shell}"
    print(cmd)
    os.system(cmd)
    
def main(): 
    print(f"AZV KEY FIND ..")
    print(f"")
    checkValue()
    print(f"fail to find key: {CheckFailDict}")
    print(f"")
    print(f"##set ENV")
    for i in CheckSecretDict.keys():
        env_name = next(iter(CheckSecretDict[i].keys()))
        env_value = CheckSecretDict[i][env_name]
        env_create(env_name,env_value)
    os.system(f"source ~/.{shell}")

if __name__ == '__main__':
    main()


