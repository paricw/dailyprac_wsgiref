from wsgiref.simple_server import make_server
# 导入编写的application函数
from web_helloworld import application

# 创建一个服务器，IP地址为空，端口是8000，传入函数application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()