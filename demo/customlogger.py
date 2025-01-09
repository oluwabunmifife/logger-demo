from prometheus_client import Counter
import logging

log_counters = {
    'INFO': Counter('django_log_info_total', 'Total number of INFO logs'),
    'WARNING': Counter('django_log_warning_total', 'Total number of WARNING logs'),
    'ERROR': Counter('django_log_error_total', 'Total number of ERROR logs'),
}

class PrometheusLogHandler(logging.Handler):
    def emit(self, record):
        log_level = record.levelname
        if log_level in log_counters:
            log_counters[log_level].inc()