# Implement code based on design


### Models

- new model `Calendar` *DONE*
- new field `calendars` to `Camper` model of type `WeakSet` *DONE*

- models are now frozen

### Engine

- new `DictionaryStore` `calendar` *DONE*

### DataStoreAccess

- new generalist method `populate_store(store, data)`

### DictionaryStore

- FK mechanism:
  - new `ForeignKeyDictionaryStore` `NamedTuple(foreign_store,
    fk_column_name)`
  - `DictionaryStore` as a new `foreign_keys` attribute
  - `upsert` behaviour modification:
    - add the new row to the linked `DictionaryStore` if any
    - fail to upsert if no match in the linked `DictionaryStore`
