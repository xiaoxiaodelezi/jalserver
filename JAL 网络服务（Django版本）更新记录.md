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



