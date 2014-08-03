"""
Print descriptive stats to a Markdown file.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import pytz

def toUTC(d):
	tz = pytz.timezone('US/Pacific')
	est_tz = tz = pytz.timezone('US/Eastern')
	return tz.localize(d).astimezone(pytz.utc)

df = pd.read_csv('results.csv')

# Date/time conversion to UTC
df['StartTime'] = df['StartTime'].apply(lambda d: toUTC(datetime.strptime(d.strip(' PDT'), '%Y-%m-%d %H:%M:%S')))
df['EndTime'] = df['EndTime'].apply(lambda d: toUTC(datetime.strptime(d.strip(' PDT'), '%Y-%m-%d %H:%M:%S')))
df.set_index(pd.DatetimeIndex(df['StartTime']), inplace=True)
# Remove unnecessary columns
df = df.drop(['PriceUnit', 'From', 'Direction', 'ApiVersion', 'AccountSid'], 1)
# Remove test calls
df = df[df.To != 4849197384]

# Print to file
f = open('stats.md', 'w')
f.write('## Duration Stats (in seconds)  \n\n')

stats = df['Duration'].describe()
for index, value in stats.iteritems():
	f.write(str(index) + ': ' + str(int(value)) + '  \n')
f.write('\n')

f.write('## Call Status Counts  \n\n')
for index, value in df['Status'].value_counts().iteritems():
	f.write(index + ': ' + str(int(value)) + '  \n')

f.close()
