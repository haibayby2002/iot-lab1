print("Hello ThingsBoard")
import paho.mqtt.client as mqttclient
import time
import json
import  random


#access_token: PThWLRpoIJfOUifjOZ9y
#device_id: 0f03f780-7814-11ec-91d1-9b16bfb7b504

BROKER_ADDRESS = "demo.thingsboard.io"
PORT = 1883
THINGS_BOARD_ACCESS_TOKEN = "PThWLRpoIJfOUifjOZ9y"

def subscribed(client, userdata, mid, granted_qos):
    print("Subscribed...")


def recv_message(client, userdata, message):
    print("Received: ", message.payload.decode("utf-8"))
    temp_data = {'value': True}
    try:
        jsonobj = json.loads(message.payload)
        if jsonobj['method'] == "setValue":
            temp_data['value'] = jsonobj['params']
            client.publish('v1/devices/me/attributes', json.dumps(temp_data), 1)
    except:
        pass


def connected(client, usedata, flags, rc):
    if rc == 0:
        print("Thingsboard connected successfully!!")
        client.subscribe("v1/devices/me/rpc/request/+")
    else:
        print("Connection is failed")


client = mqttclient.Client("Gateway_Thingsboard")
client.username_pw_set(THINGS_BOARD_ACCESS_TOKEN)

client.on_connect = connected
client.connect(BROKER_ADDRESS, 1883)
client.loop_start()

client.on_subscribe = subscribed
client.on_message = recv_message

#Some temperature configure
MAX_TEMP = 40
MIN_TEMP = -20
MAX_TEMP_STEP = 3

MAX_HUMI = 60
MIN_HUMI = 5
MAX_HUMI_STEP = 2

temp = random.randint(MIN_TEMP, MAX_TEMP)
humi = random.randint(MIN_HUMI, MAX_HUMI)
#light_intesity = random.randint(40, 120)

longitude = 106.6297
latitude = 10.8231

MIN_LONGTITUDE = -180
MAX_LONGTITUDE = 180
MIN_LATITUDE = -90
MAX_LATITUDE = 90

def updatePosition(max_longtitude_step, max_latitude_step):
    global longitude
    global latitude

    # Boundary limit
    longitude += random.uniform(-max_longtitude_step, max_longtitude_step)  #update longtitude
    if longitude > MAX_LONGTITUDE:
        longitude = MAX_LONGTITUDE
    elif longitude < MIN_LONGTITUDE:
        longitude = MIN_LONGTITUDE

    latitude += random.uniform(-max_latitude_step, max_latitude_step)   #update latitude
    #Boundary limit
    if latitude > MAX_LATITUDE:
        latitude = MAX_LATITUDE
    elif latitude < MIN_LATITUDE:
        latitude = MIN_LATITUDE

counter = 0
while True:
    collect_data = {'temperature': temp, 'humidity': humi, 'longitude': longitude, 'latitude': latitude}

    #for temperature
    temp += random.randrange(-MAX_TEMP_STEP, MAX_TEMP_STEP, 1)
    if temp > MAX_TEMP:
        temp = MAX_TEMP
    elif temp < MIN_TEMP:
        temp = MIN_TEMP

    #for humid
    humi += random.randrange(-MAX_HUMI_STEP, MAX_TEMP_STEP, 1)
    if humi > MAX_HUMI:
        humi = MAX_HUMI
    elif humi < MIN_HUMI:
        humi = MIN_HUMI

    #For position
    updatePosition(0.00001, 0.00001)
    print('(', latitude, ' ' , longitude, ')')

    client.publish('v1/devices/me/telemetry', json.dumps(collect_data), 1)
    time.sleep(10)
