from jsonpath_ng.exceptions import JsonPathLexerError, JsonPathParserError
from jsonpath_ng.ext import parse as parse_json_path


class JSONPathParserError(Exception):
    """Raised when parsing of a JSON path fails"""


def inject_value(json: dict, json_path: str, value: any) -> dict:
    """
    Injects a value into the given JSON at the JSON path specified

    :param json: Dict representing the JSON to be altered according to the given path and value
    :param json_path: JSON path where value should be injected.
    :param value: Value to be injected
    :return: Dict resulting from value being injected

    :raises: ValueError if the JSON path is invalid or the value cannot be serialized
    """
    try:
        return parse_json_path(json_path).update(json, value)
    except (JsonPathLexerError, JsonPathParserError) as ex:
        raise JSONPathParserError(str(ex))
