""" THIS SCRIPT IS VALID BASED ON THE SINGAPORE MRT MAP VERSION ON 20 SEPTEMBER 2018. """

"""
LINE NO              LINE
   1                 EAST WEST LINE
   2                 NORTH SOUTH LIKE
   3                 CIRCLE LINE
   4                 NORTH EAST LINE
   5                 DOWNTOWN LINE
   6                 CIRCLE LINE BRANCH
   7                 AIRPORT BRANCH
   8                 BUKIT PANJANG LRT
   9                 SENKANG LRT WEST
   10                SENKANG LRT EAST
   11                PUNGGOL LRT WEST
   12                PUNGGOL LRT EAST
"""


# Display name of station in data
# When checking with input call .upper
data = {
         1 : {
                 1:["Pasir Ris",[]],
                 2:["Tampines",[5]],
                 3:["Simei",[]],
                 4:["Tanah Merah",[7]],
                 5:["Bedok",[]],
                 6:["Kembangan",[]],
                 7:["Eunos",[]],
                 8:["Paya Lebar",[3]],
                 9:["Aljunied",[]],
                 10:["Kallang",[]],
                 11:["Lavender",[]],
                 12:["Bugis",[5]],
                 13:["City Hall",[2]],
                 14:["Raffles Place",[2]],
                 15:["Tanjong Pagar",[]],
                 16:["Outram Park",[4]],
                 17:["Tiong Bahru",[]],
                 18:["Redhill",[]],
                 19:["Queenstown",[]],
                 20:["Commonwealth",[]],
                 21:["Buona Vista",[3]],
                 22:["Dover",[]],
                 23:["Clementi",[]],
                 24:["Jurong East",[2]],
                 25:["Chinese Garden",[]],
                 26:["Lakeside",[]],
                 27:["Boon Lay",[]],
                 28:["Pioneer",[]],
                 29:["Joo Koon",[]],
                 30:["Gul Circle",[]],
                 31:["Tuas Crescent",[]],
                 32:["Tuas West Road",[]],
                 33:["Tuas Link",[]]
             },
         2 : {
                 1:["Jurong East",[1]],
                 2:["Bukit Batok",[]],
                 3:["Bukit Gombak",[]],
                 4:["Choa Chu Kang",[8]],
                 5:["Yew Tee",[]],
                 6:[None,[]],
                 7:["Kranji",[]],
                 8:["Marsiling",[]],
                 9:["Woodlands",[]],
                 10:["Admiralty",[]],
                 11:["Sembawang",[]],
                 12:[None,[]],
                 13:["Yishun",[]],
                 14:["Khatib",[]],
                 15:["Yio Chu Kang",[]],
                 16:["Ang Mo Kio",[]],
                 17:["Bishan",[3]],
                 18:["Braddell",[]],
                 19:["Toa Payoh",[]],
                 20:["Novena",[]],
                 21:["Newton",[5]],
                 22:["Orchard",[]],
                 23:["Somerset",[]],
                 24:["Dhoby Ghaut",[3,4]],
                 25:["City Hall",[1]],
                 26:["Raffles Place",[1]],
                 27:["Marina Bay",[6]],
                 28:["Marina South Pier",[]]
             },
         3 : {
                 1:["Dhoby Ghaut",[2,4]],
                 2:["Bras Basah",[]],
                 3:["Esplanade",[]],
                 4:["Promenade",[5,6]],
                 5:["Nicoll Highway",[]],
                 6:["Stadium",[]],
                 7:["Mountbatten",[]],
                 8:["Dakota",[]],
                 9:["Paya Lebar",[1]],
                 10:["MacPherson",[5]],
                 11:["Tai Seng",[]],
                 12:["Bartley",[]],
                 13:["Serangoon",[4]],
                 14:["Lorong Chuan",[]],
                 15:["Bishan",[2]],
                 16:["Marymount",[]],
                 17:["Caldecott",[]],
                 18:[None,[]],
                 19:["Botanical Gardens",[5]],
                 20:["Farrer Road",[]],
                 21:["Holland Village",[]],
                 22:["Buona Vista",[1]],
                 23:["one-north",[]],
                 24:["Kent Ridge",[]],
                 25:["Haw Par Villa",[]],
                 26:["Pasir Panjang",[]],
                 27:["Labrador Park",[]],
                 28:["Telok Blangah",[]],
                 29:["HarbourFront",[4]]
             },
         4 : {
                 1:["HarbourFront",[3]],
                 2:[None,[]],
                 3:["Outram Park",[1]],
                 4:["Chinatown",[5]],
                 5:["Clarke Quay",[]],
                 6:["Dhoby Ghaut",[2,3]],
                 7:["Little India",[5]],
                 8:["Farrer Park",[]],
                 9:["Boon Keng",[]],
                 10:["Potong Pasir",[]],
                 11:["Woodleigh",[]],
                 12:["Serangoon",[3]],
                 13:["Kovan",[]],
                 14:["Hougang",[]],
                 15:["Buangkok",[]],
                 16:["Sengkang",[9,10]],
                 17:["Punggol",[11,12]]
             },
         5 : {
                 1:["Bukit Panjang",[8]],
                 2:["Cashew",[]],
                 3:["Hillview",[]],
                 4:[None,[]],
                 5:["Beauty World",[]],
                 6:["King Albert Park",[]],
                 7:["Sixth Avenue",[]],
                 8:["Tan Kah Kee",[]],
                 9:["Botanic Gardens",[3]],
                 10:["Stevens",[]],
                 11:["Newton",[2]],
                 12:["Little India",[4]],
                 13:["Rocher",[]],
                 14:["Bugis",[1]],
                 15:["Promenade",[3,6]],
                 16:["Bayfront",[6]],
                 17:["Downtown",[]],
                 18:["Telok Ayer",[]],
                 19:["Chinatown",[4]],
                 20:["Fort Canning",[]],
                 21:["Bencoolen",[]],
                 22:["Jalan Besar",[]],
                 23:["Bendemeer",[]],
                 24:["Geylang Bahru",[]],
                 25:["Mattar",[]],
                 26:["Macpherson",[3]],
                 27:["Ubi",[]],
                 28:["Kaki Bukit",[]],
                 29:["Bedok North",[]],
                 30:["Bedok Reservoir",[]],
                 31:["Tampines West",[]],
                 32:["Tampines",[1]],
                 33:["Tampines East",[]],
                 34:["Upper Changi",[]],
                 35:["Expo",[7]],
             },
         6 : {
                 0:["Promenade",[3,5]],
                 1:["Bayfront",[5]],
                 2:["Marina Bay",[2]]
             },
         7 : {
                 0:["Tanah Merah",[1]],
                 1:["Expo",[5]],
                 2:["Changi Airport",[]]
             },
         8 : {
                 1:["Choa Chu Kang",[2]],
                 2:["South View",[]],
                 3:["Keat Hong",[]],
                 4:["Teck Whye",[]],
                 5:["Phoenix",[]],
                 6:["Bukit Panjang",[5]],
                 7:["Petir",[]],
                 8:["Pending",[]],
                 9:["Bangkit",[]],
                 10:["Fajar",[]],
                 11:["Segar",[]],
                 12:["Jelapang",[]],
                 13:["Senja",[]],
                 14:["Ten Mile Junction",[]]
             },
         9 : {
                 0:["Sengkang",[4,10]],
                 1:["Cheng Lim",[]],
                 2:["Farmway",[]],
                 3:["Kupang",[]],
                 4:["Thanggam",[]],
                 5:["Fernvale",[]],
                 6:["Layar",[]],
                 7:["Tongkang",[]],
                 8:["Renjong",[]]
             },
         10: {
                 0:["Sengkang",[4,9]],
                 1:["Compasville",[]],
                 2:["Rumbia",[]],
                 3:["Bakau",[]],
                 4:["Kangkar",[]],
                 5:["Ranggung",[]]
             },
         11: {
                 0:["Punggol",[4,12]],
                 1:["Sam Kee",[]],
                 2:["Teck Lee",[]],
                 3:["Punggol Point",[]],
                 4:["Samudera",[]],
                 5:["Nibong",[]],
                 6:["Sumang",[]],
                 7:["Soo Teck",[]]
             },
         12: {
                 0:["Punggol",[4,11]],
                 1:["Cove",[]],
                 2:["Meridian",[]],
                 3:["Coral Edge",[]],
                 4:["Riviera",[]],
                 5:["Kadaloor",[]],
                 6:["Oasis",[]],
                 7:["Damai",[]]
             }

       }
                 
"""
LINE NO              LINE
   1                 EAST WEST LINE
   2                 NORTH SOUTH LIKE
   3                 CIRCLE LINE
   4                 NORTH EAST LINE
   5                 DOWNTOWN LINE
   6                 CIRCLE LINE BRANCH
   7                 AIRPORT BRANCH
   8                 BUKIT PANJANG LRT
   9                 SENKANG LRT WEST
   10                SENKANG LRT EAST
   11                PUNGGOL LRT WEST
   12                PUNGGOL LRT EAST
"""
#---------------
#START OF CODE |
#---------------
import time
def get_line(number):
    if number == 1:
        return "East West Line"
    if number == 2:
        return "North South Line"
    if number == 3:
        return "Circle Line"
    if number == 4:
        return "North East Line"
    if number == 5:
        return "Downtown Line"
    if number == 6:
        return "Circle Line Branch"
    if number == 7:
        return "EWL Airport Branch"
    if number == 8:
        return "Bukit Panjang LRT"
    if number == 9:
        return "Sengkang LRT West"
    if number == 10:
        return "Sengkang LRT East"
    if number == 11:
        return "Punggol LRT West"
    if number == 12:
        return "Punggol LRT East"
    return "Unknown" #this should not happen

while True:
  start_station = input("Enter the name of your starting station.").upper()
  start_station_info = None
  station_found = False
  #Find out and print the details of the start station
  for line,stations in data.items():
      for number,stationdata in stations.items():
        try:
          if stationdata[0].upper() == start_station:
            if station_found == False:
              start_station_info = [line,number,stationdata]
              station_found = True
            else:
                pass
        except:
             pass
  if start_station_info == None:
      print("Invalid Input.")
      pass
  else:
      break

print("---------------------------------------------")
print(f"Starting Station Details")
inter = ""
for number in start_station_info[2][1]:
    inter = inter+f", {get_line(number)}"
if inter == "":
    inter = "No Interchanges."
else:
    inter = inter[1:]
data2 = [f"Line : {get_line(start_station_info[0])}",
         f"Station Name : {start_station_info[2][0]}",
         f"Station Number: {start_station_info[1]}",
         f"Interchange(s) : {inter}"]
for line in data2:
    print(line)
print("---------------------------------------------")

while True:
  end_station = input("Enter the name of your ending station.").upper()
  end_station_info = None
  station_found = False
  #Find out and print the details of the end station
  for line,stations in data.items():
      for number,stationdata in stations.items():
        try:
          if stationdata[0].upper() == end_station:
            if station_found == False:
              end_station_info = [line,number,stationdata]
              station_found = True
            else:
                pass
        except:
             pass
  if end_station_info == None:
      print("Invalid Input.")
      pass
  else:
      break

print("---------------------------------------------")
print(f"Ending Station Details")
inter = ""
for number in end_station_info[2][1]:
    inter = inter+f", {get_line(number)}"
if inter == "":
    inter = "No Interchanges."
else:
    inter = inter[1:]
data2 = [f"Line : {get_line(end_station_info[0])}",
         f"Station Number: {end_station_info[1]}",
         f"Station Name : {end_station_info[2][0]}",
         f"Interchange(s) : {inter}"]
for line in data2:
    print(line)
print("---------------------------------------------")


print("---------------------------------------------")
print("Starting to find your route...")
print("---------------------------------------------")
time.sleep(1)
alrdy_reached = False
print(f"Fastest way from {start_station_info[2][0]} to {end_station_info[2][0]}")
if start_station_info[2][0] == end_station_info[2][0]:
    print("You have reached your destination.")
    alrdy_reached = True
# Datasets : end_station_info and start_station_info
# Both is a list [lineenumber,stationnumber,[stationname,[interchanges]]]


# First, Check if the stations fall in the same line.
same_line = False
start_station_lines = [start_station_info[0]]
for interchange in start_station_info[2][1]:
    start_station_lines.append(interchange)
end_station_lines = [end_station_info[0]]
for interchange in end_station_info[2][1]:
    end_station_lines.append(interchange)

    
for line in start_station_lines:
    if line in end_station_lines:
        same_line = True
        line_no = line

if same_line == True:
    if alrdy_reached == False:
      print(f"Take the {get_line(line_no)} directly to your destination.")
      alrdy_reached = True


if not alrdy_reached:
    #Interchanges.
    # variables start_station_lines, end_station_lines, start_station_info[0], end_station_info[0]
    opt_1 = False
    for key in sorted(data[start_station_info[0]].keys()):
        value = data[start_station_info[0]][key]
        interchanges_stn = value[1]
        name_stn = value[0]
        for item in interchanges_stn:
            if item in end_station_lines:
                if opt_1 == False:
                  opt_1 = True
                  alrdy_reached = True
                  line_to = get_line(item)
                  change_at = name_stn
                  station_change_at_1 = key
                else:
                    #an alternative solution was found. which is faster?
                    station_change_at = key
                    station_now_at = start_station_info[1]
                    if abs(station_now_at - station_change_at) < abs(station_now_at - station_change_at_1):
                      line_to = get_line(item)
                      change_at = name_stn
                      station_change_at_1 = key
    #Repeat twice for consistency, but this time list is rotated
    for key in sorted(data[start_station_info[0]].keys())[::-1]:
        value = data[start_station_info[0]][key]
        interchanges_stn = value[1]
        name_stn = value[0]
        for item in interchanges_stn:
            if item in end_station_lines:
                if opt_1 == False:
                  opt_1 = True
                  line_to = get_line(item)
                  change_at = name_stn
                  station_change_at_1 = key
                else:
                    #an alternative solution was found. which is faster?
                    station_change_at = key
                    station_now_at = start_station_info[1]
                    if abs(station_now_at - station_change_at) < abs(station_now_at - station_change_at_1):
                      line_to = get_line(item)
                      change_at = name_stn
                      station_change_at_1 = key
    if alrdy_reached:           
      print(f"Change to the {line_to} at {change_at} and you will reach your destination.")

if not alrdy_reached:
    #Double Interchange now.
    pass











print("---------------------------------------------")
print("Thank you for using the SG MRT GPS by XtremeCoder.")
input("Press Enter to exit.")
      

