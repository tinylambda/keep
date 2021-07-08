import logging


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %I:%M:%S %p',
)


class COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == '__main__':
    logging.info(f'{COLORS.WARNING}Warning: some thing unexpected happened')
    logging.info(f'{COLORS.FAIL}Error: bad !')
    logging.info(f'{COLORS.OKCYAN}OK')
    logging.info(f'{COLORS.OKGREEN}OK OK')

