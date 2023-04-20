import csv

rank_list = []
with open('data.csv', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        rank_list.append(row)

with open('country_codes.csv', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        country_list = {row[1]:row[0] for row in reader}

for i in range(len(rank_list)):
    if rank_list[i][6].upper() in country_list:
        rank_list[i][6] = country_list[rank_list[i][6].upper()]

with open('edited_data.csv', 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    for i in range(len(rank_list)):
        writer.writerow(rank_list[i])
