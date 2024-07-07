# Render JSON Template GitHub Action

This action renders a given JSON template according to the field and values passed as inputs.

## Usage

```yaml
- uses: georgepstaylor/render-json-template@v0.0.3
  with:
    # Path to JSON file serving as the template for rendering an output file. Required.
    json-file-path: path/to/file.json
    
    # Multi-line string containing key/value pairs of JSON property paths and desired property values
    field-value-pairs: |
       $.some.path: "value"
       $.some.items: [1, 2, 3]
```

## Outputs

### `rendered-json-file`

Path to file containing JSON rendered from the base file provided, and injected with the key/value pairs provided.

## Example Usage

This example below displays the contents of the rendered file in the action output. It assumes that a file exists at the root of the repository containing this workflow named `test.json`, containing valid JSON.

```yaml
on:
  push:
    branches:
      - main

jobs:
  render-test-json:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v3
      - id: render
        uses: georgepstaylor/render-json-template@v1
        with:
          json-file-path: test.json
          field-value-pairs: |
            $.some: "things"
            $.items: [1.7, "hello"]
      - run: |
          cat ${{ steps.render.outputs.rendered-json-file }}
```

## Reference

- This action is based on https://github.com/h2non/jsonpath-ng
- Supported JSON path syntax can be found at https://goessner.net/articles/JsonPath/
