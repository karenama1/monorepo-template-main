import unittest
from gilded_rose import GildedRose, Item

class GildedRoseTest(unittest.TestCase):
    def test_general_item_behavior(self):
        # Arrange
        items = [Item("General Item", 10, 20)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual("General Item", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19,items[0].quality)

    def test_aged_brie_item(self):
        # Arrange
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_sulfuras_item(self):
        # Arrange
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_passes_item(self):
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_conjured_item(self):
        # Arrange
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)

        # Act
        gilded_rose.update_quality()

        # Assert
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

if __name__ == '__main__':
    unittest.main()

