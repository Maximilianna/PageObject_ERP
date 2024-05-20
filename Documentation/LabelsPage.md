类 LabelsPage

```
Object
└─ BasePage
    └─ LabelsPage
```
子类：

MessagePage

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

| 特有方法                     | 说明                       |
|--------------------------|--------------------------|
| close_labels(*labelName) | 关闭指定页面,若未指定默认关闭当前页面      |
| Page_name()              | 需要子类重写,返回当前页面名字,默认返回空字符串 |