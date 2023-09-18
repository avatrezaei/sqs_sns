# AWS SNS & SQS Python Utility

This utility provides a way to interact with AWS SNS (Simple Notification Service) and SQS (Simple Queue Service) through Python using `boto3`.

## Prerequisites

- Python 3.x
- Boto3 installed (`pip install boto3`)
- AWS credentials configured. You can either configure it via the command line (`aws configure`) or by setting the following environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and optionally `AWS_DEFAULT_REGION`.

## Features

### SNS Utility Functions:

1. **`sns_client`**: Returns an SNS client.
2. **`create_topic`**: Creates an SNS topic.
3. **`get_topics`**: Lists all SNS topics.
4. **`get_topic_attributes`**: Retrieves attributes of a specific SNS topic.
5. **`update_topic_attributes`**: Updates specific attributes of an SNS topic.
6. **`delete_topic`**: Deletes an SNS topic.
7. **`create_email_subscription`**: Creates an email subscription for a specific topic.
8. **`create_sms_subscription`**: Creates an SMS subscription for a specific topic.
9. **`create_sqs_queue_subscription`**: Creates an SQS queue subscription for a specific topic.
10. **`list_subscriptions`**: Lists all subscriptions.
11. **`list_subscriptions_by_topic`**: Lists all subscriptions of a specific topic.
12. **`unsubscribe`**: Removes a specific subscription.
13. **`publish_message`**: Publishes a message to a given topic.
14. **`check_if_phone_number_opted_out`**: Checks if a phone number has opted out of receiving messages.
15. **`list_phone_numbers_opted_out`**: Lists all phone numbers that have opted out of receiving messages.
16. **`opt_out_of_email_subscription`**: Unsubscribes an email from the given topic.
17. **`opt_out_of_sms_subscription`**: Unsubscribes a phone number from the given topic.
18. **`opt_in_phone_number`**: Opts a phone number back into receiving messages.

### SQS Utility Functions:

1. **`sqs_client`**: Returns an SQS client.
2. **`create_sqs_queue`**: Creates an SQS queue.
3. **`cretae_fifo_queue`**: Creates a FIFO SQS queue.
4. **`create_queue_for_dead_letter`**: Creates a dead-letter SQS queue.
5. **`find_queue`**: Lists all queues with a specific prefix.
6. **`delete_queue`**: Deletes an SQS queue.
7. **`list_all_queues`**: Lists all SQS queues.
8. **`get_queue_attributes`**: Retrieves attributes of a specific SQS queue.
9. **`update_queue_attributes`**: Updates specific attributes of an SQS queue.
10. **`send_message_to_queue`**: Sends a single message to a given queue.
11. **`send_batch_messeges_to_queue`**: Sends a batch of messages to a given queue.
12. **`receive_message_from_queue`**: Receives messages from a given queue.
13. **`process_message_from_queue`**: Processes and prints the messages received from a given queue.
14. **`delete_message_from_queue`**: Deletes a processed message from the queue.
15. **`message_visibility_timeout`**: Changes the visibility timeout of a message.
16. **`purge_queue`**: Purges all messages from a queue.

## How to Use:

- Update constants like `TOPIC_NAME`, `TOPIC_ARN`, `QUEUE_NAME`, etc., with the desired values.
- Comment/Uncomment the desired methods under the `if __name__ == '__main__':` section to perform the specific operations.
- Run the script to execute the operations.

> **Note**: Make sure to handle exceptions and ensure the appropriate IAM roles and permissions are in place before performing any operations.