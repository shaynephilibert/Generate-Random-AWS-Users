import boto3
import random

client = boto3.client('iam')

#Generate Random Number
randomInt = random.randint(1000,9999)

#A Collection of Random Words
words = 'tiger bird rabbit dog cat moon light sage mushroom rogue panda stork analyst helper assistant magic wombat'.split()
random.shuffle(words)

#Build the random username
newUserName = str(randomInt)+"-"+random.choice(words)

#Method to create random user
def createSingleUser(newUserName):
    response = client.create_user(
        Path='/GeneratedUsers/',
        UserName=newUserName,
        Tags=[
            {
                'Key': 'Generated',
                'Value': ''
            },
    ]
)

#Call the function to create the random user
createSingleUser(newUserName)
print("Success: "+newUserName+" was created!")