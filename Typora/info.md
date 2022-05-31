##  面签

###  一. 流程

![image-20210628170511943](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210628170511943.png)

###  二. 配置

> admin账户登录限制

redis:47.97.41.159  6379  FvDev@2020-yuuwei

PRE_LOCK_ACCOUNT+ 账号 
PRE_FAIL_PWD_TIMES+账号

> 客户话术回答错误被锁

FORBIDDEN_FOR_INCORRECT_ANSWER_BANK
FORBIDDEN_FOR_INCORRECT_ANSWER_CLIENTID

> 面签/排队日志路径

/usr/program/tomcat-fv-dev/logs/catalina.out
/usr/program/tomcat-fv-dev/log/zgfv/business

/home/fv-dev/logs-local/business
/opt/program/queue-svc/logs

> 排队公式

score - ((入队时间-队首入队时间)/1000/10)*3

入队时间-队首入队时间 = 毫秒 / 100 = 秒
队列配置客户排队时长权重值每10秒 + 3, 所以再除以10乘3

##  云上

### 一. 流程

![image-20210628170709641](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210628170709641.png)

### 二. 配置

账号信息测试环境

| NAME   |    PHONE    |  TITLE   |
| ------ | :---------: | :------: |
| 赵云静 | 18685443157 |  业务员  |
| 张江弘 | 18166764653 |  调查员  |
| 杨兰依 | 18608508857 |  审核员  |
| 陶俊杰 | 13984940855 | 勘验审批 |
| 帅剑锋 | 17708514146 | 勘验人员 |



账号信息正式环境

| NAME   |    PHONE    | TITLE  | BIZTYPE |
| ------ | :---------: | :----: | :-----: |
| 车肖   | 13233683600 | 业务员 |  车贷   |
| 李涵   | 15285117545 | 调查员 |  车贷   |
| 罗燕   | 13595383585 | 审核员 |  车贷   |
| 夏雨宇 | 18008500508 | 审核员 |  家装   |
| 张忠益 | 15329229399 | 调查员 |  家装   |
| 刘天利 | 17585959936 | 业务员 |  家装   |

PassWord ab@124578 | ab124578@

录单关键字段

```python
汽车分期 {
    是否电子签: 是
    业务模式: 组合
    业务品种编号: 4600002
}

家装分期 {
    是否电子签: 是
    业务模式: 保证
    业务品种编号: 简装
}
```

订单修改为==征信通过==状态设计表及字段

```sql
USE rm_guizhou_icbc_v3_test;

SELECT * FORM rm_order_info;

/*
order_number    字段查询修改订单
order_status    字段(1,3)状态改成(5)状态
investigate_id  字段写入18调查员张江弘
approve_id      字段写入19审核员杨兰依
credit_result   字段写入“征信查询通过”
order_no        字段可以按之前的订单复制一个然后更改后几位数字,不一致即可(ICBC20200441163602123002)
*/

SELECT * FROM rm_client_info;

/*
credit_message  字段 填入“风险预筛查通过，blaze策略0-建议通过”
credit_result   填入 0
*/

```

订单修改为==开卡成功==状态设计表及字段

```sql
SELECT * FORM rm_order_info;

/*
order_number    字段查询修改订单
sp_companyid    240304150327(渠道公司id)
order_status    8
card_result     放款成功
inspection_id   1241
inspection_approval_id  172
*/

```

测试环境修改面签装状态

```sql
# 云上数据
SELECT * FROM rm_order_info;
/*
sign_status == 1
*/


# 面签数据
SELECT * FROM order_info;
/*
remote_platno == A-013 云上分期
business_code == 01(车贷), 02(家装)

remote_number 改为预关联订单一致
loan_number 为贷款

*/
```



