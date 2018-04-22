'''
协议解析模块

+ 解析报文中的一行字节流
'''

def process(message: bytes):
    '''
    将字节流解析为字符串
    过滤内容使其容易被解析
    :param message: 
    :return: 预处理结果
    '''
    content = message.decode()
    content = content.replace(';', ' ')
    content = content.strip().split(' ')
    content.remove('NR')
    return content

def simple(content: str):
    '''
    只有单个测试结果的内容解析
    :param content: 预处理结果
    :return: 字典形式处理结果
    '''
    msg, _len = content, len(content)
    return {msg[i]: float(msg[i+1]) for i in range(0, _len, 2)}

def multiple(content: str, m: int):
    '''
    具有多个测试结果的内容解析
    :param content: 预处理结果
    :param m: 测试结果个数
    :return: 字典形式处理结果
    '''
    msg, _len = content, len(content)
    return {
        msg[i]: [float(x) for x in msg[i+1 : i+m+1]]
        for i in range(0, _len, m+1)
    }

