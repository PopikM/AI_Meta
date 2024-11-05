import pandas as pd
from os import listdir
import matplotlib.pyplot as plt
import numpy as np

# files = [f for f in listdir("results/astarGrid2")]

# print(len(files))

# j = 0
# k = 0
# dfpaps = [0, 1, 10, 2, 3, 4, 5, 6, 7, 8, 9]
# dfpap = dfpaps[j]
# dfpmp = dfpaps[k]

# print("dfpap,dfpmp,%win,% travelled,run time,game ticks,planning time,total plannings,nodes evaluated,most backtracked nodes")

# for i in range(0, 121):
#     dfpap = dfpaps[j]
#     dfpmp = dfpaps[k]
#     df = pd.read_csv("results/astarGrid2/" + files[i], header=5)
#     df2 = pd.read_csv("results/astarGrid2/" + files[i + 121], header=5)
#     df3 = pd.read_csv("results/astarGrid2/" + files[i + 121 * 2], header=5)
#     print(str(dfpap) + "," 
#           + '%.2f' % dfpmp + "," + 
#           '%.2f' % ((df["win/fail"].sum() + df2["win/fail"].sum() + df3["win/fail"].sum()) / 363) + "," +
#           '%.2f' % ((df["% travelled"].sum() + df2["% travelled"].sum() + df3["% travelled"].sum()) / 363) + "," +
#           str((df["run time"].sum() + df2["run time"].sum() + df3["run time"].sum())) + "," +
#           str((df["game ticks"].sum() + df2["game ticks"].sum() + df3["game ticks"].sum())) + "," +
#           str((df["planning time"].sum() + df2["planning time"].sum() + df3["planning time"].sum())) + "," +
#           str((df["total plannings"].sum() + df2["total plannings"].sum() + df3["total plannings"].sum())) + "," +
#           str((df["nodes evaluated"].sum() + df2["nodes evaluated"].sum() + df3["nodes evaluated"].sum())) + "," +
#           str(max((df["most backtracked nodes"].max(), df2["most backtracked nodes"].max(), df3["most backtracked nodes"].max())))
#           )
    
#     k += 1
#     if k > 10:
#         k = 0
#         j += 1;       
#         pass

df = pd.read_csv("resultsConc/astarGrid2.csv")

df_fin = df.pivot(index="dfpap", columns="dfpmp", values="most backtracked nodes")
print(df_fin)

plt.imshow(df_fin, cmap="hot")
plt.title("Run time")
plt.ylabel("DFPAP")
plt.xlabel("DFPMP")
plt.yticks(range(len(df_fin.index)), df_fin.index)
plt.xticks(range(len(df_fin.columns)), df_fin.columns)
plt.colorbar()
plt.show();