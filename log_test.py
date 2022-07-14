import logging
import logging.config
import yaml


class CronFilter(logging.Filter):
    def filter(self, record):
        # print('filtering!')
        return 'Cron' in record.msg


if __name__ == "__main__":
    with open('logging_config.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    logger = logging.getLogger('sampleLogger')

    logger.debug('This is a debug message')
    logger.info('This is a Cron message')

    import test_log_sub
    test_log_sub.print_logs()

    another_logger = logging.getLogger('anotherLogger')
    another_logger.info("Log from anotherLogger!")




