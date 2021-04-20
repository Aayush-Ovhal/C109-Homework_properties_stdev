import pandas as pd
import statistics as st
import plotly.graph_objects as go
import plotly.figure_factory as pff
import csv

df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].to_list()

meanH = st.mean(height_list)
medianH = st.median(height_list)
modeH = st.mode(height_list)
stdevH = st.stdev(height_list)

firststart, firstend = meanH - stdevH, meanH + stdevH
secondstart, secondend = meanH - (2 * stdevH), meanH + (2 * stdevH)
thridstart, thirdend = meanH - (3 * stdevH), meanH + (3 * stdevH)

firstdata = [result for result in height_list if result > firststart and result < firstend]
secondata = [result for result in height_list if result > secondstart and result < secondend]
thirdata = [result for result in height_list if result and result < thirdend]

percent_firstdata = len(firstdata) * 100/ len(height_list)
percent_secondata = len(secondata) * 100/len(height_list)
percent_thirdata = len(thirdata) * 100/ len(height_list)

print(str(percent_firstdata) + "% of data lies within first deviation")
print(str(percent_secondata) + "% of data lies within second deviation")
print(str(percent_thirdata) + "% of data lies within third deviation")


