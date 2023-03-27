# MonitorCenter
python3.10+Django4.1.7+Mysql5.7
## 项目依赖
﻿asgiref==3.6.0
Django==4.1.7
mysqlclient==2.1.1
sqlparse==0.4.3
tzdata==2022.7



## 后端容器更新方式：

直接docker ps -a查看运行的容器

然后进入容器删除或者备份/opt内的后端代码

回到虚拟机docker cp 本地代码   容器ID:/opt

然后再进入容器执行django_run.sh脚本即可，日志在MonitorCenter内的monitor.logs