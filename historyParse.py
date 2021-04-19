import sqlite3
import sys
from datetime import datetime
import calendar as cal

try: 
    filename = sys.argv[1]
    database = sqlite3.connect(filename)
        
    Cur_TD = database.cursor()
    Total_Downloads = "SELECT count(*) FROM Downloads;"
    Cur_TD.execute(Total_Downloads)
    td = Cur_TD.fetchall()

    Cur_UT = database.cursor()
    Unique_Term = "SELECT COUNT (DISTINCT term) FROM keyword_search_terms;"
    Cur_UT.execute(Unique_Term)
    ut = Cur_UT.fetchall()

    Cur_Fname = database.cursor()
    longest_time = "SELECT DISTINCT replace(current_path, rtrim(current_path, replace(target_path, '\', '' ) ), '') file_name, received_bytes FROM Downloads ORDER BY (end_time - start_time) DESC LIMIT 1"
    Cur_Fname.execute(longest_time)
    cf = Cur_Fname.fetchall()

    Cur_Search = database.cursor()
    Recent_Search = "SELECT a.term, datetime(B.last_visit_time  / 1000000 - 11644473600, 'unixepoch', 'localtime') as LAST_VISIT_TIME FROM keyword_search_terms A,  URLS B where B.id = a.url_id ORDER BY LAST_VISIT_TIME DESC"
    Cur_Search.execute(Recent_Search)
    cs = Cur_Search.fetchall()

    Cur_dt = database.cursor()
    date_time_search = "SELECT datetime(B.last_visit_time  /1000000 + (strftime('%s', '1601-01-01')), 'unixepoch')  as last_visit_time FROM keyword_search_terms A,  URLS B where B.id = a.url_id ORDER BY last_visit_time DESC LIMIT 1"
    Cur_dt.execute(date_time_search)
    dt = Cur_dt.fetchall()
    
    print("Source File:",format(filename))
    print("Total Downloads:", format(td[0][0]))
    print("File Name:", format(cf[0][0].split("\\")[-1]))
    print("File Size:",format(cf[0][1]))
    print("Unique Search Terms:", format(ut[0][0]))
    print("Most Recent Search:", format(cs[0][0]))
   # print( format(dt[0][0]))
    print("Most Recent Search Date/Time:",dt[0][0].split("-")[0]+"-"+cal.month_abbr[int(dt[0][0].split("-")[1])]+"-"+dt[0][0].split("-")[-2], dt[0][0].split(" ")[-1])
except IndexError:
    print("Error! - No History File Specified!")
except IOError:
    print ("Error! - File Not Found!")
except FileNotFoundError:
    print("Error! - File Not Found!")
    raise (SystemExit)
except sqlite3.OperationalError:
    print ("Error! - File Not Found!")