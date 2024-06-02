# App user segmentation is the task of grouping users based on how they engage with the app. It helps find retained users, find the user segment for a marketing campaign, and solve many other business problems where you need to search for users based on similar characteristics.

import numpy as np 
import pandas as pd 

df = pd.read_csv("C:\\Users\\PARUL\\Downloads\\userbehaviour.csv")

df.head() 

import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import pandas as pd
pio.templates.default = "plotly_white"

# Let’s start by looking at the highest, lowest, and average screen time of all the users:

print(f'Average Screen Time = {df["Average Screen Time"].mean()}')
print(f'Highest Screen Time = {df["Average Screen Time"].max()}')
print(f'Lowest Screen Time = {df["Average Screen Time"].min()}')

# Now let’s have a look at the highest, lowest, and the average amount spent by all the users:

print(f'Average Spend of the Users = {df["Average Spent on App (INR)"].mean()}')
print(f'Highest Spend of the Users = {df["Average Spent on App (INR)"].max()}')
print(f'Lowest Spend of the Users = {df["Average Spent on App (INR)"].min()}') 

# Now let’s have a look at the relationship between the spending capacity and screen time of the active users and the users who have uninstalled the app:

figure = px.scatter(data_frame = df, 
                    x="Average Screen Time",
                    y="Average Spent on App (INR)", 
                    size="Average Spent on App (INR)", 
                    color= "Status",
                    title = "Relationship Between Spending Capacity and Screentime",
                    trendline="ols")
figure.show()

# So this is great! Users who uninstalled the app had an average screen time of fewer than 5 minutes a day, and the average spent was less than 100. We can also see a linear relationship between the average screen time and the average spending of the users still using the app.

# Now let’s have a look at the relationship between the ratings given by users and the average screen time:

figure = px.scatter(data_frame = df, 
                    x="Average Screen Time",
                    y="Ratings", 
                    size="Ratings", 
                    color= "Status", 
                    title = "Relationship Between Ratings and Screentime",
                    trendline="ols")
figure.show()

# So we can see that users who uninstalled the app gave the app a maximum of five ratings. Their screen time is very low compared to users who rated more. So, this describes that users who don’t like to spend more time rate the app low and uninstall it at some point.

# App User Segmentation to Find Retained and Lost Users

clustering_data = df[["Average Screen Time", "Left Review", 
                        "Ratings", "Last Visited Minutes", 
                        "Average Spent on App (INR)", 
                        "New Password Request"]]

from sklearn.preprocessing import MinMaxScaler
for i in clustering_data.columns:
    MinMaxScaler(i)
    
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(clustering_data)
df["Segments"] = clusters

print(df.head(10))

print(df["Segments"].value_counts())

# Now let’s rename the segments for a better understanding:

df["Segments"] = df["Segments"].map({0: "Retained", 1: 
    "Churn", 2: "Needs Attention"})

PLOT = go.Figure()
for i in list(df["Segments"].unique()):
    

    PLOT.add_trace(go.Scatter(x = df[df["Segments"]== i]['Last Visited Minutes'],
                                y = df[df["Segments"] == i]['Average Spent on App (INR)'],
                                mode = 'markers',marker_size = 6, marker_line_width = 1,
                                name = str(i)))
PLOT.update_traces(hovertemplate='Last Visited Minutes: %{x} <br>Average Spent on App (INR): %{y}')

    
PLOT.update_layout(width = 800, height = 800, autosize = True, showlegend = True,
                   yaxis_title = 'Average Spent on App (INR)',
                   xaxis_title = 'Last Visited Minutes',
                   scene = dict(xaxis=dict(title = 'Last Visited Minutes', titlefont_color = 'black'),
                                yaxis=dict(title = 'Average Spent on App (INR)', 
                                           titlefont_color = 'black')))

# The blue segment shows the segment of users the app has retained over time. The red segment indicates the segment of users who just uninstalled the app or are about to uninstall it soon. And the green segment indicates the segment of users that the application has lost.





