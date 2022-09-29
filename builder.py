from typing import Optional, Callable

import utils

CMD_TO_FUNCTION: dict[str, Callable] = {
    'filter': utils.filter_query,
    'map': utils.map_query,
    'sort': utils.sort_query,
    'unique': utils.unique_query,
    'limit': utils.limit_query,
    'regex': utils.regex_query
}

FILE_NAME = 'data/apache_logs.txt'


def build_query(cmd: str, param: str, data: Optional[list[str]]) -> list[str]:
    if data is None:
        with open(FILE_NAME) as file:
            prepared_data: list[str] = list(map(lambda x: x.strip(), file))
    else:
        prepared_data = data

    return CMD_TO_FUNCTION[cmd](param=param, data=prepared_data)
