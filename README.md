## 基于Scrapy的爬虫项目集合

利用Scrapy对国内的相关网站进行爬取，获取之业信息
### site
* ~~[拉勾网](https://www.lagou.com/)~~拉胯了
* [智联招聘](https://www.zhilian.com/)
* [BOSS直聘](https://www.zhipin.com/?city=100010000&ka=city-sites-100010000)
* [51Job](https://www.51job.com/)
* [猎聘网](https://www.liepin.com/)
* [中聘网](https://www.cnzp.cn/)
* [大街网](https://www.dajie.com/)
* [智通人才网](http://www.job5156.com/)

### 开发
* **安装python模块 pip install -r requirements.txt**
* 进入job目录，cd job
* 创建爬虫 scrapy genspider 网站名 域名
* 编写爬虫，仅填充能够爬取的字段

### 字段说明
* 职位名称
    item['Jname'] = ''
* ~~薪水 已废弃 换成了最低薪资和最高薪资~~
    item['Jsalary'] = 0
* 地区
    item['Jarea'] = ''
* 值位类型
    item['Jtype'] = ''
* 职位要求
    item['Jrequirements'] = ''
* 公司名称
    item['Jcompany'] = ''
* 标签
    item['Jtag'] = ''
* 福利
    item['Jwelfare'] = ''
* 学历要求
    item['Jeducation'] = ''
* 经验要求
    item['Jexperience'] = ''
* 最低工资 类型为int
    item['JminSalary'] = 0
* 最高工资 均以k为单位，类型为int
    item['JmaxSalary'] = 0
* 每年多少薪资数据类型int
    item['JpayTimes'] = 0
* 公司类型
    item['JcomType'] = ''
* 招聘人数,因有“招人若干”之类的，所以为varchar
    item['JhireCount']='0'
