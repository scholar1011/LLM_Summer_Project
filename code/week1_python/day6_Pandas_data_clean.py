import pandas as pd
import numpy as np

data = {
    "姓名": ["王五","张三","李四","王五","钱器","黄毛","张三"],
    "班级": ["1班","1班","2班","1班","2班","1班","1班"],
    "语文": [12, np.nan, 34, 12, 56, 90, np.nan],
    "数学": [45, 65, 78, 45, np.nan, 88, 65],
    "英语": [34, 67, 89, 34, 90, 92, 67]
}
#练习一
df = pd.DataFrame(data)
df.to_csv('score.csv',encoding="utf-8",index=False)
df=pd.read_csv('score.csv',encoding="utf-8")
print("原始脏数据：\n", df)
print(df.isnull().sum())
df_fill=df.fillna({"语文":df["语文"].mean(),"数学":0})
#练习二
print("去重前：",len(df_fill))
df_fill1=df_fill.drop_duplicates(subset=["姓名","语文","数学"],keep="first").copy()
print("去重后：",len(df_fill1))
#练习三
gb=df_fill1.groupby("班级")
gb["语文"].mean()
gb["数学"].min()
gb["英语"].max()
#可以改进
#res = gb.agg(
#    语文平均分=("语文","mean"),
#    数学最低分=("数学","min"),
#    英语最高分=("英语","max")
#)
filter_df = gb.filter(lambda x:x["语文"].mean()>50)
print("语文均分>50班级所有学生：\n", filter_df)
df_fill1["班级语文平均分"]=gb["语文"].transform('mean')
#练习四
df_fill1.to_csv('clean_score.csv',encoding="utf-8",index=False)
clean_df=pd.read_csv("clean_score.csv",encoding="utf-8")
print(clean_df)