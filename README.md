# tframe
我们提供了一些用于测试使用tframe的案例, 如您需要可查看: [test_tframe](https://github.com/WY-74/test_tframe.git)

## 环境文档
tframe中封装了多种测试常用第三方库, 详细的函数使用方法可在以下对应文章中查看
- [Requests](manual/pages/base_pages/requests.md)

## 框架结构介绍及命名规范
```
root
|___ data
|  |___ <模块名>
|     |___ __init__.py : 定义模块数据结构
|     |___ <模块名>_data.py : 存放模块用到的数据
|___ pages
|  |___ <模块名>
|     |___ __init__.py : 初始化对应环境的BasePage
|     |___ <模块名>_pages.py (需要继承BASE)
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

## 官方文档
- [Selenium](https://www.selenium.dev/documentation/)
- [Playwright](https://playwright.dev/python/)
- [Appium](https://appium.io/docs/en/2.0/)
- [Requests](https://requests.readthedocs.io/en/latest/#)
