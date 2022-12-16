JAL 网络服务（Django版本）更新记录



2022.11.15

版本：Alpha 0.1.1

包含三个子项目

django项目名称为jalservice

cargo包含货运部分

homepage处理主页



逻辑处理方面

desk项目增加了进港特殊货物，templates部分只有jsp，具体逻辑可能还需要修改。后续版本更新。

FR部分增加了cargosalesreport比对逻辑





2022.11.16

版本：Alpha 0.1.2

将reservation和accouting合并

在traffic中添加了外航scs筛选的子模块，初步写了逻辑。逻辑有些不足：1.分批重量没有涵盖进去 2.mail部分也没有联动进去。初步写好了templates，但具体动态实现还没有联动。



2022.11.18

版本：Alpha 0.1.3

外航scs的模块增加了邮件运单的输入，分批重量问题解决。scs_result的templates还在考虑如何写



2022.11.19

版本：Alpha 0.1.4

cargo项目中新增了两个文件夹

file_templates用来存放文件模板

file_pool用来作为临时文件夹的总目录，每个临时文件夹用uuid4生成名字，用来存放每次功能运行需要的文件实例

cargo的func函数增加了3个函数

send_mail 发送邮件的模块

mk_templates 在file_pool中生成一个临时文件夹的函数

auxiliary_instance 通过调用辅材模板xlsx来生成一个辅材模板的实例，存在临时文件夹中





2022.11.20

版本： Alpha 0.1.5

增加了外航SCS的逻辑，包含邮件发送机制。



2022.11.21

版本： Alpha 0.1.6

从webserver中移植了uldstorage到项目中。





2022.11.21

版本：Alpha 0.1.7

从webserver中移植了crosscheck到项目中。



2022.11.22

版本：Alpha 0.1.8

重新考虑了特殊货物部分的逻辑函数返回部分。只是修改了逻辑函数，返回值和对应的templates还没有修改好。



2022.11.23

版本：Alpha 0.1.9

特殊货物的逻辑函数部分重写完成，templates完成了修改，但也只做了JSP一个类别作为参考。具体什么形式的templates还需要经过和相关部门讨论才能最终决定。



2022.11.24

版本：Alpha 0.1.9.1

尝试特殊货物result的templates的修改，不太满意。



2022.11.25

版本：Alpha 0.1.10

给外航的保函申请项目：和相关部门确认了信息的格式，在views中添加了sendmail的try except结构，增加了result的templates反馈两个邮件发送结果。



2022.11.26

版本：Alpha 1.0.0

添加了uwsgi相关信息。



2022.11.26

版本：Alpha 1.0.1

修改uwsgi相关信息。



2022.11.26

版本：Alpha 0.1.11

uwsgi设置失败，删除uwsgi的相关内容，重新回到0.1版本。



2022.11.27

版本：Alpha 0.2

uwsgi配置调试完成



2022.11.27

版本：Alpha 0.2.1

nginx适配完成，uwsgi改为socket，但项目需要在服务器上切换chdir内容。



2022.11.28

版本：Alpha 0.2.2

特殊货物添加了val、hum、avi



2022.11.29

版本：Alpha 0.2.3

重写了特殊货物result的templates



2022.11.30

版本：Alpha 0.2.4

重写了特殊货物result的templates

JPH现在归为温控货物。

AVI,JCA,JPH,BUP,COL,等测试由于数据量少，暂时还没有办法进行。需要在随后的工作中进行追踪。



2022.11.30

版本：Alpha 1.0

添加了server.ini作为在服务器上启动uwsgi的文件



2022.12.1

版本：Alpha 1.0.1

修改了scs发送的地址



2022.12.1

版本：Alpha 1.1.0

增加了cargo的数据库 Airport，导入了所有US的空港三字代码



2022.12.2

版本：Alpha 1.1.1

特殊货物templates增加了中转，JCA和JPH的标注，去掉了温控货物关于整板的选择。





2022.12.3

版本：Alpha 1.1.2

修正了外航保函中目的港提取的bug



2022.12.3

版本：Alpha 1.1.3

修正了中专卡车的信息提取bug，修改了特殊货物result templates的反馈



2022.12.3

版本：Alpha 1.1.4

修正了specialcodelist的要给bug



2022.12.4

版本：Alpha 1.1.5

修复了外航保函航班筛选中的一个bug，同时增加了ups的5X航班的筛选方法。



2022.12.5

版本：Alpha 1.1.6

修改了进港特殊货物result的templates



2022.12.6

版本：Alpha 1.1.6.1

检查了5x的反馈的bug，在自己系统上没有问题。





2022.12.7

版本：Alpha 1.1.6.2

修改了func中的几个形参和函数中的参数，避免和str混淆



2022.12.8

版本：Alpha 1.1.7

新建了test_file文件夹，用来做一些新项目的尝试。

考虑出发特殊代码时的第一次尝试逻辑上有不足。



2022.12.9

版本：Alpha 1.1.8

在cargo中增加了notallowedcargo项目，用来检验出发货物中是否有可疑物品

从ari cargo manifest中获取的信息包括是否存在可疑物品和主分单的出发港，达到港信息，用来以后处理分单中国家代码和主单不一致的匹配。

新建了相关的两个templates，但还需要进一步优化。



2022.12.10

版本：Alpha 1.1.9

在sales对比中增加了pdf和excel的对比。

目前只写了对比逻辑。



2022.12.10

版本：Alpha 1.1.9.1

在sales对比中增加了pdf和excel的对比。（需要注意的是目前excel是xlsx版本，需要销售自己从xls调整位xlsx）

salse report的pdf和excel对比已经经过测试，写入了func。upload templates完成， result templates目前还没有完成。

另外notallowedcargo的resutl templates也还没有完成。



2022.12.11

版本：Alpha 1.1.9.2

完成了sales中pdf和excel对比的templates。



2022.12.11

版本：Alpha 1.1.9.3

完成了traffic csp部分的可疑物品检查，但对应的国家等目前还没有想好逻辑。



2022.12.12

版本：Alpha 1.1.10

cargosalescheck 增加了2个excel的比对。



2022.12.12

版本：Alpha 1.1.10.1

修正了git上传的时间



2022.12.13

版本：Alpha 1.1.10.2

小bug修正。



2022.12.15

版本：Alpha 1.1.10.3

修正了品名中带有dep-dtn这类字符导致的正则匹配问题。



2022.12.16

版本：Alpha 1.1.11

增加了两个模型。

special_uld：用来筛选需要特别注意的uld

country：国家全名和缩写的对应表，用来将来核对用

向airport模型导入了数据。

在总目录下新建了一个文件夹related_documents用来存放相关的一些数据。

