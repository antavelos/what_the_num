# -*- coding: utf-8 -*-

"""Console script for what_the_num."""

import click


@click.command()
def main(args=None):
    """Console script for what_the_num."""
    click.echo("Replace this message by putting your code into "
               "what_the_num.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
