import image_scraper
import argparse
from dp_challange_web_scraper import Scraper


parser = argparse.ArgumentParser(
    description='IAQA research software using CUHK-PQ, AVA and IAD')


# meta args-- directing sub process
parser.add_argument('--api_key', default=None, type=str,
                    help='api key from hugging_face account')
parser.add_argument('--get_meta', action='store_true',
                    help='if entered will retrieve site data, can be resumed')
parser.add_argument('--login', action='store_true',
                    help='if entered will try to sen .csv')
parser.add_argument('--make', action='store_true',
                    help='create_new hf project')
parser.add_argument('--train', action='store_true',
                    help='create_new hf project')

args = parser.parse_args()


if __name__ == '__main__':
    if args.api_key:
        print(args.api_key)
        scrape = Scraper(args.api_key)
    if args.get_meta:
        scrape.get_data_dict()
