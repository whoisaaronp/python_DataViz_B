import csv

canada = []
world = []
bronzes = []

categories = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1;

        elif row[4] == "CAN":
            canada.append([int(row[0]), row[5], row[6], row[7]])
        else: 
            world.append([int(row[0]), row[5], row[6], row[7]])
            line_count =+ 1

print('total medals for canada:', len(canada))
print('rest of the world:', len(world))

print(canada[0])

print('processed', line_count, 'rows of data')

gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []

for medal in canada:
    if medal[0] == 1924 and medal[3] == "Gold":
        gold_1924.append(medal)
    elif medal[0] == 1948 and medal[3] == "Gold":
        gold_1948.append(medal)
    elif medal[0] == 1972 and medal[3] == "Gold":
        gold_1972.append(medal)
    elif medal[0] == 2002 and medal[3] == "Gold":
        gold_2002.append(medal)
    elif medal[0] == 2014 and medal[3] == "Gold":
        gold_2014.append(medal)

print('canada won', len(gold_1924),  'gold medals in 1924')
print(' canada won',  len(gold_2014), 'gold medals in 2014')


#  Array bucket for men and women parse
men_1924 = []
women_1924 = []
men_1948 = []
women_1948 = []
men_1972 = []
women_1972 = []
men_2002 = []
women_2002 = []
men_2014 = []
women_2014 = []

# Loop that is fetching the excel sheet from 
# first if state we'll check the year[0] which is the years in csv, the if means the years[1] is referencing the gender then it's appending to another array.
# [0] = years, [1] gender, [2] = event, [3] = medals
for years in canada:
    if years[0] == 1924 and years[3] == "Gold":
    # here must be 1924 and gold to execute
        if years[1] == "Men": 
            men_1924.append(years)
        elif years[1] == "Women": 
            women_1924.appending(years)
    # end if 1924 and gold

print('men', len(gold_1924), 'gold medals in 1924')
print('men', len(gold_1948), 'gold medals in 1948')
print('men', len(gold_1972), 'gold medals in 1972')
print('men', len(gold_2002), 'gold medals in 2012')
print('men', len(gold_2014), 'gold medals in 2014')


#  

