import unittest

from programytest.storage.asserts.store.assert_maps import MapStoreAsserts

from programy.storage.stores.sql.store.maps import SQLMapsStore
from programy.storage.stores.sql.engine import SQLStorageEngine
from programy.storage.stores.sql.config import SQLStorageConfiguration

import programytest.storage.engines as Engines


class SQLMapsStoreTests(MapStoreAsserts):

    @unittest.skipIf(Engines.sql is False, Engines.sql_disabled)
    def test_initialise(self):
        config = SQLStorageConfiguration()
        engine = SQLStorageEngine(config)
        engine.initialise()
        store = SQLMapsStore(engine)
        self.assertEqual(store.storage_engine, engine)

    @unittest.skipIf(Engines.sql is False, Engines.sql_disabled)
    def test_map_storage(self):
        config = SQLStorageConfiguration()
        engine = SQLStorageEngine(config)
        engine.initialise()
        store = SQLMapsStore(engine)

        self.assert_map_storage(store)

    @unittest.skipIf(Engines.sql is False, Engines.sql_disabled)
    def test_upload_from_text(self):
        config = SQLStorageConfiguration()
        engine = SQLStorageEngine(config)
        engine.initialise()
        store = SQLMapsStore(engine)

        self.assert_upload_from_text(store)

    @unittest.skipIf(Engines.sql is False, Engines.sql_disabled)
    def test_upload_text_files_from_directory_no_subdir(self):
        config = SQLStorageConfiguration()
        engine = SQLStorageEngine(config)
        engine.initialise()
        store = SQLMapsStore(engine)

        self.assert_upload_text_files_from_directory_no_subdir(store)

    @unittest.skip("CSV not supported yet")
    def test_upload_from_csv_file(self):
        config = SQLStorageConfiguration()
        engine = SQLStorageEngine(config)
        engine.initialise()
        store = SQLMapsStore(engine)

        self.assert_upload_from_csv_file(store)

    @unittest.skip("CSV not supported yet")
    def test_upload_csv_files_from_directory_with_subdir(self):
        config = SQLStorageConfiguration()
        engine = SQLStorageEngine(config)
        engine.initialise()
        store = SQLMapsStore(engine)

        self.assert_upload_csv_files_from_directory_with_subdir(store)

