#!/usr/bin/env sh

JSON_FILE_PATH=$1
FIELD_VALUE_PAIRS=$2

echo "${FIELD_VALUE_PAIRS}"

python -m render_json.render --json-file-path "${JSON_FILE_PATH}" --field-value-pairs "${FIELD_VALUE_PAIRS}"
