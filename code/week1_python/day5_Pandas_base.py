import pandas as pd
import numpy as np
#练习一
s=pd.Series(["lisi","www","wdwe"],index=[2012,2013,2014])
df=pd.DataFrame({
    "姓名":['王五','张三','李四','钱器','黄毛'],
    "语文":[12,21,34,56,90],
    "数学":[45,65,78,98,88],
    "英语":[34,67,89,90,92]
},index=[11,22,33,44,55])
print(df.head(2))
print(df.shape)
print(df.columns.tolist())
#练习二
print(df.loc[11])
print(df.loc[[22,33],["姓名","数学"]])
print(df.iloc[[0,2],[1,3]])
print(df.loc[11:33, "姓名"])
#练习三
print(df[df["语文"]>85])
print(df[(df["数学"]>90)&(df["英语"]>80)])
print(df[(df["语文"]<60)|(df["数学"]>95)])
df["总分"]=df[["数学","语文","英语"]].sum(axis=1)
print(df[df["总分"]>240])
#训练四
df.to_csv("student_score.csv",encoding="utf-8",index=False)
df_part = pd.read_csv("student_score.csv", usecols=["语文", "英语"], encoding="utf-8")
print(df_part)