#!/usr/bin/env bash

JSON_FILE_PATH=$1
FIELD_VALUE_PAIRS=$2

echo "::notice ::Output file ${JSON_FILE_PATH}"

OUTPUT_FILE_PATH="$(echo $RANDOM | md5sum | head -c 10; echo;).${JSON_FILE_PATH}"


python -m render_json.render \
  --json-file-path "${JSON_FILE_PATH}" \
  --field-value-pairs "${FIELD_VALUE_PAIRS}" \
  --output-file-path "${OUTPUT_FILE_PATH}"
