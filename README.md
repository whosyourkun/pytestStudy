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