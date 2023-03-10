# MonitorCenter
python3.10+Django4.1.7+Mysql5.7
## 项目依赖
﻿asgiref==3.6.0
Django==4.1.7
mysqlclient==2.1.1
sqlparse==0.4.3
tzdata==2022.7



## 更新进度20230309

新增系统信息管理表

MonitorCenter表新增obejec_id，计划作为指标对象缩写

admin路径可以新增指标信息以及系统信息

系统信息和监控对象两个类做了多对多关联，可以实现后面每个系统查看自己的指标

至于每个系统内单独指标启停，和监控对象选择还在考虑

注意：setting.py用的本地mysql地址，自己跑注意修改



首页新增系统信息展示

右上角超级管理员点击可以跳转到

## 更新进度20230310

页面增加系统信息查询页面修改了urls和views以及新增和修改了html

首页增加系统下拉框以及额外操作下拉框

view内增加一些数据表的查询，新增，m2m表的修改





