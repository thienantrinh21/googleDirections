import urllib.request
import json

origin = input("Choose a starting location: ").replace(" ","+")
destination = input("Choose a destination: ").replace(" ","+")
key = input("Please input your Maps API key here: ")

url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={key}"

maps = urllib.request.urlopen(url).read()

Steps = json.loads(maps)["routes"][0]["legs"][0]["steps"]

Origin = json.loads(maps)["routes"][0]["legs"][0]["start_address"]

Destination = json.loads(maps)["routes"][0]["legs"][0]["end_address"]

print(f"Starting from {Origin}\n")

for point in range(len(Steps)):

    directions = Steps[point]["html_instructions"].replace("<b>","").replace("</b>", "").replace("</div>", "").replace("<div style=\"font-size:0.9em\">","").replace("Destination","\nThe destination")

    distance = Steps[point]["distance"]["text"]

    print(f"{directions} in {distance}")

print(f"\nYou have reached your destination:\n{Destination}")
