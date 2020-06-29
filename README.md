## Scrapy爬虫基本框架

### 功能
* 代理池：已集成，无需配置
* 存储到MySQL

### 配置
1.  使用Navicat登录远程数据库创建数据表（IP密码数据库在pipelins.py中找）
2.  修改pipelines.py中的连接配置，主要是数据表名称
3.  编写爬虫和相关代码，参考pipelines中的写入方法（pymysql）

### 运行