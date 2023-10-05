# -*- coding: utf-8 -*-
""" Using Strategy design pattern """

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemUpdateHandler:
    def update_item(self, item):
        pass
class GeneralItemUpdateHandler(ItemUpdateHandler):
    def update_item(self, item):
        if item.name == "General Item":
            # Implement quality and sell_in update logic for general items
            if item.quality > 0:
                item.quality -= 1

            item.sell_in -= 1

            if item.sell_in < 0 and item.quality > 0:
                item.quality -= 1
        else:
            super().update_item(item)


class AgedBrieUpdateHandler(ItemUpdateHandler):
    def update_item(self, item):
        if item.name == "Aged Brie":
            # Increase quality for Aged Brie
            if item.quality < 50:
                item.quality += 1

            # Decrease sell_in for all items
            item.sell_in -= 1

            # Increase quality again after the sell_by date
            if item.sell_in < 0 and item.quality < 50:
                item.quality += 1

class BackstagePassesUpdateHandler(ItemUpdateHandler):
    def update_item(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11:
                if item.quality < 50:
                    item.quality += 1
            if item.sell_in < 6:
                if item.quality < 50:
                    item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        self.handler_map = {
            "General Item": GeneralItemUpdateHandler(),
            "Aged Brie": AgedBrieUpdateHandler(),
        }

    def update_quality(self):
        for item in self.items:
            if item.name in self.handler_map:
                handler = self.handler_map[item.name]
                handler.update_item(item)
            else:
                self.update_quality_for_normal_item(item)

    def update_quality_for_normal_item(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            self.decrement_quality(item)
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_quality_for_backstage_passes(item)
            else:
                self.decrement_sell_in(item)
                if item.sell_in < 0:
                    if item.name != "Aged Brie":
                        self.decrement_quality(item)
                    else:
                        self.increment_quality(item)

    def decrement_quality(self, item):
        if item.quality > 0:
            item.quality -= 1

    def increment_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def decrement_sell_in(self, item):
        item.sell_in -= 1

    def update_quality_for_backstage_passes(self, item):
        if item.sell_in < 11:
            self.increment_quality(item)
        if item.sell_in < 6:
            self.increment_quality(item)
        self.decrement_sell_in(item)
        if item.sell_in < 0:
            item.quality = 0
