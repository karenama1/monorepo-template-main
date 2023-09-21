import unittest
import json
from src.jsonapi import BetterEncoder, BetterDecoder 

class TestBetterEncoder(unittest.TestCase):

    def test_encode_complex(self):
        encoder = BetterEncoder()
        complex_number = complex(2.5, 3.7)
        encoded = encoder.encode_complex(complex_number)
        self.assertEqual(encoded, {"real": 2.5, "imag": 3.7})

    def test_encode_range(self):
        encoder = BetterEncoder()
        integer_range = range(1, 10, 2)
        encoded = encoder.encode_range(integer_range)
        self.assertEqual(encoded, {"start": 1, "stop": 10, "step": 2})

class TestBetterDecoder(unittest.TestCase):

    def test_decode_complex(self):
        decoder = BetterDecoder()
        encoded = {"__extended_json_type__": "complex", "real": 2.5, "imag": 3.7}
        decoded = decoder.decode_complex(encoded)
        self.assertEqual(decoded, complex(2.5, 3.7))

    def test_decode_range(self):
        decoder = BetterDecoder()
        encoded = {"__extended_json_type__": "range", "start": 1, "stop": 10, "step": 2}
        decoded = decoder.decode_range(encoded)
        self.assertEqual(list(decoded), list(range(1, 10, 2)))

if __name__ == '__main__':
    unittest.main()
