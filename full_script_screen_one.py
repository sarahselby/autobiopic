import sys
from Adafruit_IO import MQTTClient
import vlc
import time
import random

# change this to Freya's AdafruitIO credentials 
ADAFRUIT_IO_KEY = "aio_hASB20dLiA1kSLzeh5IBU5iGUmri"
ADAFRUIT_IO_USERNAME = 'freyawhite24'
FEED_ID = 'auto-biopic-1'
media_player = vlc.MediaPlayer()
media_player.set_fullscreen(True)

def chooseVideo(mess):
    file_name = 'videos/' + mess + '.mp4'
    media = vlc.Media(file_name)
    media_player.set_media(media)
    playVideo()
    
def playVideo():
    try:
        media_player.play()
        time.sleep(10)
    except KeyboardInterrupt:
        pass

def connected(client):
    print('Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID))
    client.subscribe(FEED_ID)

def subscribe(client, userdata, mid, granted_qos):
    print('Subscribed to {0} with QoS {1}'.format(FEED_ID, granted_qos[0]))

def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    chooseVideo(payload)

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.on_subscribe  = subscribe

client.connect()
client.loop_blocking()
