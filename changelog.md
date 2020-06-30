### 0.7 -latest
1.  添加代理开关，在爬虫的的__init__函数中（没有则自行创建）添加self.useProxy = True（False）标明是否使用 没加就是不使用代理

### 0.6
1.  item中添加数据表名Jdb，为每个爬虫单独建立表格存储数据，使用时请在每次循环中加入表名
```
job = JobItem()
for item in response.xpath("//div"):
    job['Jdb']='demo'
    ...
```
Boss直聘：boss
智联招聘：zlzp
51Job：51job
猎聘网：lp
中聘网：cnzp
大街网：dj
智通人才网：ztrc

### 0.5
1.  添加JcomSize字段（公司规模），类型str