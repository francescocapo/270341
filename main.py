x_f.columns=['size of clusters','mean', 'std','min', '25%','median','75%','max']
x_m=data.groupby("ClusterLabel")[["Monetary Value"]].describe()
x_m.columns=['size of clusters','mean', 'std','min', '25%','median','75%','max']
x_m
%-----
x_r
x_f
#%%
x_f=data.groupby("ClusterLabel")[["Frequency"]].describe()
x_f.columns=['size of clusters','mean', 'std','min', '25%','median','75%','max']
x_f