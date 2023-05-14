# tframe
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
    - mac：Google\ Chrome -–remote-debugging-port=9000
    - windows：chrome -–remote-debugging-port=9000
- 完成上述操作后执行代码即可

## 常用数据结构
**注意**: 此节阐述命名将会在下文中保持一致
- actions: 包含一个或多个键值对的字典
    - 当是需要进行输入时, 键必须是以"_input"结尾的字符串, 值应该写为"locator@text", locator为该元素定位器, text为待输入文本, 以@作为分隔。
    - 当是需要进行点击时, 键必须是以"_click"结尾的字符串, 值应该写为"locator", locator 为该元素定位器。
```python
actions = {
    "search_input": "locator@text",
    "search_click": "locator"
}
```

## Selenium封装
- 路径: `pages/base_pages`
### 1.1 get_attributes
以列表的形式返回一类元素的同一种属性值
- 参数: data
    - data: 传入一个包含定位器和属性名的字符串, 用 @ 分隔
```python
data = "locator@attr"
```
### 2.1 cilck_until_find
在一定时间内反复点击一个按钮直到出现期望元素或超时, 若找到期望元素会将期望元素返回
- 参数: locators, time_out:
    - locator: 传入包含两个字符串的元祖, 第一个字符串是待点击按钮的定位器, 第二个字符串是期望点击后出现元素的定位器
    - time_out: int, 可选参数, 默认为10s
```python
locators = ("button_locator", "expectation_element_locator")
```
### 3.1 action_flow
完成一系列点击输入的流程
- 参数: actions
### 4.1 keyboard_enter
在一系列输入点击流程结束以后模拟键盘的Enter键进行提交
- 参数: actions


## 可用装饰器
- 路径: `utils/decorator`
### 1.1 exception_capture
可装饰在测试用例上, 该装饰器会帮助我们在执行测试用例过程中捕捉异常, 并保存发生异常时的浏览器截屏(log/screenshot)以及HTML源码(log/page_source)。

*后续需要结合logging 以及 allure 完善该方法*

## 官方文档
- [Selenium](https://www.selenium.dev/documentation/)

