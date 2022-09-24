import os
import random
Directory = '/home/azureuser/spam_filter/enron1/emails/'
Dir_list = os.listdir(Directory)
for file in Dir_list:
    pass
with open(Directory + file, 'r') as f:
    emails_list = [f.read()]
