import csv
import re

list_of_column_names = []
data = []
total = dict()
with open("Shakespeare_data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    #loops over the first row and gets the column names
    for row in reader:
        list_of_column_names.append(row)
        break
    #array of the index of columns that get looped over
    #columns are [Dataline', 'Play', 'PlayerLinenumber', 'ActSceneLine', 'Player', 'PlayerLine']
    included_cols = [1,4,5]
    for row in reader:
        #all of the data for one row is appended to this array
        rowData = []
        for i in included_cols:
            if len(row[3]) > 0:
                # enters block when the column being read is either the playName or characterName column
                if i == 1 or i == 4:
                    rowData.append(row[i])
                # enters block when the column being read is the spoken words
                if i == 5:
                    # array to hold the spoken words
                    spokenWordsArray = []
                    # saves the spoken words to a string
                    spokenWords = row[i]
                    spokenWords = spokenWords.split(" ")
                    # iterates over the string of spoken words
                    for p in spokenWords:
                        # makes all words lowercase
                        p = p.lower()
                        # removes punctuation from string https://www.geeksforgeeks.org/python-remove-punctuation-from-string/
                        res = re.sub(r"[^\w\s]", "", p)
                        # adds the lowercase and puctuationless word to the spokenWordsArray
                        spokenWordsArray.append(res)
                        if res in total:
                            # Increment count of word by 1
                            total[res] = total[res] + 1
                        else:
                            # Add the word to dictionary with count 1
                            total[res] = 1
                    # adds the edited spoken words to the rowData
                    rowData.append(spokenWordsArray)
        # appends the entire row as long as its not empty
        if len(rowData) > 0:
            data.append(rowData)

#sorts the dict by the highest repeated word https://careerkarma.com/blog/python-sort-a-dictionary-by-value/
sortedDict = sorted(total.items(), key=lambda x: x[1], reverse=True)
print(sortedDict)
