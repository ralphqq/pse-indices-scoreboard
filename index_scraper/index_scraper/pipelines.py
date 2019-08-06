# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from main_board.models import MarketIndex, ValueUpdate


class IndexScraperPipeline(object):
    def process_item(self, item, spider):
        try:
            market_index = MarketIndex.objects.get(name=item['name'])
        except (MarketIndex.DoesNotExist, KeyError):
            pass
        else:
            val_update = market_index.valueupdate_set.create(
                current_value = item['current_value'],
                points_change = item['points_change'],
                percent_change = item['percent_change']
            )

        return item
