# Render JSON Template

This action renders a given JSON template according to the field and values passed as inputs.

## Testing

For testing the GitHub Action, we can use [act](https://github.com/nektos/act). After installing, here's what you'll
need to test locally:

1. Create a workflow in `.github/workflows`, for example `test.yaml`:
   
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
           with:
             token: ${{ secrets.GITHUB_TOKEN }}
         - uses: ./
           with:
             json-file-path: test.json
             field-value-pairs: |
               $.some: things
               $.items: hello
   ```
2. Create a test file, for example `test.json`:

   ```json
   {
     "some": "thing",
     "items": [1, 2, 3]
   }
   ```

3. Trigger the workflow with `act`:

   ```shell
   act
   
   # Or if you are on an Apple M1
   act -P ubuntu-22.04=ubuntu:22.04
   ```
