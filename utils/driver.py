'''
测试驱动模块

+ 以subprocess调动测试exe从标准输出流获取测试结果并解析
'''

from utils.protocol import (
    process, simple, multiple
)
from utils.mock import (
    mock_test_relay, mock_test_touch
)

def test_relay():
    '''
    测试继电器
    :return: 吸合电压/释放电压
    '''
    return simple(process(mock_test_relay()))


def test_touch():
    '''
    测试触点
    :return: 吸合时间/释放时间/常闭电阻/常开电阻
    '''
    m = 8
    return multiple(process(mock_test_touch(m)), m)