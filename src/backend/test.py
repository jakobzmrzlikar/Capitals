import json

state_capitals = {"Washington": "Olympia", "Oregon": "Salem",
                  "California": "Sacramento", "Ohio": "Columbus",
                  "Nebraska": "Lincoln", "Colorado": "Denver",
                  "Michigan": "Lansing", "Massachusetts": "Boston",
                  "Florida": "Tallahassee", "Texas": "Austin",
                  "Oklahoma": "Oklahoma City", "Hawaii": "Honolulu",
                  "Alaska": "Juneau", "Utah": "Salt Lake City",
                  "New Mexico": "Santa Fe", "North Dakota": "Bismarck",
                  "South Dakota": "Pierre", "West Virginia": "Charleston",
                  "Virginia": "Richmond", "New Jersey": "Trenton",
                  "Minnesota": "Saint Paul", "Illinois": "Springfield",
                  "Indiana": "Indianapolis", "Kentucky": "Frankfort",
                  "Tennessee": "Nashville", "Georgia": "Atlanta",
                  "Alabama": "Montgomery", "Mississippi": "Jackson",
                  "North Carolina": "Raleigh", "South Carolina": "Columbia",
                  "Maine": "Augusta", "Vermont": "Montpelier",
                  "New Hampshire": "Concord", "Connecticut": "Hartford",
                  "Rhode Island": "Providence", "Wyoming": "Cheyenne",
                  "Montana": "Helena", "Kansas": "Topeka",
                  "Iowa": "Des Moines", "Pennsylvania": "Harrisburg",
                  "Maryland": "Annapolis", "Missouri": "Jefferson City",
                  "Arizona": "Phoenix", "Nevada": "Carson City",
                  "New York": "Albany", "Wisconsin": "Madison",
                  "Delaware": "Dover", "Idaho": "Boise",
                  "Arkansas": "Little Rock", "Louisiana": "Baton Rouge"}

with open('data.json', 'w') as f:
        json.dump(state_capitals, f, ensure_ascii=False, indent=2, sort_keys=True)
