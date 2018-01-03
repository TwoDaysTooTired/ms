# model
## TeachMaterial
    id
    SerialNum
    MaterialName
    MaterialType :  Book workBook experimentEquipment other
    Inventorylimit
    InventoryNumber
    Note
    Price

 ## StudentInfo
    id
    studentId
    Name
    Gender
    Age
    Electivecourse（mtm）


# CourseInfo
    id
    SerialNum
    CourseName
    CourseMaterials(mtm)
    Note

 ## Grade
    id
    GradeName 
    MaxNum
    CourseInfos(mtm)




# 主要内容
## 管理员
1.登陆
2.录入学生信息，修改学生信息，删除学生信息
3.录入材料信息，修改，删除
4.录入课程信息，修改，删除
5.录入班级信息，修改，删除

6.材料入库
    数据结构
    record
    Materail(oto) num date note
7.班级材料分配

    MaterialAlloc
    Material(oto) num 
    record
    id(privekey) grade(oto) MaterialAlloc(mtm) data note allnum
8。入库记录，分配记录

## 学生注册选课
1.注册
2.登陆
3.选课


# 步骤
### 安装python
    打开 https://www.python.org/downloads/ 下载python3 最新版本
    

