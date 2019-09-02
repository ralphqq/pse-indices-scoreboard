# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from main_board.models import MarketIndex, ValueUpdate


class MarketNotInSession(Exception):
    """Exception raised when market is not open."""
    pass


class IndexScraperPipeline(object):
    def process_item(self, item, spider):
        try:
            if (not ValueUpdate.is_open() and 
                    item['market_status'] != 'OPEN' and 
                    spider.db_mode == 'save'):
                raise MarketNotInSession
            market_index = MarketIndex.objects.get(name=item['name'])
        except MarketIndex.DoesNotExist:
            logging.log(
                logging.ERROR,
                'Unknown index name or ticker'
            )
        except KeyError as e:
            logging.log(logging.ERROR, e)
        except MarketNotInSession:
            logging.log(
                logging.INFO,
                'Market currently not in session'
            )
        else:
            val_update = market_index.valueupdate_set.create(
                current_value = item['current_value'],
                points_change = item['points_change'],
                percent_change = item['percent_change'],
                market_status=item['market_status']
            )
            logging.log(
                logging.INFO,
                f'Saved update for {val_update.market_index.name} to db'
            )

        return item
