#列表推导式清洗训练文本
samples = ["如何QLoRA微调", "", "显存优化方案", " ", None, "RAG结合大模型"]
s=[x for x in samples if x is not None and x.strip()!=""]
print(s)
#filter + lambda 筛选高质量样本
scores = [9, 4, 7, 2, 8, 5, 10]
lis=list(filter(lambda x:x>=6,scores))
print(lis)
# zip + 字典推导式 构建问答训练集
user_input = ["显存不够怎么办", "什么是梯度检查点"]
model_ans = ["使用QLoRA轻量化微调", "减少训练时显存占用的技术"]
z=zip(user_input,model_ans)
dic={x:y for x,y in z}
print(dic)
#map + lambda 批量构造 Prompt
questions = ["怎么训练LoRA", "微调报错怎么解决", "小模型怎么部署"]
m=list(map(lambda x :"用户问题："+x,questions))
print(m)
#综合小流程（完整模拟数据集预处理）
#有瑕疵
texts = ["全参数微调", "", "LoRA微调", "   ", "QLoRA微调"]
quality = [7, 3, 9, 2, 8]
texts=[x for x in texts if x is not None and x.strip()!=""]
quality=list(filter(lambda x:x>=7,quality))
z1=zip(texts,quality)
m1=map(lambda x:f"训练文本:{x[0]}，质量分:{x[1]}",z1)#map(lambda x,y: ..., z1) 这个写法只能传 1 个可迭代对象
#正确写法（接收元组，用t[0] t[1]拆分）
print(list(m1))
#工程标准写法
txt = ["全参数微调", "", "LoRA微调", "   ", "QLoRA微调"]
score = [7, 3, 9, 2, 8]
zp=zip(txt,score)
clean=[p for p in zp if p[0].strip()!=""]
good=list(filter(lambda p: p[1] >= 7, clean))
res_map = map(lambda p: f"训练文本:{p[0]}，质量分:{p[1]}", good)
result = list(res_map)
print(result)