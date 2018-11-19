'''
Created on Nov 19, 2018

@author: abhimanyu_h_k
'''

import boto3


class SQSConsumer(object):
    '''
    classdocs
    '''

    def __init__(self, queue):
        '''
        Constructor
        '''
        # Get the service resource
        self.sqs = boto3.resource('sqs')
        # Get the queue
        if queue is None :
            self.queue = self.sqs.get_queue_by_name(QueueName='FlowTest.fifo')
        else:
            self.queue = self.sqs.get_queue_by_name(QueueName=queue)
        
    def start(self):
        
        # Process messages by printing out body
        for message in self.queue.receive_messages():
            # Print out the body of the message
            print('Hello, {0}'.format(message.body))
            
            # Let the queue know that the message is processed
            message.delete()
        
        
if __name__ == "__main__":
    SQSConsumer(queue='FlowTest.fifo').start()
    
