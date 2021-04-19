import sys
import csv
import datetime as dt
import operator
import calendar as cal

if __name__=="__main__":
	try:
		file = sys.argv[1]
		with open(file) as csv_file:
			csvread = csv.reader(csv_file, delimiter=',')
			ip_dict_key={}
			bad_ip_list=[]
			commad_list=[]
			sIP = []
			infectedHost = []
			Init_connection=0

			for row in csvread:
				if row[4] in ['1338','1337', '1339','1340']:
					if row[1] not in bad_ip_list:
						bad_ip_list.append(row[1])
					if (row[2] not in commad_list and row[1] in bad_ip_list):
						commad_list.append(row[2])
					if Init_connection == 0:
						Init_connection = int(row[0])

				if(row[2] in commad_list and (row[2] in ip_dict_key.keys())):
					ip_dict_key[row[2]] =int(row[5]) + ip_dict_key[row[2]]
				elif(row[2] in commad_list and (row[2] not in ip_dict_key.keys())):
					ip_dict_key[row[2]] = int(row[5])
	
			for i in bad_ip_list:
				sIP.append(i.split("."))
				sIP.sort(key=lambda sIP:int(sIP[3]))

			for i in sIP:
				order_ip="."
				order_ip = order_ip.join(i)
				infectedHost.append(order_ip)

			print("Source File:",file) 
			print("Systems Infected:",len(infectedHost)) 
			print("Infected System IPs:",infectedHost)
			print("C2 Servers:",len(commad_list))
			commad_list.sort(reverse=False)
			print("C2 Server IPs:",commad_list)
			date = dt.datetime.utcfromtimestamp(Init_connection).strftime('%Y-%m-%d %H:%M:%S')
			print("First C2 Connection:",date.split("-")[0]+"-"+cal.month_abbr[int(date.split("-")[1])]+"-"+date.split("-")[-1],"UTC")
			c2Data_total = sorted(ip_dict_key.items(), key=operator.itemgetter(1),reverse=True)
			print("C2 Data Totals:",c2Data_total)
	except IndexError:
		print("Error! - No Log File Specified!")
	except IOError:
		print ("Error! - File Not Found!")
	except FileNotFoundError:
		print("Error! - File Not Found!")




