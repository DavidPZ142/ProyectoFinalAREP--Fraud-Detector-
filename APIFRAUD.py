import boto3, uuid, json
client = boto3.client('frauddetector', region_name='us-east-1')
response = client.get_event_prediction(
    detectorId="detector-getting-started",
    eventId=str(uuid.uuid4()),
    eventTypeName="registration",
    eventTimestamp="2019-08-10T20:44:00Z",
    entities=[{"entityType": "customer", "entityId": str(uuid.uuid4())},],
    eventVariables={
        "billing_address": "78253 Centro Comercial Calima.",
        "billing_postal": "39854",
        "billing_state": "NC",
        "email_address": "ncamacho@gmail.com",
        "ip_address": "122.136.132.150",
        "phone_number": "(555) 332 - 9271",
        "user_agent": "Mozilla/5.0 (iPad CPU iPad OS 10_3_3 like Mac OS X) AppleWebKit/532.2 (KHTML, like Gecko) CriOS/34.0.827.0 Mobile/13K063 Safari/532.2"
    }

    print('The predicted outcome is :' +json.dumps(response['ruleResults'][0]['outcomes']))
)
