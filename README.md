## 基于Scrapy的爬虫项目集合

利用Scrapy对国内的相关网站进行爬取，获取之业信息
### site
* [拉勾网](https://www.lagou.com/)
* [BOSS直聘](https://www.zhipin.com/?city=100010000&ka=city-sites-100010000)
* [51Job](https://www.51job.com/)
* [猎聘网](https://www.liepin.com/)
* [中聘网](https://www.cnzp.cn/)
* [大街网](https://www.dajie.com/)
* [智通人才网](http://www.job5156.com/)

### 开发
* 进入job目录，cd job
* 创建爬虫 scrapy genspider 网站名 域名
* 编写爬虫，必须实现items中所有字段的填充，没有也要设为空''或0(参考数据库字段类型)
