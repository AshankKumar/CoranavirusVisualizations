import pandas as pd

state_dict = {
    'Alabama' :'AL',
    'Alaska' :'AK',
    'Arizona' :'AZ',
    'Arkansas' :'AR',
    'California' :'CA',
    'Colorado' :'CO',
    'Connecticut' :'CT',
    'Delaware' :'DE',
    'Florida' :'FL',
    'Georgia' :'GA',
    'Hawaii' :'HI',
    'Idaho' :'ID',
    'Illinois' :'IL',
    'Indiana' :'IN',
    'Iowa' :'IA',
    'Kansas' :'KS',
    'Kentucky' :'KY',
    'Louisiana' :'LA',
    'Maine' :'ME',
    'Maryland' :'MD',
    'Massachusetts' :'MA',
    'Michigan' :'MI',
    'Minnesota' :'MN',
    'Mississippi' :'MS',
    'Missouri' :'MO',
    'Montana' :'MT',
    'Nebraska' :'NE',
    'Nevada' :'NV',
    'New Hampshire' :'NH',
    'New Jersey' :'NJ',
    'New Mexico' :'NM',
    'New York' :'NY',
    'North Carolina' :'NC',
    'North Dakota' :'ND',
    'Ohio' :'OH',
    'Oklahoma' :'OK',
    'Oregon' :'OR',
    'Pennsylvania' :'PA',
    'Rhode Island' :'RI',
    'South Carolina' :'SC',
    'South Dakota' :'SD',
    'Tennessee' :'TN',
    'Texas' :'TX',
    'Utah' :'UT',
    'Vermont' :'VT',
    'Virginia' :'VA',
    'Washington' :'WA',
    'West Virginia' :'WV',
    'Wisconsin' :'WI',
    'Wyoming' :'WY',
}

df = pd.read_csv('us-states.csv')

df = df.loc[(df['state'] != 'Guam') & (df['state'] != 'District of Columbia') & (df['state'] != 'Northern Mariana Islands') & (df['state'] != 'Puerto Rico') & (df['state'] != 'Virgin Islands')]

df['code'] = df['state'].map(state_dict)
df['date'] = pd.to_datetime(df['date'])
df.index = df['date']


DFList = []

for group in df.groupby(df.index.date):
    DFList.append(group[1])

print (type(DFList[0]))
print (type(df))