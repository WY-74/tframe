# 可用装饰器
- 路径: `utils/decorator`
## exception_capture
可装饰在测试用例上, 该装饰器会帮助我们在执行测试用例过程中捕捉异常, 并保存发生异常时的浏览器截屏(log/screenshot)以及HTML源码(log/page_source)。

*后续需要结合logging 以及 allure 完善该方法*
## save_cookies
当我们需要保存cookie时可以使用该装饰器, 该装饰器会在被装饰函数执行完毕之后获取cookie并存储(./cookies.yaml)。
## load_cookies
当我们需要读取cookie时可以使用该装饰器, 该装饰器会在被装饰函数执行完毕之前获取cookie(./cookies.yaml)。
