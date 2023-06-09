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

## 相关配置
- 框架依赖库安装 `pip install -r requirements.frozen`
- playwright相关依赖: `python -m playwright install`
- Chrome复用环境:
    - 找到Chrome启动路径
        - mac的启动路径通常为: `/Applications/Google\ Chrome.app/Contents/MacOS`
        - windows可通过右键查看程序属性, 属性中的 `目标(不包含最后的\chrome.exe)` 即为启动路径
    - 将启动路径配置到环境变量中, 并重启终端
- appium环境依赖
    - [安装JDK](https://github.com/WY-74/fragmented-notes/blob/master/base/002.md)
    - [安装SDK](https://github.com/WY-74/fragmented-notes/blob/master/base/003.md)
    - 安装Node.js
    - 安装Appium Server: `sudo npm install -g appium`
    - 安装环境监测工具: `sudo npm install -g appium-doctor`

## 命令行功能
**注意:** 支持pytest所有的命令行功能
### 通用命令
#### --suite
框架内包含了Selenium, Playwright和Appium, 因此可以通过设置`--suite`切换模块(目前Playwright和Appium还未完全加入, 只是提供了切换入口)
- 我们必须在执行时进行设置:
```shell
python -m pytest <路径> --suite=selenium
```
```shell
python -m pytest <路径> --suite=playwright
```
```shell
python -m pytest <路径> --suite=appium
```
#### --web
此参数是在控制我们所启用的浏览器或手机平台, 但可用的参数值取决于suite的设置
当`suite==Selenium/Playwright`时可设置:
```shell
python -m pytest <路径> --suite=selenium --web=Chrome
```
```shell
python -m pytest <路径> --suite=selenium --web=Firefox
```
当`suite==appium`时可设置(**注意:** 实例化appium之前您可以在 `utils/capabilities.py` 中设置capability参数):
```shell
python -m pytest <路径> --suite=appium --web=Android
```
```shell
python -m pytest <路径> --suite=appium --web=Ios
```
### Selenium/Playwright可用命令
#### --headless
我们可以让程序在无头模式下执行
- 默认是不会进入到无头模式执行程序的, 当我们期望通过无头模式执行程序请设置:
```shell
python -m pytest <路径> --suite=selenium --headless=True
```
#### --debugger
在框架中提供了便捷使用debugger_address的方法, 前提是我们需要配置浏览器为可复用状态
- **特别注意**: 在使用前关闭所有Chrome已有进程
- 该功能默认是关闭状态, 若想开启请在执行命令时设置
```shell
python -m pytest <路径> --suite=selenium --debugger=True
```
#### --remote
本框架提供了capabilities+分布式的执行方式, 目前的环境为: https://selenium-node.hogwarts.ceshiren.com/ui#, 这仅仅是为了测试入口, 后期我们会搭建属于自己的分布式环境
- 默认不会进行分布式执行, 因此但我们需要在某个节点进行分布式执行时需要先配置 `utils/capabilities.py`
- 并且在执行程序时设置:
```shell
python -m pytest <路径> --suite=selenium --remote=True
```
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


## Selenium环境
- 路径: `pages/base_pages`
- `self.driver`: 实例化的driver
- `self.split_symbol = "@"`: 用于分隔的特殊字符
### open -> None
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
### scroll_and_click -> None
- 滑动到元素并点击, 当定位器定位到多个元素时只会点击第一个元素
- 参数: eol
    - eol -> str|WebElement: 待点击的元素或该元素的定位器
### get_element_by_text -> WebElement
- 找到第一个文本符合期望文本的元素
- 参数: locator, text
    - text -> str: 期望文本
### get_element_by_childtext -> WebElement|None
- 返回第一个字元素文本符合要求的父元素
- 参数: locator, child_locator, text, complete
    - child_locator -> str: 子元素的定位器
    - text -> str: 期望文本
    - complete -> bool: 判断文本时是否完全匹配, 默认为True
### get_attributes -> List[str]
- 以列表的形式返回一类元素的同一种属性值
- 参数: attr, eol
    - attr -> str: 属性名
    - eol -> str|List[WebElement]: 元素的定位器或存放元素的列表
### select_dropdown -> None
- 选择一个下拉列表中的元素
- 参数: box_locator, menu_locator, item
    - box_locator -> str: 下拉框的定位器
    - menu_locator -> str: 展开后整体列表的定位器
    - item -> str: 期望选择的列表中的条目的文本
### action_flow -> None
- 完成一系列点击, 输入, 下拉框选择的流程
- 参数: actions
### keyboard_enter -> None
- 在一系列流程结束以后模拟键盘的Enter键进行提交
- 参数: actions

## Playwright环境
**注意:** Playwright当前并未完全被封装, 因此我们目前只是提供了切换Selenium和Playwright的入口, 后续我们会持续封装Playwright, 保证只通过 `--suite` 就可以随意切换不影响各个函数名

## Appium环境

## Requests环境
### **http_methods**
- method(必填) -> Method: 请求方法【 GET | POST | PUT | DELETE 】
- url(必填) -> str: URL
- params -> Dict[str, str|int] | None: 传递url参数信息
- headers -> Dict[str, str|int] | None: 传递请求头信息
- json_params -> Dict[str, str | int] | None: 传递json请求体信息

一个最为基础的请求方法. 为了避免手动输入可能造成的错误, 我们已经有了预设的method: `utils/data_sets.py::Method`, 因此当我们使用 `http_methods` 方法时可以通过调用 `Method` 传入 `method` 参数.
### **assert_status_code**
- response(必填) -> Response: 传入一个响应对象
- e_status(必填) -> int: 传入该响应预期的状态码

一个用于断言响应状态码的函数

### **assert_json_response**
- response(必填) -> Response: 传入一个响应对象
- want -> Dict[str, str | int]= {}: 传入一组期望的数据
- key -> str: 传入一个唯一的关键字
- value -> str|int: 唯一关键字的对应数值

当我们希望断言响应数据，并且响应的数据是json结构时可以使用此函数. 
    
json的响应提被映射为python可用数据对象之后会有两种情况, 一种为列表另一种为字典.

当为列表时, 往往列表中的每一组元素都有一唯一的可辨别的键值对, 我们可以传入 `key` 和 `value` 来锁定该组元素

当为字典时则无需 `key` 和 `value` 辅助

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
- [Playwright](https://playwright.dev/python/)
- [Appium](https://appium.io/docs/en/2.0/)
- [Requests](https://requests.readthedocs.io/en/latest/#)

