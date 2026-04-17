import requests

Goat = requests.get("https://api.tvmaze.com/search/people?q=Leonardo").json()
response = Goat

Goat_last_names = set()

for item in response:
    Goat_full_name = item["person"]["name"]
    Goat_name_parts = Goat_full_name.split()
    
    if len(Goat_name_parts) > 1 and Goat_name_parts[0] == 'Leonardo':
        last_name = Goat_name_parts[-1]
        Goat_last_names.add(Goat_last_names)

print("Unique last names of Leonardos:")
for name in Goat_last_names:
    print(name)


