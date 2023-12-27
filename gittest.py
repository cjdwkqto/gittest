import boto3
import json

# AWS Lambda 클라이언트 초기화
lambda_client = boto3.client('lambda')

# Lambda 함수 호출
response = lambda_client.invoke(
    FunctionName='get_secret',  # Lambda 함수 이름
    InvocationType='RequestResponse'
)

# Lambda 함수의 응답 처리
response_payload = json.loads(response['Payload'].read().decode("utf-8"))

# 받은 데이터 활용
api_key = response_payload['api_key']  # 예: 'api_key'가 반환되는 secret 데이터의 키라 가정
another_key = response_payload['another_key']  # 예: 'another_key'가 또 다른 데이터 키라 가정

# 데이터 출력 혹은 활용
print(api_key)
print(another_key)
