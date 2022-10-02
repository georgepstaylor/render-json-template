import click


@click.command()
@click.option('--value', type=(str, str))
@click.option("--template", required=True, help="Base JSON")
def render(template: str, value: tuple[str, str]):
    print(template)


if __name__ == "__main__":
    render()
