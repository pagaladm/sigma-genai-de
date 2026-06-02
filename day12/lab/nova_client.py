import boto3
import json

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

def ask_nova(prompt):
    response = client.invoke_model(
        modelId="amazon.nova-pro-v1:0",
        body=json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        })
    )

    result = json.loads(response["body"].read())
    return result

if __name__ == "__main__":
    print(ask_nova("Say: Nova Pro is working"))