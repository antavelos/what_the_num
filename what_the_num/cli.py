# -*- coding: utf-8 -*-

"""Console script for what_the_num."""

import click

from what_the_num import what_the_num as wtn


@click.command()
@click.argument('number')
@click.option("--trivia", "num_type", flag_value="trivia")
@click.option("--math", "num_type", flag_value="math")
@click.option("--date", "num_type", flag_value="date")
@click.option("--year", "num_type", flag_value="year")
def main(number, num_type):
    """Console script for what_the_num."""
    try:
        response = wtn(number, num_type)
    except Exception as e:
        click.echo(e)
        return 1

    for num, text in response.items():
        click.echo(num)
        click.echo(text)

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
