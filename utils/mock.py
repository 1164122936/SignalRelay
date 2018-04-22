'''
测试接口

+ 随机生成数据字节流用于功能测试
'''
from random import random

def mock_test_relay():
    '''
    测试步骤1

    + 报文格式: NR;CV 2174.0;OV 0.0;\r\n
    :return: 模拟报文字符流
    '''
    return 'NR;CV {cv};OV {ov};\r\n'.format(
        cv=random(), ov=random()
    ).encode()

def mock_test_touch(m):
    '''
    测试步骤2

    :param m: 触点个数

    + 报文格式: NR;CT ...(ct*n);OT ...(ot*n);NCR ...(ncr*n);NOR ...(nor*n);\r\n
    :return: 模拟报文字符流
    '''
    return 'NR;CT {ct};OT {ot};NCR {ncr};NOR {nor};\r\n'.format(
        ct=' '.join(str(random()) for _ in range(m)),
        ot=' '.join(str(random()) for _ in range(m)),
        ncr=' '.join(str(random()) for _ in range(m)),
        nor=' '.join(str(random()) for _ in range(m))
    ).encode()