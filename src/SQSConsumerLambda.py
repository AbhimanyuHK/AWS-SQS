'''
Created on Nov 19, 2018

@author: abhimanyu_h_k
'''

def consumer_start(json_input, context):
    
    for message in json_input['Records']:
        print message['body']
    