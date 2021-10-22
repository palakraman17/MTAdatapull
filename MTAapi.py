from google.transit import gtfs_realtime_pb2
import os
import requests
import pandas as pd
import json
from datetime import datetime

df_id2Name = None

def ReadCsv(filename):
  global df_id2Name
  df = pd.read_csv(filename)
  df_id2Name = df[['stop_id','stop_name']]
  # print (df_id2Name)
  print(df_id2Name.loc[df_id2Name['stop_id'] == 'R01N',['stop_name']])


def main():
    my_headers = {'x-api-key' : 'tQ5fewZjmB9F2Fe53QJkc15tM3nH7cMG6ONiDPdN'}
    feed = gtfs_realtime_pb2.FeedMessage()
    url = ('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw')
    ReadCsv('Stop.Csv')
    get_feed(feed, url, my_headers)

def printResults(feed):
    from datetime import datetime
    ts = int(str(feed.header.timestamp))
    print("Last update: " + datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S'))
    for entity in feed.entity:
        if entity.HasField('trip_update'):
        
          
          Trips = entity.trip_update.stop_time_update
          print(">>>>>>>>>>>>>ROUTE: ",entity.trip_update.trip.route_id,"<<<<<<<<<<<<<<<<<<<")
          for trip in Trips:
            print("Arrival Time :",  datetime.fromtimestamp(int(trip.arrival.time)), "Departure ",datetime.fromtimestamp(int(trip.departure.time)),"Station: ",df_id2Name.loc[df_id2Name['stop_id'] == trip.stop_id,['stop_name']].to_string(header=None) )

          # print (str(entity)+';')

        with open('output.txt', mode='w') as f:
            for entity in feed.entity:
                if entity.HasField('trip_update'):
                        f.write(str(entity.trip_update.trip.trip_id)+';')



def get_feed(feed, url , Authheaders):
    # proxies = {'http': '127.0.0.1:5555','https': '127.0.0.1:5555'}
    response = requests.get(url,headers = Authheaders ,allow_redirects=True)
    try:
        feed.ParseFromString(response.content)
        printResults(feed)
    except :
        print("Oops!  That was no valid data. Try again...\n\n" )
        try:
            from google.protobuf import text_format
            text_format.Parse(response.content.decode('UTF-8'), feed, allow_unknown_extension=True)
            print("Parse with text format successfully.")
            printResults(feed)
        except text_format.ParseError as e:
            raise IOError("Cannot parse file %s." % (str(e)))
if __name__ == "__main__":
    main()



















# feed = gtfs_realtime_pb2.FeedMessage()

# try:
#   my_headers = {'x-api-key' : 'tQ5fewZjmB9F2Fe53QJkc15tM3nH7cMG6ONiDPdN'}
#   response = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/  nyct%2Fgtfs-nqrw',headers=my_headers)
#   response.raise_for_status()
#   # print(response)
#   print(response.text())
  
#   # feed.ParseFromString(response.text())
#   # for entity in feed.entity:
#   #   if entity.HasField('trip_update'):
#   #     print (entity.trip_update)
# except requests.exceptions.HTTPError as error:
#   print(error)
#   # This code will run if there is a 404 error.

