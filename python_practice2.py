counties = ["Arapahoe", "Denver", "Jefferson"]
if counties [1] == 'Denver':
    print(counties[1])


if score >= 90:
    print('Your grade is an A.')
else:
    if your score >= 80:
        print('Your grade is a B.')
    else:
        if your score >= 70:
            print ('Your grade is a C.')
        else: 
            if score >= 60:
                print('Your grade is a D.')
            else: 
                if score >= 50:
                    print('Your grade is a F.')    

Resources/election_results.csv
file_to_load = 'Resources/election_results.csv'
election_data = open(file_to_load, 'r')
with open(election_results.csv) as election_data:
    