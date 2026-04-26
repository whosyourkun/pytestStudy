This is for learning the pytest framework.

## 常用参数：

- -v：增加详细程度
- -s：捕获IO
- -x：快速退出
- -m：用例筛选

## 标记：

用户自定义标记 只能实现用例筛选
pytest --markers可以查看标记
pytest -m markerName 运行对应标记用例

### 1. 用户自定义标记

#### 步骤

1. 先注册
2. 再标记
3. 后筛选

### 2. 框架内置标记

框架内置标记 为用例增加特殊执行效果

和用户自定义标记区别：

1. 不需要注册
2. 不仅可以筛选，还可以增加特殊效果
3. 不同的标记
    - skip:无条件通过
    - skipif:有条件跳过
    - xfail：预期失败
    - parameterize：参数化
    - usefixtures：使用fixtures

数据驱动测试=参数化测试+数据文件
根据数据文件的内容，动态决定用例的数量、内容


## 夹具
夹具:在用例执行之前、执行之后，自动运行代码
场景:
- 之前:加密参数/之后:解密结果
- 之前:启动浏览器/之后:关闭浏览器
- 之前:注册、登录账号/之后:删除账号
### 1. 创建fixture
  1. 创建函数
  2. 添加装饰器
  3. 添加yield关键字
### 2. 使用fixture
  1. 在用例的参数列表中，加入fixture名字即可
  2. 给用例加上pytest.mark.usefixtures("funcName“)
### 3. 高级用法
  1. 自动使用
        pytest.fixture(autouse=True)
  2. 依赖使用
        1. linux:使用linux进行编译
        2. git:使用git进行版本控制
        3. fixture:使用fixture进行前后置自动操作
  3. 返回内容:接口自动化封装：接口关联
  4. 范围共享
     - 默认范围：function
     - 全局范围：session
       - 使用conftest.py

## 插件管理

插件分为两类：
- 不需要安装的：内置插件
- 需要安装的：第三方插件

插件的启动管理：
- 启用： -p abc使用abc插件 
- 禁用： -p no:abc不使用abc插件

插件的使用方式：
1. 参数
2. 配置文件
3. fixtures
4. mark

## 常用第三方插件
pytest有1400+个插件：https://docs.pytest.org/en/stable/reference/plugin_list.html
### 1. pytest-html
用途：生成HTML测试报告
安装：pip install pytest-html  
使用：pytest --html=report.html --self-contained-html  
可以在pytest.ini中添加addopts参数
### 2. pytest-xdist
用途：分布式执行
安装：pip install pytest-xdist
使用：-n N  N为同时有多少线程个并行
- 只有在任务本身耗时较长，超度调用成本很多的时候，才有意义
- 分布式执行，有并发问题：资源竞争、乱序
### 3. pytest-rerunfialures
用途：用例失败之后，重新执行
安装：pip install pytest-rerunfailures
使用： --reruns 5 --reruns-delay 1 重新执行5次 重试和重试之间间隔1秒
### 4. pytest-result-log
用途：把用例的执行结果记录到日志文件中  
使用：
- 1og_file = ./logs/pytest.1og
- 1og_file_level = infolog_file_format = %(levelname)-8s %(asctime)s [%(name)s:%(1ineno)s] :%(message)s1og_file_date_format = %Y-%m-%d %H:%M:%s
;记录用例执行结果
- result_log_enable = 1  
;记录用例分割线
- result_log_separator = 1  
;分割线等级
- result_log_level_separator = warning  
;异常信息等级
- result_log_level_verbose = info  

**建议使用logging/loguru,此插件比较老**
### 5. 企业级测试报告
1. allure 是一个测试报告的框架
   - 安装：pip install allure-pytest
   - 配置：--alluredir=temps --clean-alluredir
   - 生成报告：allure generate -o report -c temps
   - allure支持对用例进行分组和关联
   - allure支持对用例进行分组和关联(敏捷开发术语)
     - @allure.epic 史诗 项目
     - @allure.feature 主题 模块
     - @allure.story 故事 功能
     - @allure.title 标题 用例  
     **使用相同装饰器的用例，自动并入一组**