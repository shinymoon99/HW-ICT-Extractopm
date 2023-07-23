# HW-ICT-EventExtraction
使用一个嵌套实体识别模型来识别论元，然后用一个“首-首”匹配和“尾-尾”匹配模型来构建论元之间的关系
## 环境配置
```
pip install -r requirements.txt
```
## 运行方法


直接运行duee_v1.py即可
## 模型的下载地址
[google drive](https://drive.google.com/open?id=1ykENKV7dIFAqRRQbZIh0mSb7Vjc2MeFA)
### tip
对应的模型其实在huggingface里有，但找到的模型好像只支持tensorflow2，而作者说tensorflow2有运行风险。我运行的模型是在github上的替代模型。

|[huggingface上的模型](https://huggingface.co/hfl/chinese-roberta-wwm-ext)|
[github上的模型](https://github.com/brightmart/roberta_zh)|
