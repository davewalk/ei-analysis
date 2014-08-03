# Electronic Intern Analysis

Statistics and analysis of at this point over 800 calls to after-school programs by the [Electronic Intern](https://github.com/davewalk/electronic_intern) using Pandas and Matplotlib and maybe other stuff eventually.

# Results

### Scatter plot results
* These plots of time of day to duration do not really show a correlation between the two.
* However, it appears that throughout the day there is a constant duration of 77 seconds with the status of "completed".
  * How could this be? The only thing that I think of in common is that this is an answering machine picking up. Each number triggers the answering machine after the same number of rings (four?). The message starts playing immediately and to Twilio this is considered "completed".
* So now that I know that there is a pretty high frequency of calls of the exact same duration, I can try to see if it is always the same callees. K-Means or something else?