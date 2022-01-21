import logging
import logging.handlers
from syslog import LOG_USER
from urllib.parse import urlparse

LOG_FMT = r"%(asctime)s %(name)s[%(process)d] [%(levelname)s] %(message)s"
LOG_DATE_FMT = r"%Y-%m-%d %H:%M:%S"
LOG_DATE_SYSLOG_FMT = r"%b %d %H:%M:%S"


if __name__ == '__main__':
    logger = logging.getLogger('test')

    syslog_url = 'syslog://localhost:514?test'

    assert syslog_url.startswith('syslog://')

    info = urlparse(syslog_url)
    facility = LOG_USER

    if info.query in logging.handlers.SysLogHandler.facility_names:
        facility = info.query

    if info.netloc:
        address = (info.hostname, info.port or 514)
    else:
        address = info.path

    handler = logging.handlers.SysLogHandler(address=address, facility=facility)
    formatter = logging.Formatter(fmt=LOG_FMT, datefmt=LOG_DATE_SYSLOG_FMT)
    handler.setFormatter(formatter)
    logger.handlers = [handler]

    logger.info('GOOD')
