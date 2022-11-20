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





2002.11.20

版本： Alpha 0.1.5

增加了外航SCS的逻辑，包含邮件发送机制。
