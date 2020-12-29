from hidb import fileStoreDB

test_data = {
    "test1": "value",
    "test2": 12,
    "test3": [12, 23, 34],
}


class TestFilestoreDB:
    def test_one(self):
        db = fileStoreDB("./")
        db.create("test_data", test_data)
        self.assertEqual(db.read("test_data", test_data))
        self.assertIsInstance(db.read("test_data", dict))
        with self.assertRaises(KeyError):
            db.read("test_data2")

    def test_two(self):
        db = fileStoreDB("./")
        db.create("test_data", test_data)
        self.assertEqual(db.read("test_data", test_data))
        db.delete("test_data")
        with self.assertRaises(KeyError):
            db.read("test_data")
