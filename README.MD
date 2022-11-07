# AZURE VAULT 보안비밀 사용 샘플
## AZV 개요
> 각 서비스 코드 노출(유출) 발생 시 패스워드와 같은 주요정보의 노출을 최소화 하고자 다음과 같이 AZV 보안비밀의 키 값을 환경변수로 등록

> 각 프로젝트 .env에 패스워드와 같은 주요정보를 직접 작성하는 것이 아닌 환경변수를 불러오는 방식으로 사용


### 설치
1. AZV 초기 세팅 가이드는 document 가이드 참고
> https://learn.microsoft.com/ko-kr/azure/key-vault/secrets/quick-create-python?tabs=azure-cli

> ./.env 파일 생성 필수

>./simple-web/default_env > ./simple-web/.env

2. 라이브러리 설치 (python-azure-vault-sdk, python-dotenv, json)
```bash
pip install azure-keyvault-secrets azure-identity
```


### 사용 예
1. ./conf/conf.josn을 수정하여 불어올 AZV 키 이름과 등록할 환경변수 이름 작성

```json
{
    "KVUri" : "https://{your-vault-name}.vault.azure.net/",
    "shell": "bashrc",
    "ListSecret" : {
        "★★★★AZV에 등록된 키 값★★★★":"★★★★ENV에 등록된(할) 이름★★★★",
        "AZV-AUTH-TOKEN-TEST":"AZV_AUTH_TOKEN_TEST", 
        "AZV-AUTH-PASSWORD-TEST":"AZV_AUTH_PASSWORD_TEST",
        "keyvalue3":"env_name3",
        "keyvalue4":"env_name4"
    }
}
```

2. 키 값 불어오기 및 환경변수 등록
```bash
python ./AzureVualtGetSecret.py
source ~/.bashrc
```
mac - zsh를 사용하는 경우
 > ./conf/conf.json 4line 수정
 ```json
{
    ...
    "shell": "zshrc",
    ...
}
```
```bash
python ./AzureVualtGetSecret.py
source ~/.zshrc
```


## 프로젝트 .env 설정 예시

> ./simple-web/.env
```env
AUTH_PASSWORD=${AZV_AUTH_PASSWORD_TEST}
AUTH_TOKEN=${AZV_AUTH_TOKEN_TEST}
```
.env파일의 값을 위의 json에서 등록한 환경변수 값으로 작성

```bash
cd ./simple-web
python index.py
> 0987654321
```

