#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `what_the_num` package."""

from click.testing import CliRunner

from what_the_num import utils
from what_the_num import cli


def test_date_data():
    # edge cases
    assert utils.is_date('-1/19') is False
    assert utils.is_date('1/39') is False
    assert utils.is_date('13/12') is False
    assert utils.is_date('13/32') is False
    assert utils.is_date('a3/r2') is False

    # happy cases
    for i in range(1, 13):
        for j in range(1, 32):
            string = "{}/{}".format(i, j)
            assert utils.is_date(string) is True

            if i < 10:
                string = "0{}/{}".format(i, j)
                assert utils.is_date(string) is True

            if j < 10:
                string = "{}/0{}".format(i, j)
                assert utils.is_date(string) is True


def test_range_data():
    assert utils.is_range('1...3') is False
    assert utils.is_range('1,,3') is False
    assert utils.is_range('1..3,,2') is False
    assert utils.is_range('1..3,a') is False
    assert utils.is_range('1..b,4') is False

    assert utils.is_range('1..10') is True
    assert utils.is_range('1..10,13') is True
    assert utils.is_range('1..10,13,20') is True


def test_command_line_interface():
    """Test the CLI."""
    # runner = CliRunner()
    # result = runner.invoke(cli.main)
    # assert result.exit_code == 0
    # assert 'what_the_num.cli.main' in result.output
    # help_result = runner.invoke(cli.main, ['--help'])
    # assert help_result.exit_code == 0
    # assert '--help  Show this message and exit.' in help_result.output
