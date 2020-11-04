import json

from campersheaven.engine import Engine
from campersheaven.datastore import DictionaryStore, ForeignKeyDictionaryStore
from campersheaven.models import Camper, Calendar


def main():
    print("=== WELCOME TO CAMPERSHEAVEN ==")
    print()

    camper_store = DictionaryStore("campers", Camper)

    calendar_fkds = ForeignKeyDictionaryStore(
            'camper_id', camper_store, 'calendars')
    calendar_store = DictionaryStore(
            "calendars", Calendar, foreign_keys=[calendar_fkds])

    engine = Engine(camper_store, calendar_store)
    print("Engine started...")
    print()

    with open("data/campers.json") as f:
        campers_data = f.read()
    with open("data/calendars.json") as f:
        calendars_data = f.read()
    with open("data/searches.json") as f:
        search_queries = f.read()

    print("New campers in sight...")
    engine.insert_data(campers_data)
    engine.insert_data(calendars_data)

    print("Searching for the right campers now...")
    print()
    search_results_json = engine.search(search_queries)

    with open('data/results.json', 'w+') as f, open('expected_results.json') as f_exp:
        indented_results = json.dumps(json.loads(search_results_json), indent=4)
        f.write(indented_results)
        f.write('\n')
        print(indented_results)

        f.seek(0)
        f_b = f.read()
        f_exp_b = f_exp.read()

        print(f_b)
        print(f_exp_b)
        assert f_b == f_exp_b

    print()
    print("=== GOOD BYE ===")
    print()


if __name__ == '__main__':
    main()
