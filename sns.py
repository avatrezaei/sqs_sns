import boto3

TOPIC_NAME = 'TOPIC_NAME'
TOPIC_ARN = 'arn:aws:sns:us-east-1:123456789012:TOPIC_NAME'


def sns_client():
    sns = boto3.client('sns', region_name='us-east-1')
    return sns


def create_topic():
    return sns_client().create_topic(
        Name=TOPIC_NAME
    )


def get_topics():
    return sns_client().list_topics()


def get_topic_attributes():
    return sns_client().get_topic_attributes(
        TopicArn=TOPIC_ARN
    )


def update_topic_attributes():
    return sns_client().set_topic_attributes(
        TopicArn=TOPIC_ARN,
        AttributeName='DisplayName',
        AttributeValue=TOPIC_NAME + '-Updated'
    )


def delete_topic():
    return sns_client().delete_topic(
        TopicArn=TOPIC_ARN
    )


def create_email_subscription(topic_arn, email_address):
    return sns_client().subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint=email_address
    )

def create_sms_subscription(topic_arn, phone_number):
    return sns_client().subscribe(
        TopicArn=topic_arn,
        Protocol='sms',
        Endpoint=phone_number
    )

def create_sqs_queue_subscription(topic_arn, queue_arn):
    return sns_client().subscribe(
        TopicArn=topic_arn,
        Protocol='sqs',
        Endpoint=queue_arn
    )

def list_subscriptions():
    return sns_client().list_subscriptions()

def list_subscriptions_by_topic(topic_arn):
    return sns_client().list_subscriptions_by_topic(
        TopicArn=topic_arn
    )

def unsubscribe(subscription_arn):
    return sns_client().unsubscribe(
        SubscriptionArn=subscription_arn
    )

def publish_message(topic_arn, message):
    return sns_client().publish(
        TopicArn=topic_arn,
        Message=message
    )

def check_if_phone_number_opted_out(phone_number):
    return sns_client().check_if_phone_number_is_opted_out(
        phoneNumber=phone_number
    )

def list_phone_numbers_opted_out():
    return sns_client().list_phone_numbers_opted_out()

def opt_out_of_email_subscription(email_address):
    list_subscriptions  = list_subscriptions_by_topic(TOPIC_ARN)
    for subscription in list_subscriptions['Subscriptions']:
        if subscription['Protocol'] == 'email' and subscription['Endpoint'] == email_address:
            print(subscription['SubscriptionArn'])
            unsubscribe(subscription['SubscriptionArn'])
            print('Unsubscribed')
            return True
        
    return False

def opt_out_of_sms_subscription(phone_number):
    list_subscriptions  = list_subscriptions_by_topic(TOPIC_ARN)
    for subscription in list_subscriptions['Subscriptions']:
        if subscription['Protocol'] == 'sms' and subscription['Endpoint'] == phone_number:
            print(subscription['SubscriptionArn'])
            unsubscribe(subscription['SubscriptionArn'])
            print('Unsubscribed')
            return True
        
    return False



def opt_in_phone_number(phone_number):
    return sns_client().opt_in_phone_number(
        phoneNumber=phone_number
    )



if __name__ == '__main__':
    print(create_topic())
    # {'TopicArn': 'arn:aws:sns:us-east-1:123456789012:TOPIC_NAME'}
    print(get_topics())
    # {'Topics': [{'TopicArn': 'arn:aws:sns:us-east-1:123456789012:TOPIC_NAME'}], 'ResponseMetadata': {'RequestId': 'a1b2c3d4-567e-8fgh-90ij-klmnopqrstuv', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'a1b2c3d4-567e-8fgh-90ij-klmnopqrstuv', 'content-type': 'text/xml', 'content-length': '356', 'date': 'Thu, 01 Jan 1970 00:00:00 GMT'}, 'RetryAttempts': 0}}
    print(get_topic_attributes())
    create_email_subscription(TOPIC_ARN, 'avatrezaei88@gmail.com')
    create_sms_subscription(TOPIC_ARN, '+989123456789')
    create_sqs_queue_subscription(TOPIC_ARN, 'arn:aws:sqs:us-east-1:123456789012:MY_QUEUE')
    print(list_subscriptions())
    print(list_subscriptions_by_topic(TOPIC_ARN))
    print(publish_message(TOPIC_ARN, 'Hello World'))
    print(check_if_phone_number_opted_out('+989123456789'))
    print(delete_topic())
    # {'ResponseMetadata': {'RequestId': 'a1b2c3d4-567e-8fgh-90ij-klmnopqrstuv', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'a1b2c3d4-567e-8fgh-90ij-klmnopqrstuv', 'content-type': 'text/xml', 'content-length': '212', 'date': 'Thu, 01 Jan 1970 00:00:00 GMT'}, 'RetryAttempts': 0}}
    print(list_phone_numbers_opted_out())
    opt_out_of_email_subscription('avatrezaei88@gmail.com')
    opt_out_of_sms_subscription('+989123456789')
    print(opt_in_phone_number('+989123456789'))

