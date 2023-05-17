# tframe
## 可拓展框架结构及命名规范
```
root
|___ data
|  |___ <模块名>
|     |___ <模块名>_data.py
|___ pages
|  |___ <模块名>
|     |___ <模块名>_pages.py (需要继承base_pages.py 中的 BasePages 类)
|___ testcases
|  |___ <模块名>
|     |___ test_<模块名>.py (需要继承base_test.py 中的 BaseTest 类)

测试类命名需要以 Test 开头, 测试函数命名需要以 test_ 开头
```

## 环境配置
### 1.1 debugger
在框架中提供了便捷使用debugger_address的方法,因此我们需要配置浏览器为可复用状态
#### 1.1.1 配置浏览器环境
- 找到Chrome启动路径
    - mac的启动路径通常为: `/Applications/Google\ Chrome.app/Contents/MacOS`
    - windows可通过右键查看程序属性, 属性中的 `目标(不包含最后的\chrome.exe)` 即为启动路径
- 将启动路径配置到环境变量中, 并重启终端
#### 1.1.2 使用
- **特别注意**:在使用前关闭所有Chrome已有进程
- 启动/关闭debugger():
    - **注意:** 我们通过临时设置环境变量以决定debugger是否生效。这意味着当重启终端之后配置便会失效(推荐使用这种方法设置环境变量, 因为我们不希望总以debug的方式运行代码)。
    - mac:
        - 启动: `export CHROME_DEBUG=1`
        - 关闭: `重启终端` 或者 `unset CHROME_DEBUG`
    - windows:
        - 启动: `set CHROME_DEBUG=1`
        - 关闭: `重启终端` 或者 `set CHROME_DEBUG=`
- 命令行启动浏览器
    - mac：`Google\ Chrome --remote-debugging-port=9000`
    - windows：`chrome -–remote-debugging-port=9000`
- 完成上述操作后执行代码即可

## 常用数据结构
**注意**: 此节阐述命名将会在下文中保持一致
- actions -> Dict[str, str]: 包含一个或多个键值对的字典
    - 当是需要进行输入时, 键必须是以"_input"结尾的字符串, 值应该写为"locator@text", locator为该元素定位器, text为待输入文本, 以@作为分隔。
    - 当是需要进行点击时, 键必须是以"_click"结尾的字符串, 值应该写为"locator", locator 为该元素定位器。
    - 当需要操作一个下拉框列表时, 键必须是以"_dropdown"结尾的字符串, 值应该写为"box_locator@menu_locator@attr"。box_locator为下拉框的定位器, menu_locator为下拉列表整体的定位器, attr为希望选择的选项的文本文字, 三者以@作为分隔。
```python
actions = {
    "test_input": "locator@text",
    "test_click": "locator",
    "test_dropdown": "box_locator@menu_locator@attr"
}
```
- locator -> str: 元素的定位器。
```python
locator = "locator"
```
- time_out -> int: 通常作为可选参数, 用来控制等待的时长, 默认为10s。


## Selenium封装
- 路径: `pages/base_pages`
- `self.driver`: 实例化的driver
- `self.split_symbol = "@"`: 用于分隔的特殊字符
### open
- 打开一个网址
- 参数: url
    - url -> str: 完整的url
### must_get_element -> WebElement
- 等待并返回一个元素, 若超时依旧没有找到期望元素则会报错: `missing valid locator or elements`
- 参数: locator, time_out
### must_after_cilck -> WebElement
- 在一定时间内反复点击一个按钮直到出现期望元素并返回, 若未找到按钮会报`未找到元素`; 若未找到点击后的期望元素会报错: `[Err]: the button or expected element is not found`
- 参数: button_locator, target_locator, time_out:
    - button_locator: 待点击按钮的定位器, 
    - target_locator: 第二个字符串是期望点击后出现元素的定位器
### click_element -> None
- 找到元素并点击
- 参数: web
    - web -> str|WebElement: 待点击的元素或该元素的定位器
### get_element_by_text -> WebElement
- 找到第一个文本符合期望文本的元素
- 参数: locator, text
    - text -> str: 期望文本
### get_attributes -> List[str]
- 以列表的形式返回一类元素的同一种属性值
- 参数: attr, web
    - attr -> str: 属性名
    - web -> str|List[WebElement]: 元素的定位器或存放元素的列表
### select_dropdown -> None
- 选择一个下拉列表中的元素
- 参数: box_locator, menu_locator, item
    - box_locator -> str: 下拉框的定位器
    - menu_locator -> str: 展开后整体列表的定位器
    - item -> str: 期望选择的列表中的条目的文本
### action_flow
- 完成一系列点击, 输入, 下拉框选择的流程
- 参数: actions
### keyboard_enter -> None
- 在一系列流程结束以后模拟键盘的Enter键进行提交
- 参数: actions


## 可用装饰器
- 路径: `utils/decorator`
### exception_capture
可装饰在测试用例上, 该装饰器会帮助我们在执行测试用例过程中捕捉异常, 并保存发生异常时的浏览器截屏(log/screenshot)以及HTML源码(log/page_source)。

*后续需要结合logging 以及 allure 完善该方法*
### save_cookies
当我们需要保存cookie时可以使用该装饰器, 该装饰器会在被装饰函数执行完毕之后获取cookie并存储(./cookies.yaml)。
### load_cookies
当我们需要读取cookie时可以使用该装饰器, 该装饰器会在被装饰函数执行完毕之前获取cookie(./cookies.yaml)。

## 官方文档
- [Selenium](https://www.selenium.dev/documentation/)

