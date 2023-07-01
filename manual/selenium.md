# Selenium环境
- 路径: `pages/base_pages`
- `self.driver`: 实例化的driver
- `self.split_symbol = "@"`: 用于分隔的特殊字符
## open -> None
- 打开一个网址
- 参数: url
    - url -> str: 完整的url
## must_get_element -> WebElement
- 等待并返回一个元素, 若超时依旧没有找到期望元素则会报错: `missing valid locator or elements`
- 参数: locator, time_out
## must_after_cilck -> WebElement
- 在一定时间内反复点击一个按钮直到出现期望元素并返回, 若未找到按钮会报`未找到元素`; 若未找到点击后的期望元素会报错: `[Err]: the button or expected element is not found`
- 参数: button_locator, target_locator, time_out:
    - button_locator: 待点击按钮的定位器, 
    - target_locator: 第二个字符串是期望点击后出现元素的定位器
## scroll_and_click -> None
- 滑动到元素并点击, 当定位器定位到多个元素时只会点击第一个元素
- 参数: eol
    - eol -> str|WebElement: 待点击的元素或该元素的定位器
## get_element_by_text -> WebElement
- 找到第一个文本符合期望文本的元素
- 参数: locator, text
    - text -> str: 期望文本
## get_element_by_childtext -> WebElement|None
- 返回第一个字元素文本符合要求的父元素
- 参数: locator, child_locator, text, complete
    - child_locator -> str: 子元素的定位器
    - text -> str: 期望文本
    - complete -> bool: 判断文本时是否完全匹配, 默认为True
## get_attributes -> List[str]
- 以列表的形式返回一类元素的同一种属性值
- 参数: attr, eol
    - attr -> str: 属性名
    - eol -> str|List[WebElement]: 元素的定位器或存放元素的列表
## select_dropdown -> None
- 选择一个下拉列表中的元素
- 参数: box_locator, menu_locator, item
    - box_locator -> str: 下拉框的定位器
    - menu_locator -> str: 展开后整体列表的定位器
    - item -> str: 期望选择的列表中的条目的文本
## action_flow -> None
- 完成一系列点击, 输入, 下拉框选择的流程
- 参数: actions
## keyboard_enter -> None
- 在一系列流程结束以后模拟键盘的Enter键进行提交
- 参数: actions
