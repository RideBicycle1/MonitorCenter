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

