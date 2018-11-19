'''
Created on Nov 19, 2018

@author: abhimanyu_h_k
'''

import boto3

class SQSPublisher(object):

    def __init__(self, queue):
        
        # Get the service resource
        self.sqs = boto3.resource('sqs')
        # Get the queue
        if queue is None :
            self.queue = self.sqs.get_queue_by_name(QueueName='FlowTest.fifo')
        else:
            self.queue = self.sqs.get_queue_by_name(QueueName=queue)
        
    
    def publish(self, data):
        response = self.queue.send_message(
            MessageBody=data
            # MessageGroupId='messageGroup1'
            )
        
        # The response is NOT a resource, but gives you a message ID and MD5
        print(response.get('MessageId'))
        print(response.get('MD5OfMessageBody'))
        
if __name__== "__main__":
    SQSPublisher('FlowTest.fifo').publish("welcome to AWS 7")
    