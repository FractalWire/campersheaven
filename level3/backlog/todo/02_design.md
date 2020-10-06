# Design modification

Now that we need to do some sort of join-like query on the datastore, we need a
more robust datastore implementation.

We could use something comparable to a foreign key using `weakref`.
One store could have `weakref` on another datastore row.

That way, we can query a model and have all the informations needed. When the
referenced row is deleted from the original datastore it will be automatically
garbage collected in the linked datastore.

Note: This is only true if GC is triggered. This means we could have some
dangling ref when querying a datastore.

### Implementation

For the actual assignment this means:

- a new model `Calendars` with its row being potentially linked to `Campers`
- `Campers` will be modified by adding a new field `calendars` of type `WeakSet`.
This imply to make models `dataclass` `frozen` so that they can be hashable.

- add a new store for the Engine, that will be referenced when accessing
  `Datastores`
- new method `populate_store` in `DatastoreAccess` also replace
  `populate_campers`

- `DictionaryStore` need a way to know in which other linked `DictionaryStore`
  to reference a row

### Important note

The actual design do not truly respect a MVC pattern.

As of now, the `Engine`  has too nuch responsabilities. It acts as the
Controller but also overlap the Model responsability in some way as it also have
the responsability to start the whole thing.

For it to be a true Controller, datastore reference should not be kept there at
all.

I will not dig too deep into that.

