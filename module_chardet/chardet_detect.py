import logging
import sys

import chardet

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


if __name__ == '__main__':
    s = '这里是一个测试ID'
    gb18030 = s.encode('gb18030')
    gbk = s.encode('gbk')
    utf8 = s.encode('utf8')

    logging.info('%s', chardet.detect(gb18030))
    logging.info('%s', chardet.detect(gbk))
    logging.info('%s', chardet.detect(utf8))
