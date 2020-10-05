# Setup basic test using TDD

Make the required tests fail:

### `Engine` module: *DONE*

- `test_insert_data` for `insert_data(data)`
- `test_search` for `search(search_query)`

### `View` module: *DONE*

- `test_render` for `render(campers)`

### `Models` module:

#### `Camper` dataclass:

### `DataStore` module :

#### `DictionaryStore` class: *DONE*

- `test_upsert_data` for `upsert_data(data)`
- `test_upsert` for `upsert(row_object)`
- `test_filter` for `filter(filter_predicate)`

#### `DataStoreAccess` module: *DONE*

- `test_populate_campers` for `populate_campers(store, data)`
- `test_find_campers_around` for `find_campers_around(store, position)`

Out-of-scope (won't implement) but typically found here:

- `test_add` for `add(store, camper)`
- `test_get` for `get(store, camper_id)`
- `test_modify` for `modify(store, camper_id, changes)`
- `test_remove` for `remove(store, camper_id)`

### `Geometries` module:

#### `Point` NamedTuple *DONE*

- `test_valid_point` for `valid()`
- `test_bounding_box` for `bbox(bbox_diff)`
- `test_within` for `within(bbox)`

#### `BoundingBox` NamedTuple *DONE*

- `test_valid_bbox` for `valid()`

