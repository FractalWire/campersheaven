# Implement code based on design


### Models

- models are now frozen *DONE*

- new `isavailable(start_date, end_date)` for `Camper` *DONE*

- new model `Calendar` *DONE*
- new field `calendars` to `Camper` model of type `WeakSet` *DONE*
- new `isdaterange_overlaps(start_date, end_date)` for `Calendar` *DONE*

### Engine

~ - new `DictionaryStore` `calendar` *DONE* ~
- new `stores` list holding all the `DictionaryStore` *DONE*

### DataStoreAccess

- new generalist method `populate_store(store, data)` *DONE*
- new `find_available_campers(store, position, start_date,
  end_date)` *DONE*

### DictionaryStore

- FK mechanism: *DONE*
  - new `ForeignKeyDictionaryStore` `NamedTuple(foreign_store,
    fk_column_name)`
  - `DictionaryStore` as a new `foreign_keys` attribute
  - `upsert` behaviour modification:
    - add the new row to the linked `DictionaryStore` if any
    - fail to upsert if no match in the linked `DictionaryStore`
