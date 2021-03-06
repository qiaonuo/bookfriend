# bookfriend(书友)

## 概览

> 用framework7实现的一个web-app，帮助用户方便的借到想看的书，以书会友。


## 目录说明
总共有三个子项目，其目录分别为：
* backend：后端项目，提供restful-api，用法参考其目录下 [README.MD](https://github.com/sniperyen/bookfriend/tree/master/backend)
* frontend: 前端项目，页面的展示，用法参考其目录下的 [README.MD](https://github.com/sniperyen/bookfriend/tree/master/frontend)
* book_scrapy: 爬虫，爬取网上的图书信息，用法参考其目录下的 [README.MD](https://github.com/sniperyen/bookfriend/tree/master/book_scrapy)

其它目录说明：
* docs: 相关设计文档
* prototype: app原型

## 需求分析

帮助用户方便的借到想看的书,只要有可以借出的书,每个人就是一个私人图书馆.

* 用户人群是哪些?
* app吸引人的功能点在哪里?
* 如何鼓励用户上传以及借出自己的书
* 如何在微信中传播?

![图书馆](https://raw.githubusercontent.com/sniperyen/bookfriend/master/docs/%E5%9B%BE%E4%B9%A6%E9%A6%86.jpg)

## UML(UML在作业部落中用markdown写的，这里显示不正常)

### 注册登录方式

用户可以注册自己的账号，也可以通过微信联合登录，时序图如下所示：

```seq
用户->应用服务器: 请求微信联合登陆
应用服务器->微信服务器: 发送请求到微信服务器
微信服务器-->用户: 调用用户微信客户端
用户->用户: 是否允许此次的登陆
Note right of 微信服务器: 此步骤可能有问题。。
用户->微信服务器: 允许登陆
微信服务器-->应用服务器: 返回用户的登陆token
应用服务器->应用服务器: 存储用户token
应用服务器-->用户: 登陆成功
```

### 借书流程

方式一：
甲在平台上查找到书本，向某一个拥有者（乙）发送借书请求。
```seq
甲->平台: 我要向乙借一本书（书名）
平台->乙: 借阅通知：甲想借这本书，您愿意借给他吗？ 
乙-->平台: 我愿意借书给甲
平台-->甲: 乙愿意借书给您
甲->乙: 沟通借书方式，快递或当面？
乙-->平台: 书已经借给甲，要求甲确认
甲->平台: 我已经收到了书，阅读中
平台->乙: 甲已确认，阅读中
```

方式二：
甲可以在平台上发布借书请求，平台向多个拥有同一本书的用户（乙、丙）广播借书请求，如果乙同意借书给甲，则系统需要推送消息给其它用户（丙），告知这次借阅已成功，这样丙则无需再关注这次借书请求。
```seq
甲->平台: 我想借一本书（书名）
平台->平台: 获取到这本书的拥有者列表(乙、丙)
平台->乙: 借阅通知：甲想借这本书，您愿意借给他吗？ 
平台->丙: 借阅通知：甲想借这本书，您愿意借给他吗？ 
乙-->平台: 我愿意借书给甲
平台-->甲: 乙愿意借书给您
甲->乙: 沟通借书方式，快递或当面？
乙-->平台: 书已经借给甲，要求甲确认
平台-->甲: 请确认乙已经把书借给了您
甲->平台: 我已经收到了书，阅读中
平台->乙: 甲已确认，阅读中
平台->丙: 甲已经借到了书，谢谢您的参与
```

### 还书流程
```seq
甲->平台: 我已经看完书，请求归还书本
平台->乙: 甲已经看完书，请求归还\n注意在收到书后点击“已归还”
甲->乙: 沟通归还方式（快递或当面）
甲->平台: 书已归还
平台->乙: 甲的书已归还，请确认是否收到了书
乙-->平台: 确认已收到
平台-->甲: 乙已经确认收到，此次借阅完成


```

## 开发计划
### 第一期

* 图书的爬取
* 用户的注册和登陆(微信联合登陆)
* 图书的上传与展示
* 搜索周边的用户或图书
* 借书
* 还书
* 添加好友
* 私信

### 后期

* 读书打卡功能,并可以分享到朋友圈
* 线下活动
* 公共图书馆图书借阅
* 找不到的图书,导流到线上书店购买

## 涉及到相关技术

前后端分离,后端只是提供api,前端通过ajax调用,然后通过vue来双向绑定数据.

### 后端
* web框架: django + restfulapi
* 消息的推送: 没想好。。
* 数据库: sqlite(后期迁移到mysql)

### 前端
* [framework7](http://framework7.cn/)
* [vue](http://cn.vuejs.org/)

## 竞品分析
* 书乡

## 参考文章
第一次使用framework7和vue.js,尝试前后段分离的开发方式,参考了许多文章,也学习了很多东西,把觉得有价值的文章链接粘贴在下面,供参考:

* [我们为什么要尝试前后端分离](https://segmentfault.com/a/1190000006240370)
* [从MVC到前后端分离（REST-个人也认为是目前比较流行和比较好的方式）](http://blog.csdn.net/shaobingj126/article/details/49420145)
