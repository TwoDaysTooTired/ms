# model
## Material
    id                  编号（主键）
    SerialNum           材料编号（唯一）
    MaterialName        材料名
    MaterialType :  Book workBook experimentEquipment other （材料类型）
    InventoryLimitNum   最大库存
    InventoryNum        库存数量
    Note                备注
    Price               价格

 ## StudentInfo
    id                  编号
    SerialNum           学号
    Name                姓名
    Gender              性别
    Age                 年龄
    Electivecourse      选修课
    Email               邮箱
    Tel                 电话号码
    Grade               班级
    Note                备注

# Course
    id                  编号
    SerialNum           课程编号
    Name                课程名
    Materials           教学材料
    Type                课程类型（choices=(室内,练习，视屏)）
    Note                课程描述

 ## Grade
    id                  编号
    SerialNum           班级编号
    GradeName           班级名
    LimitNum            最大人数
    Courses             基础课程
    AllocNum            已分配数
    Note                班级描述



## MaterialStorageRecord
    Num                 数量
    Material            材料
    Data                日期时间

## MaterialAllocateRecord
    Num                 数量
    Material            材料
    Data                日期时间

# 主要内容
## 管理员
1.管理登陆
2.录入学生信息，修改学生信息，删除学生信息
3.录入材料信息，修改，删除
4.录入课程信息，修改，删除
5.录入班级信息，修改，删除

6.材料入库
    选择教材添加数量
7.材料分配
    选择班级分发教材
    
8。入库记录，分配记录
    查看教材的炒作记录

## 学生注册选课
1.注册
    管理员添加新的学生信息时添加学生账号，默认密码123456 ，用户名为学号
    
2.登陆
3.选课


# 步骤
### 安装python
    打开 https://www.python.org/downloads/ 下载python3 最新版本,
    下载使用pycharm IDE，按章django
    

