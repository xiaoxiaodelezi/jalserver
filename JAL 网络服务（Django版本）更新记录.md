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

在traffic中添加了外航scs筛选的子模块，初步写了逻辑。逻辑有些不足：1.分批重量没有涵盖进去 2.mail部分也没有联动进去。初步写好了templates，但具体动态实现还没有联动