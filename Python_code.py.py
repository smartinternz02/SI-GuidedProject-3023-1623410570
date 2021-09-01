import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "c0uvi7",
        "typeId": "iotinformation",
        "deviceId":"001"
    },
    "auth": {
        "token": "Jyo12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if(cmd.data['command']=="motoron"):
                print("motor on")
                
    elif(cmd.data['command']=="motoroff"):
                print("motor off")

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    t=random.randint(-20,125)
    h=random.randint(0,100)
    v=random.randint(0,100)
    myData={'temperature':t, 'humidity':h, 'voltage':v}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
