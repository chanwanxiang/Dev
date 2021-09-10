### Scrapy爬虫框架

#### scrapy框架简介

scrapy框架是用纯python实现一个为了爬取网站数据、提取结构化数据而编写的应用框架

#### scrapy架构图示

![image-20210405103223600](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210405103223600.png)

![image-20210405103349896](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210405103349896.png)

#### 安装

> pip install scrapy

#### 新建scrapy项目

创建爬虫项目

> scrapy startproject 项目名称

创建爬虫文件

> scrapy genspider 文件名称 域名

启动爬虫项目

> scrapy crawl name

#### Sample 斗鱼图片获取