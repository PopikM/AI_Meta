import pandas as pd
from os import listdir
import matplotlib.pyplot as plt
import numpy as np

# files = [f for f in listdir("results/astar")]

# print(len(files))

# j = 0
# sss = [1, 10, 2, 20, 3, 4, 5, 6, 7, 8, 9]
# ss = sss[j]
# ttfw = 0.2

# print("ss,ttfw,%win,% travelled,run time,nodes evaluated")

# for i in range(0, 110):
#     ss = sss[j]
#     df = pd.read_csv("results/astar/" + files[i], header=2)
#     df2 = pd.read_csv("results/astar/" + files[i + 110], header=2)
#     df3 = pd.read_csv("results/astar/" + files[i + 220], header=2)
#     print(str(ss) + "," 
#           + '%.2f' % ttfw + "," + 
#           '%.2f' % ((df["win/fail"].sum() + df2["win/fail"].sum() + df3["win/fail"].sum()) / 45.0) + "," +
#           '%.2f' % ((df["% travelled"].sum() + df2["% travelled"].sum() + df3["% travelled"].sum()) / 45.0) + "," +
#           str((df["run time"].sum() + df2["run time"].sum() + df3["run time"].sum())) + "," +
#           str((df["nodes evaluated"].sum() + df2["nodes evaluated"].sum() + df3["nodes evaluated"].sum()))
#           )
    
#     ttfw += 0.2;
#     if ttfw > 2.05:
#         ttfw = 0.2
#         j += 1;       
#         pass

df = pd.read_csv("resultsConc/astar.csv")

df_fin = df.pivot(index="ss", columns="ttfw", values="% travelled")
print(df_fin)

plt.imshow(df_fin, cmap="hot")
plt.title("% Travelled")
plt.ylabel("Search steps")
plt.xlabel("Time to finish weight")
plt.yticks(range(len(df_fin.index)), df_fin.index)
plt.xticks(range(len(df_fin.columns)), df_fin.columns)
plt.colorbar()
plt.show();