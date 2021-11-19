# MTAdatapull
To fetch live data from MTA's Api.

## Description
Get MTA Live transit data and later run it in a Pi or Pocket computer to display status Trains or/and your station of concern status.
Enabling a piece of live transit information at your door so that you can make wise decisions before leaving your home/Work.
One of the perks of living in NYC - THE MTA.

## Pre-requisite
Install Modules
1. Google's Transite API  
   ```pip install --upgrade gtfs-realtime-bindings```
2. Requests Module  
   ```pip install requests```
3. Pandas
   ```pip install pandas ```  
4. Get Developer API-Key from:  
   https://new.mta.info/developers  
5. Google Transit Reference:  
   https://developers.google.com/transit/gtfs/reference

## Document Hierarchy
MTAdatapull  
|- MTAApi.py  
|- Stops.csv  
|- Output.txt

### Response packet will look like
```  
entity {
  id: "000017FS"
  trip_update {
    trip {
      trip_id: "138950_FS..N"    
      start_time: "23:09:30"     
      start_date: "20211118"     
      route_id: "FS"
    }
    stop_time_update {
      arrival {
        time: 1637294970
      }
      departure {
        time: 1637294970
      }
      stop_id: "D26N"
    }
    stop_time_update {
      arrival {
        time: 1637295150
      }
      departure {
        time: 1637295150
      }
      stop_id: "S04N"
    }
    stop_time_update {
      arrival {
        time: 1637295270
      }
      departure {
        time: 1637295270
      }
      stop_id: "S03N"
    }
    stop_time_update {
      arrival {
        time: 1637295390
      }
      departure {
        time: 1637295390
      }
      stop_id: "S01N"
    }
  }
}  
```

