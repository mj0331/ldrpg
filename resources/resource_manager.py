import json
from pathlib import Path, PosixPath


class ResourceManager:
    def __init__(self, data_root: Path, supported_json_resource_versions: list[int] = [1]):
        self.data_root = data_root
        self.resources = {}
        self.supported_json_resource_versions = supported_json_resource_versions

        print(f'[ResourceManager] Resource root: {self.data_root.absolute()}')
        self._load_resource(self.data_root)

    def _load_resource(self, resource_path: Path):
        for resource in resource_path.iterdir():
            if resource.is_dir():
                self._load_resource(resource)

            else:
                print(f'[ResourceManager] Loading resource: {resource}')
                match resource.suffix:
                    case '.json':
                        with open(str(resource), 'r') as f:
                            json_resource = json.load(f)

                            if not 'ldrpg_data_format' in json_resource:
                                print(f'[ResourceManager] No ldrpg_data_format in resource: {resource_path}')
                            elif (format_version := json_resource['ldrpg_data_format']) not in self.supported_json_resource_versions:
                                print(f'[ResourceManager] ldrpg_data_format version "{format_version}" not supported.\n'
                                      f'[ResourceManager] Supported versions: {self.supported_json_resource_versions}')

                            self.resources[str(resource.relative_to(self.data_root).with_suffix('').as_posix())] = json_resource
                    case _:
                        print(f'\tSkipping unsupported resource: {resource}')
