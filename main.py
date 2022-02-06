import image_scraper
import argparse
from dp_challange_web_scraper import Scraper


parser = argparse.ArgumentParser(
    description='DP Challenge web scraper')


# meta args-- directing sub process
parser.add_argument('--api_key', default=None, type=str,
                    help='api key for scrapapi')
parser.add_argument('--get_meta', action='store_true',
                    help='if entered will retrieve site data, can be resumed')
parser.add_argument('--get_images', action='store_true',
                    help='will store full size images')

args = parser.parse_args()


if __name__ == '__main__':
    if args.api_key:
        print(args.api_key)
        scrape = Scraper(args.api_key)
    if args.get_meta:
        scrape.get_data_dict()
