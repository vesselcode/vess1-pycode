#penerapan list dalam phyton

# opening the CSV file
with open('stok_buah.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)
