import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from collections import Counter
import pandas
import datetime
import collections

plt.style.use('ggplot')

file = pandas.read_csv("dataset.csv")
df = pandas.DataFrame(file)

df["time"] = pandas.to_datetime(df["time"])
td = pandas.to_datetime("2015-02-02 00:00:00")
df["deltatime"] = (df['time']-td)
df["day"] = df['time'].dt.day
df["hours"] = df['time'].dt.hour
df["minutes"] = df['time'].dt.minute
df["seconds"] = df['time'].dt.second
df["total_seconds"] = (df["hours"]*3600)+(df["minutes"]*60)+(df["seconds"])
print(df.time)

df["id_freq"] = df.groupby('id')['id'].transform('count')
df["stat_freq"] = df.groupby('id')['status', 'id'].transform('count')

plt.hist2d(df.time_int, df.id_freq, bins=50, alpha=0.5)
df["id_solo"] = df.id_freq.where(df.id_freq<=10)
df["id_solo"] = df.id_solo.fillna(0)
print(df["responsetime"].where(df["responsetime"]>2.).count())
plt.subplots()
pt = df.plot(x='time', y='responsetime', legend=False)
plt.xlabel("date")
plt.ylabel("response time")
event = pandas.to_datetime("2015-02-02 11:00:00")
print(type(event))
df["after_event"] = df['time'>event]
df["rt_after_event"] = df['responsetime'].where(df['time']>event)
print(df.after_event)
print(df.rt_after_event)

pt_f = df.where(df.time>event).plot(x='time', y='responsetime', legend=False)
ymin, ymax = pt_f.get_ylim()
print(df.loc[df['status'] == 508])
pt_f.vlines(x='2015-02-11 11:00:00', ymin=ymin, ymax=ymax-1, color='b', label="status=508")
plt.legend()
plt.ylabel("responsetime (s)")

status_x = [100, 200, 302, 400, 404, 500, 501, 508]
y_pos = np.arange(len(status_x))
status_y = [2181, 12372, 4573, 3104, 960, 4518, 3107, 1]
plt.bar(y_pos, status_y, align='center')
plt.xticks(y_pos, status_x)
plt.yscale("log")
plt.ylim(0.1,14000)
plt.yscale("log")
plt.ylabel('frequency of status')
plt.xlabel('status code')

l_id = sorted(df["id"].unique())

l_id_f = df["id"].value_counts()
pandas.set_option('display.max_rows', len(l_id_f))
print(l_id_f)
y_pos = np.arange(len(l_id))
l_id_f=[3, 232, 21, 4, 143, 9, 1, 2, 3, 11, 6, 151, 6, 12, 1, 6, 2, 1, 319, 11, 14, 34, 3, 367, 43, 285, 237, 69, 17, 6, 2, 58, 209, 21, 1, 8, 1, 2, 8, 5, 3, 123, 1, 2, 14, 2, 103, 3, 240, 91, 7, 295, 75, 4, 83, 3, 7, 52, 16, 37, 175, 2, 1, 11, 1, 255, 4, 40, 6, 157, 155, 2, 9, 1, 135, 211, 7, 95, 35, 11, 2, 18, 17, 4, 3, 5, 31, 42, 68, 158, 363, 8, 18, 157, 13, 5, 5, 222, 34, 312, 1, 8, 1, 13, 42, 130, 63, 17, 58, 8, 190, 49, 13, 47, 14, 86, 8, 76, 11, 8, 32, 1, 23, 24, 4, 2, 52, 1, 49, 1, 3, 28, 53, 1, 29, 39, 257, 3, 144, 1, 33, 204, 1, 24, 29, 2, 385, 12, 107, 11, 78, 11, 5, 17, 2, 2, 48, 4, 284, 34, 257, 2, 3, 2, 114, 392, 3, 9, 5, 60, 6, 24, 132, 12, 1, 139, 1, 192, 80, 1, 59, 313, 60, 25, 217, 14, 3, 1, 89, 6, 279, 5, 63, 197, 73, 9, 13, 83, 1, 5, 29, 3, 58, 251, 106, 227, 10, 12, 7, 76, 14, 83, 2, 1, 12, 3, 205, 33, 27, 7, 28, 11, 48, 211, 396, 2, 185, 1, 4, 43, 73, 161, 18, 126, 2, 84, 2, 75, 60, 39, 336, 27, 1, 6, 4, 183, 25, 100, 204, 10, 149, 97, 70, 20, 1, 4, 88, 1, 6, 286, 1, 16, 18, 8, 2, 249, 3, 9, 2, 34, 3, 7, 3, 3, 400, 1, 3, 20, 21, 12, 16, 2, 12, 46, 82, 261, 20, 109, 122, 229, 2, 1, 243, 4, 141, 23, 29, 8, 5, 5, 2, 4, 24, 60, 3, 1, 5, 9, 109, 2, 4, 1, 1, 244, 285, 2, 6, 4, 42, 64, 3, 2, 15, 41, 212, 12, 9, 31, 2, 342, 8, 35, 19, 45, 49, 87, 2, 3, 140, 43, 48, 106, 133, 1, 23, 3, 2, 4, 25, 9, 33, 311, 9, 10, 2, 24, 9, 1, 330, 1, 5, 4, 125, 23, 92, 48, 46, 67, 4, 48, 7, 38, 16, 190, 35, 178, 166, 4, 22, 129, 15, 297, 145, 352, 347, 7, 39, 208, 19, 85, 2, 3, 5, 2, 80, 72, 225, 4, 8, 30, 112, 1, 62, 140, 19, 1, 400, 16, 371, 309, 3, 35, 88, 99, 132, 37, 10, 92, 84, 20, 2, 233, 38, 263, 268, 100, 56, 1, 35, 145, 4, 19, 3, 11, 23, 11, 14, 11, 49, 65, 294, 5, 8, 167, 55, 2, 4, 1, 10, 21, 2, 21, 243, 10, 1, 40, 44, 200, 23, 111, 110, 303, 364, 64, 48, 357, 9, 8, 5, 2]
print(np.mean(l_id_f))
plt.xlim(0,470)
plt.ylim(0, 410)
plt.xlabel("Numerical user ID, ordered alphabetically")
plt.ylabel("frequency")
plt.bar(y_pos, l_id_f, align='center')
plt.xticks(y_pos, l_id, rotation='vertical')


df.hist(layout=(2, 5))
h = df.total_seconds.hist()
h.set_xlabel("total seconds since midnight")
h.set_yscale("log")
h.set_xlim(1,10)
h.set_ylim(0,200)
plt.savefig("total_seconds.pdf")
    
h = df["status"].where(df["id"]=="Claire").hist()
status_x = [100, 200, 302, 400, 404, 500, 501, 508]
y_pos = np.arange(len(status_x))
status_y = [9, 53, 15, 13, 7, 25, 12, 1]
print(df["status"].where(df["id"]=="Claire").value_counts().sort_index(0))
plt.bar(y_pos, status_y, align='center')
plt.xticks(y_pos, status_x)
plt.ylabel("frequency of status for user 'claire'")
plt.xlabel("status code")



l_day = df['day'].tolist()
l_sec = df['total_seconds'].tolist()
l_binsx =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
l_bins_n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
h = plt.hist2d(l_day, l_sec, bins=15)
plt.grid(False)
plt.xlabel("day of the month")
plt.ylabel("seconds since midnight")
plt.colorbar()
plt.savefig("time_Vs_response.pdf")
for i, group in df.groupby('statu'):
    plt.figure()
    group.plot(x='time', y='responsetime', title="status = "+str(i), legend=False)
    group.plot(df['responsetime'], bins=20, alpha=0.5, title="status = "+str(i), kind="hist")
    plt.ylabel("responsetime (s)")
    title=str(i)+".pdf"
  plt(marker='o')
    plt.savefig(title)
print(df["stat_freq"])
for i, group, in df.groupby(['id']):
    print(group)
    print(group["status"])
    count = group["status"].value_counts().sort_index(0).to_dict()
    o_count = collections.OrderedDict(sorted(count.items()))
    print(o_count)
    plt.bar(range(len(o_count)), o_count.values(), align='center')
    plt.xticks(range(len(o_count)), list(o_count.keys()))
    
    
    group["status"].plot(x='status', y=group['status'].value_counts(), title="user status - "+str(i), legend=False, kind="bar")




    thing = df.groupby('status')['status'].transform('count')
    status_x = [100, 200, 302, 400, 404, 500, 501, 508]
    y_pos = np.arange(len(status_x))
    freq =  df["status"].value_counts()
    df['status'].where(df["id"]==group).value_counts().sort_index(0).plot(kind='bar')
    df[df.id == i].plot(x="status",title="user status - "+str(i), legend=False, kind="bar")
    plt.bar(y_pos, freq, align='center')
    plt.xticks(y_pos, status_x)
    plt.ylabel("frequency of status for user")
    group.plot(df['responsetime'], bins=20, alpha=0.5, title="status = "+str(i), kind="hist")
    plt.xlabel("status code")
    plt.title(" status codes user - "+str(i))
    title="user_status"+str(i)+".png"
     plt(marker='o')
    plt.savefig(title)
    plt.clf()

plt.yticks(df.status.unique())

plt.show()
