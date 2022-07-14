import logging
import yaml

with open('logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger('sampleLogger')


def print_logs():
    logger.debug('SUB - This is a debug message')
    logger.info('SUB - This is a Cron message')
