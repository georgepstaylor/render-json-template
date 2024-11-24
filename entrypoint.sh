#!/usr/bin/env sh

JSON_FILE_PATH=$1
FIELD_VALUE_PAIRS=$2
OUTPUT_FILE_NAME=$3

# if the directory /github/workspace exists, then assume that the script is running in a GitHub Action
# else assume that the script is running locally

if [ -d "/github/workspace" ]; then
    GHA="true"
    OUTPUT_FILE_PATH="/github/workspace/${OUTPUT_FILE_NAME}"
else
    GHA="false"
    mkdir -p /output
    OUTPUT_FILE_PATH="/output/${OUTPUT_FILE_NAME}"
fi

render template-json \
  --json-file-path "${JSON_FILE_PATH}" \
  --field-value-pairs "${FIELD_VALUE_PAIRS}" \
  --output-file-path "${OUTPUT_FILE_PATH}"

if [ "$GHA" = "true" ]; then
    echo "rendered-json-file-name=${OUTPUT_FILE_NAME}" >> $GITHUB_OUTPUT
else
    echo "rendered-json-file-name=${OUTPUT_FILE_NAME}"
    cat "${OUTPUT_FILE_PATH}"
fi
