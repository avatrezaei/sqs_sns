import boto3

QUEUE_NAME = 'MY_SQS_QUEUE'
QUEUE_NAME_URL = 'https://sqs.us-east-1.amazonaws.com/123456789012/MY_SQS_QUEUE'
FIFO_QUEUE_NAME = 'MY_SQS_QUEUE.fifo'
DEAD_LETTER_QUEUE_NAME = 'DEAD_LETTER_QUEUE'
MAIN_QUEUE_NAME = 'MY_MAIN_QUEUE'
MAIN_QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/123456789012/MY_MAIN_QUEUE'


def sqs_client():
    sqs = boto3.client('sqs', region_name='us-east-1')
    return sqs


def create_sqs_queue():
    response = sqs_client().create_queue(
        QueueName=QUEUE_NAME,
        Attributes={
            'DelaySeconds': '60',
            'MessageRetentionPeriod': '86400'
        }
    )
    return response


def cretae_fifo_queue():
    return sqs_client().create_queue(
        QueueName=FIFO_QUEUE_NAME,
        Attributes={
            'FifoQueue': 'true',
            'ContentBasedDeduplication': 'true'
        }
    )


def create_queue_for_dead_letter():
    return sqs_client().create_queue(
        QueueName=DEAD_LETTER_QUEUE_NAME,
        Attributes={
            'MessageRetentionPeriod': '86400'
        }
    )


def create_main_queue_for_dead_letter():
    return sqs_client().create_queue(
        QueueName=MAIN_QUEUE_NAME,
        Attributes={
            "DelaySeconds": "0",
            "MaximumMessageSize": "262144",
            "VisibilityTimeout": "30",
            "MessageRetentionPeriod": "345600",
            "ReceiveMessageWaitTimeSeconds": "0",
            'RedrivePolicy': {
                'deadLetterTargetArn': 'arn:aws:sqs:us-east-1:123456789012:DEAD_LETTER_QUEUE',
                'maxReceiveCount': '5'
            }
        }
    )


def find_queue():
    return sqs_client().list_queues(
        QueueNamePrefix='MY_'
    )


def delete_queue():
    return sqs_client().delete_queue(
        QueueUrl=QUEUE_NAME_URL
    )


def list_all_queues():
    return sqs_client().list_queues()


def get_queue_attributes():
    return sqs_client().get_queue_attributes(
        QueueUrl=QUEUE_NAME_URL,
        AttributeNames=[
            'All'
        ]
    )


def update_queue_attributes():
    return sqs_client().set_queue_attributes(
        QueueUrl=MAIN_QUEUE_URL,
        Attributes={
            'ReceiveMessageWaitTimeSeconds': '20',
            'MaximumMessageSize': '2048'
        }
    )


def send_message_to_queue():
    return sqs_client().send_message(
        QueueUrl=MAIN_QUEUE_URL,
        MessageBody='This is a message SQS',
        MessageAttributes={
            'Title': {
                'StringValue': 'Hello',
                'DataType': 'String'
            },
            'Author': {
                'StringValue': 'Avat',
                'DataType': 'String'
            },
            'Time': {
                'StringValue': '12:00',
                'DataType': 'String'
            }
        }
    )


def send_batch_messeges_to_queue():
    return sqs_client().send_message_batch(
        QueueUrl=MAIN_QUEUE_URL,
        Entries=[
            {
                'Id': '1',
                'MessageBody': 'This is a message SQS',
                'MessageAttributes': {
                    'Title': {
                        'StringValue': 'Hello',
                        'DataType': 'String'
                    },
                    'Author': {
                        'StringValue': 'Avat',
                        'DataType': 'String'
                    },
                    'Time': {
                        'StringValue': '12:00',
                        'DataType': 'String'
                    }
                }
            },

        ]
    )

def receive_message_from_queue():
    return sqs_client().receive_message(
        QueueUrl=MAIN_QUEUE_URL,
        AttributeNames=[
            'All'
        ],
        MessageAttributeNames=[
            'All'
        ],
        MaxNumberOfMessages=10,
        VisibilityTimeout=123,
        WaitTimeSeconds=0
    )

def process_message_from_queue():
    queued_messages = receive_message_from_queue()

    if 'Messages' in queued_messages and len(queued_messages['Messages']) >= 1:
        for message in queued_messages['Messages']:
            print(message['Body'])
            # delete_message_from_queue(message['ReceiptHandle'])
            change_visibility_timeout(message['ReceiptHandle'])


def delete_message_from_queue(receipt_handle):
    return sqs_client().delete_message(
        QueueUrl=MAIN_QUEUE_URL,
        ReceiptHandle=receipt_handle
    )

def message_visibility_timeout(receipt_handle):
    return sqs_client().change_message_visibility(
        QueueUrl=MAIN_QUEUE_URL,
        ReceiptHandle=receipt_handle,
        VisibilityTimeout=100
    )

def change_visibility_timeout(receipt_handle):
    return sqs_client().change_message_visibility(
        QueueUrl=MAIN_QUEUE_URL,
        ReceiptHandle=receipt_handle,
        VisibilityTimeout=100
    )

def purge_queue():
    return sqs_client().purge_queue(
        QueueUrl=MAIN_QUEUE_URL
    )

if __name__ == '__main__':
    # print(create_sqs_queue())
    # print(cretae_fifo_queue())
    # print(create_queue_for_dead_letter())
    # print(create_main_queue_for_dead_letter())
    # print(find_queue())
    # print(list_all_queues())
    # print(get_queue_attributes())
    # print(update_queue_attributes())
    # print(send_message_to_queue())
    # print(send_batch_messeges_to_queue())
    # print(receive_message_from_queue())
    # process_message_from_queue()
    # print(delete_message_from_queue())
    # print(message_visibility_timeout())
    # print(change_visibility_timeout())
    print(purge_queue())
