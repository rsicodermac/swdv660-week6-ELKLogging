import logging
import logstash
import sys
from random import randint

test_logger = logging.getLogger('python-application-log')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler('52.87.166.15', 5959, version=1))

test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')

# add extra field to logstash message
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 2.53,
    'test_integer': randint(1,9),
    'test_list': [1, 2, 3],
}
test_logger.info('python-logstash: test extra fields', extra=extra)
