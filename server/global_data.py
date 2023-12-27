from typing import Dict


class GlobalData:
    def __init__(self):
        self._data = {}
        self._file_path = None

    def reload_data(self, data: Dict):
        self._data = data

    def reload_from_file(self, file_path: str):
        self._file_path = file_path
        from json import loads
        try:
            with open(file_path, 'r') as f:
                self.reload_data(loads(f.read()))
        except FileNotFoundError:
            # we ignore the error here
            pass

    def dump(self) -> Dict:
        return self._data

    def to_file(self, filename: str):
        from json import dumps
        json_dump = dumps(self.dump())
        with open(filename, 'w') as f:
            f.write(json_dump)

    def dump_to_file(self):
        self.to_file(self._file_path)

    def create_or_clear_namespace(self, namespace: str):
        self._data[namespace] = {
            "user1": {
                "name": "John",
                "surname": "Brook"
            },
            "user2": {
                "name": "Jane",
                "surname": "Packer"
            }
        }.copy()
        self.dump_to_file()

    def add(self, namespace: str, key: str, value):
        self._data[namespace][key] = value
        self.dump_to_file()

    def emplace(self, namespace: str, data: Dict):
        self._data[namespace] = data
        self.dump_to_file()

    def get(self, namespace) -> Dict:
        if namespace not in self._data.keys():
            self.create_or_clear_namespace(namespace)
        return self._data[namespace]

# A dict of users.
GLOBAL_DATA = GlobalData()
