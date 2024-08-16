#!/usr/bin/env sh

JSON_FILE_PATH=$1
FIELD_VALUE_PAIRS=$2
OUTPUT_FILE_NAME=$3

OUTPUT_FILE_PATH="/github/workspace/${OUTPUT_FILE_NAME}"

python -m render_json.render \
  --json-file-path "${JSON_FILE_PATH}" \
  --field-value-pairs "${FIELD_VALUE_PAIRS}" \
  --output-file-path "${OUTPUT_FILE_PATH}"

echo "rendered-json-file=\${{ github.workspace }}/${OUTPUT_FILE_NAME}" >> $GITHUB_OUTPUT
