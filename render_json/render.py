import json
import logging
from json import JSONDecodeError

import click

from render_json import template
from render_json.template import JSONPathParserError

logger = logging.getLogger(__name__)


class JSONTemplateRendorError(Exception):
    """Raised when any error occurs while rendering a JSON template"""


@click.command()
@click.option('--inject', type=(str, str), multiple=True)
@click.option("--template-string", required=True, help="Base JSON")
def render(template_string: str, inject: tuple[str, str]):
    try:
        rendered_json = json.loads(template_string)
        for path, value in inject:
            rendered_json = template.inject_value(rendered_json, path, value)
    except (JSONTemplateRendorError, JSONPathParserError) as ex:
        logger.error(str(ex))

    print(rendered_json)


def _load_json(json_str: str) -> dict:
    try:
        return json.loads(json_str)
    except (TypeError, JSONDecodeError) as ex:
        raise JSONTemplateRendorError(f"Invalid JSON provided: {ex}")


if __name__ == "__main__":
    render()
