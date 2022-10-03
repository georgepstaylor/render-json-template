#!/usr/bin/env sh

python -m render_json.render --template-string '{"some": "thing", "items": [1, 2, 3]}' --inject "$.some" "things"
