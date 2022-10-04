#!/usr/bin/env sh

JSON_FILE_PATH=$1
FIELD_VALUE_PAIRS=$2


OUTPUT_FILE_PATH="$(tr -dc A-Za-z0-9 </dev/urandom | head -c 13 ; echo '').${JSON_FILE_PATH}"

python -m render_json.render \
  --json-file-path "${JSON_FILE_PATH}" \
  --field-value-pairs "${FIELD_VALUE_PAIRS}" \
  --output-file-path "${OUTPUT_FILE_PATH}"

echo "::set-output name=rendered-json-file::${OUTPUT_FILE_PATH}"
