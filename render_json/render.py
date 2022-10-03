import json
import logging
from json import JSONDecodeError

import click
from jsonpath_ng.exceptions import JsonPathLexerError, JsonPathParserError
from jsonpath_ng.ext import parse as parse_json_path

logger = logging.getLogger(__name__)


class JSONTemplateRenderError(Exception):
    """Raised when any error occurs while rendering a JSON template"""


class JSONPathParserError(Exception):
    """Raised when parsing of a JSON path fails"""


@click.command()
@click.option('--field-value-pairs', required=True)
@click.option("--json-file-path", required=True, help="Path to base JSON file")
def render(json_file_path: str, field_value_pairs: str):
    try:
        with open(json_file_path) as f:
            rendered_json = json.load(f)
        for path, value in _parse_key_value_blob(field_value_pairs).items():
            rendered_json = inject_value(rendered_json, path, value)
    except (FileNotFoundError, JSONDecodeError, JSONPathParserError, JSONTemplateRenderError) as ex:
        logger.error(f"{ex.__class__.__name__} occurred: {ex}")
        exit(1)

    print(rendered_json)


def inject_value(json_dict: dict, json_path: str, value: any) -> dict:
    """
    Injects a value into the given JSON at the JSON path specified

    :param json_dict: Dict representing the JSON to be altered according to the given path and value
    :param json_path: JSON path where value should be injected.
    :param value: Value to be injected
    :return: Dict resulting from value being injected

    :raises: ValueError if the JSON path is invalid or the value cannot be serialized
    """
    try:
        return parse_json_path(json_path).update(json_dict, value)
    except (JsonPathLexerError, JsonPathParserError) as ex:
        raise JSONPathParserError(str(ex))


def _parse_key_value_blob(blob: str) -> dict:
    key_value_dict = {}
    non_empty_lines = [line for line in blob.split("\n") if line]
    for line in non_empty_lines:
        [key, value] = line.split(":", maxsplit=1)
        key_value_dict.update({
            key.strip(): value.strip()
        })
    return key_value_dict


if __name__ == "__main__":
    render()
