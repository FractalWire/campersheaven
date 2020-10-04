# Setup basic test using TDD

Make the required tests fail:

### `Engine` module: *DONE*

- `test_insert_data` for `insert_data(data)`
- `test_search` for `search(search_query)`

### `View` module:

- `test_render` for `render(campers)`

### `Model` module:

- `test_updated_row` for `updated_row(row, changeset)`

#### `Camper` dataclass:

### `DictionaryStore` class:

- `test_insert_data` for `insert_data(data)`
- `test_upsert` for `upsert(row_object)`
- `test_filter` for `filter(filter_predicate)`

### `DataStoreAccess` module:

- `test_populate_campers` for `populate_campers(data)`
- `test_find_campers_around` for `find_campers_around(position)`

Out-of-scope (won't implement) but typically found here:

- `test_add` for `add(camper)`
- `test_get` for `get(camper_id)`
- `test_modify` for `modify(camper_id, changes)`
- `test_remove` for `remove(camper_id)`

### `Geometries` module:

#### `Point` NamedTuple

- `test_valid_point` for `valid()`
- `test_bounding_box` for `bbox(bbox_diff)`
- `test_within` for `within(bbox)`

#### `BoundingBox` NamedTuple

- `test_valid_bbox` for `valid()`

