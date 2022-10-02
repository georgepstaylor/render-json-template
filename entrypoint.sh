#!/usr/bin/env sh

python render_json/render.py --template "{'some': 'thing', 'items': [1, 2, 3]}" --value "$.some" "things"
