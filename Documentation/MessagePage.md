类 MessagePage

```
Object
└─ BasePage
    └─ LabelsPage
        └─ MessagePage
```
子类：

ManagePage, BrandPage, CategoryPage, CompanyPage, WareHousePage

| 构造方法               | 说明           |
|--------------------|--------------|
| LabelsPage(driver) | 传入浏览器驱动，构造页面 |

| 方法                                  | 说明                              |
|-------------------------------------|---------------------------------|
| open(url)                           | 打开指定的网页，url是网页的网址或本地文件地址        |
| find_element(type)                  | 按照给定的键值对，定位并返回网页中的元素            |
| find_elements(type)                 | 按照给定的键值对，定位并返回网页中的元素，返回一个列表     |
| click_element(type)                 | 按照给定的键值对，点击定位到的元素               |
| click_elements(type,index)          | 按照给定的键值对，点击定位到的第index个元素        |
| input_element(type)                 | 按照给定的键值对，输入value到定位到的元素         |
| input_elements(type, value, index)  | 按照给定的键值对，输入value到定位到的第index个元素  |
| select_element(type, My_str)        | 按照给定的键值对，定位下拉框选择My_str选项        |
| alert_accept()                      | alert弹窗，选择确定                    |
| alert_dismiss()                     | alert弹窗，选择取消                    |
以上方法均继承自BasePage类

| 方法                       | 说明                       |
|--------------------------|--------------------------|
| close_labels(*labelName) | 关闭指定页面,若未指定默认关闭当前页面      |
| Page_name()              | 需要子类重写,返回当前页面名字,默认返回空字符串 |

以上方法继承自LabelsPage类

| 特有方法                                                | 说明                              |
|-----------------------------------------------------|---------------------------------|
| click_new()                                         | 点击新增按钮                          |
| click_query()                                       | 点击查询按钮                          |
| click_reset()                                       | 点击重置按钮                          |
| ul_input(Options, Input_Location, <br/>Li_Location) | 点击ul下拉框,点击对应的选项,Li_Location有默认值 |
| click_quick(Str)                                    | 输入next或prev,分页栏快速向后或向前          |
| click_quick_next()                                  | 分页栏快速向后                         |
| click_quick_prev()                                  | 分页栏快速向前                         |
| click_prev()                                        | 点击上一页                           |
| click_next()                                        | 点击下一页                           |
| click_number(number)                                | 点击指定页数                          |
| input_pagination_editor(value, *key)                | 输入页数快速跳转到指定页数 默认不回车,key为1回车     |
| input_records(value)                                | 输入每页显示多少条记录                     |
| click_data_modify(index)                            | 点击修改记录                          |
| click_data_switch(index)                            | 点击禁用或启用记录                       |
| data_switch_accept()                                | 启用或禁用弹窗选择确定                     |
| data_switch_dismiss()                               | 启用或禁用弹窗选择取消                     |
| click_save()                                        | 点击保存按钮                          |
| click_cancel()                                      | 点击取消按钮                          |
| input_add_name(Name)                                | 新增记录输入名字                        |
| input_modify_name(Name)                             | 修改记录输入名字                        |
| into_page()                                         | 进入当前页面                          |
| input_query_name(Name)                              | 输入查询记录名字                        |
| input_query_status(Option)                          | 输入查询记录当前状态                      |
