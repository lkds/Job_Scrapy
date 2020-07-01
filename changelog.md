### 0.11 -latest
1.  添加Jsite字段，标识数据来源网站中文名 如拉钩网
2.  修改Jsource字段，表示职位链接，如果没有进入具体职位爬取，则不填

### 0.10 -latest
1.  更新了数据库与网站对应表，[查看](#site-sql)
2.  建立了相关数据库
3.  修改了README
### 0.9
1.  修改字段说明，请查看字段说明.md文件并按要求修改
2.  加入拉勾网，如遇到exscjs无法导入，执行pip install PyExecJs 安装

### 0.8
1.  修改数据库指定逻辑，在spider的__init__函数中（没有则自行创建）添加self.Jdb = {数据库名称} （具体查看[0.6版本表格](#site-sql)）标明数据库表名 不设置则默认为demo

### 0.7 
1.  添加代理开关，在爬虫的的__init__函数中（没有则自行创建）添加self.useProxy = True（False）标明是否使用 没加就是不使用代理

### 0.6 （已废弃，无效）
~~1.  item中添加数据表名Jdb，为每个爬虫单独建立表格存储数据，使用时请在每次循环中加入表名~~

```
job = JobItem()
for item in response.xpath("//div"):
    job['Jdb']='demo'
    ...
```
### 0.5
1.  添加JcomSize字段（公司规模），类型str

### 网站-数据库对应表
<span id = "site-sql"></span>
~~Boss直聘：boss~~
~~智联招聘：zlzp~~
51Job：51job
猎聘网：lp
中聘网：cnzp
~~大街网：dj~~
58同城：58job
拉勾网: lagoujob