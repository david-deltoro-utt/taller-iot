# Import Adafruit IO REST client.
from Adafruit_IO import Client, RequestError, Feed
import random 
import os
import time



class AdafruitAPI():     
    def __init__(self, feeds=[]):
        self.ADAFRUIT_IO_KEY = ''
        self.ADAFRUIT_IO_USERNAME = 'davidtoro'
        self.aio = Client(self.ADAFRUIT_IO_USERNAME, self.ADAFRUIT_IO_KEY)
        self.name_feeds=feeds
        self.feeds=[]
        
    def getFeed(self, feed_name):
        return  self.aio.feeds(feed_name)
        
        
    def create(self):
        for x in self.name_feeds:
            try:
                variable= self.aio.feeds(x)
            except RequestError: # Doesn't exist, create a new feed
                feed = Feed(name=x)
                variable = self.aio.create_feed(feed)
            self.feeds.append(variable)
            
    def random_feed(self): 
        for f in self.feeds: 
            self.aio.send_data(f.key, random.randrange(20,50))
            
    def read_feed(self,f):
        os.system ("cls")
        print('*********** {0}*****************'.format(f.name))
        print('*********** {0}*****************'.format(f))
        data={"value":0}
        data = self.aio.receive(f.key)
        print('Retrieved value from Test has attributes: {0}'.format(data))
        print('Latest value from {0}: {1}'.format(f.name,data.value))
        # Finally read the most revent value from feed 'Foo'.
        time.sleep(2)
        
    def read_feeds(self):
        for f in self.feeds: 
            self.read_feed(f)
                    
                    
    def read_main(self):
        try:
            while True:
                    #Para DOS/Windows
                    self.read_feeds()
        except KeyboardInterrupt:
            pass
        
        
if __name__ == '__main__':
    mqtt=AdafruitAPI(feeds=["led","ultrasonico"])
    mqtt.create()
    mqtt.random_feed()
    mqtt.read_main()
    