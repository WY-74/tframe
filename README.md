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

## Selenium封装
- 路径: `pages/tool`
- 常用到的参数结构():
    - actions: 包含一个或多个键值对的字典
        - 当是需要进行输入时, 键必须是以"_input"结尾的字符串, 值应该写为"locator@text", locator为该元素定位器, text为待输入文本, 以@作为分隔。
        - 当是需要进行点击时, 键必须是以"_click"结尾的字符串, 值应该写为"locator", locator 为该元素定位器。
```python
actions = {
    "search_input": "locator@text",
    "search_click": "locator"
}
```
### 2.1 action_flow
完成一系列点击输入的流程
- actions

### 2.2 get_attributes
以列表的形式返回一类元素的同一种属性值
- data: 传入一个包含定位器和属性名的字符串, 用 @ 分隔
```python
data = "locator@attr"
```

### 2.3 cilck_until
在一定时间内反复点击一个按钮直到出现期望元素或超时, 若找到期望元素会将期望元素返回
- locators:
    - 数据类型: tuple[str, str]
```python
locators = ("被点击按钮的css-selector定位器", "期望点击后出现的元素的css—selector定位器")
```
- time_out(可选参数, 默认为10s):
    - 数据类型: int


### 2.4 模拟键盘相关操作
#### 2.4.1 keyboard_enter
在一系列输入点击流程结束以后模拟键盘的Enter键进行提交
- 参数: actions

## 官方文档
- [Selenium](https://www.selenium.dev/documentation/)

