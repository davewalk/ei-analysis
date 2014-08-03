"""
Scatter plots by day.

Dirty yet somewhat useful.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
import pytz
from pandas.tools.plotting import scatter_matrix
from pylab import savefig

call_days = ['20140709', '20140710', '20140711', '20140714', '20140716',
             '20140717', '20140718', '20140721', '20140722', '20140723',
             '20140725', '20140728', '20140730', '20140731', '20140801']

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
# Filter out calls over 100 seconds
df = df[df.Duration < 100]

# Print the plots
for call_day in call_days:
	day = df[call_day:call_day]
	dates = matplotlib.dates.date2num(day.StartTime)

	fig, ax = plt.subplots()
	ax.plot_date(dates, day.Duration, xdate=True)

	ax.set_title('Call Duration by Time (%s/%s/%s)' % (call_day[5:6], call_day[7:], call_day[:4]))

	ax.grid(True)
	plt.xlabel('Time (UTC)')
	plt.ylabel('Duration (seconds)')

	savefig('graphs/scatter_plots/by_duration/' + call_day + '.png')