import json
import sys
from datetime import date
import re
import os

if len(sys.argv) > 1:
    arr = []
    addresses = set()
    names = set()
    with open(sys.argv[1]) as json_file:
        for line in json_file:
            entry = json.loads(line)
            add_string = str(entry["address"])
            if add_string not in addresses:
                arr.append({"model": "search.Address", "fields": entry["address"]})
                addresses.add(add_string)
            entry["address"] = [entry["address"]["country"], entry["address"]["city"], entry["address"]["street"]]
            name = entry["name"].split()
            if not name[0].endswith("."):
                name.insert(0, "")
            name_string = str(name)
            if name_string not in names:
                arr.append({"model": "search.Name",
                            "fields": {"title": name[0], "first_name": name[1], "last_name": name[2]}})
                names.add(name_string)
            entry["name"] = [name[0], name[1], name[2]]
            entry["birthday"] = str(date.fromtimestamp(entry["birthday"]))
            entry["phone"] = re.sub(r"[()\-+]", "", entry["phone"])
            del(entry["id"])
            obj = {"model": "search.Person", "fields": entry}
            arr.append(obj)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "search/fixtures/people.json"), 'w') as out_file:
        json.dump(arr, out_file)
