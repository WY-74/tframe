# Requests环境
## **http_methods**
一个最为基础的请求方法. 为了避免手动输入可能造成的错误, 我们已经有了预设的method: `utils/data_sets.py::Method`, 因此当我们使用 `http_methods` 方法时可以通过调用 `Method` 传入 `method` 参数.

timeout我们也提供了预设的值: `utils/data_sets.py::TimeOut`, 且默认超时为3s, 若想要调整超时时间请通过调用 `TimeOut` 传入 `timeout` 参数.
- method: Method
- url: str
- params: Dict[str, str|int] | None
- headers: Dict[str, str|int] | None
- json_params: Dict[str, str | int] | None
- data_params: Dict[str, str | int] | None
- cookies: Dict[str, str | int] | None
- timeout: TimeOut

## **http_with_proxy**
为请求增加代理, `https`默认与`http`相同, `http`默认为 `127.0.0.1:8888`
- method: Method
- url: str
- http: str
- https: str|None

## **http_with_file**
一个处理上传文件接口的方法
- url: str
- path: str
- name: str
- filename: str

## **assert_status_code**
一个用于断言响应状态码的函数
- response(必填): Response
- e_status(必填): int

## **assert_json_response**
当我们希望断言响应数据，并且响应的数据是json结构时可以使用此函数. 
Json数据可能会存在嵌套的情况, 因此我们使用该函数的过程中需要借助JsonPath尽可能的解析Json, 我们提供了 [JsonPath](https://github.com/WY-74/fragmented-notes/blob/master/base/006.md) 相关文章来帮助您熟悉JsonPath.
- response: Response
- want: Any
- expr: str

## **assert_xml_response**
当响应返回的内容是XML时可以使用该方法验证. 目前我们提供的验证方法时匹配符合xpth的元素, 并将这些元素的文本信息存放到列表中, 判断我们期望的数据是否在列表中
- response: Response
- xpath: str
- want: str