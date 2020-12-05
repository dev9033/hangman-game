# change the 'csv.txt' below to your csv file absolute location
with open('comma_sep_val.txt') as f:
    file_data = f.read()

new = file_data.replace(',','\n')

# the list will be on the same location of your csv file
with open('list.txt','w') as f:
    f.write(new)