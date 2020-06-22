"""command_init_test
"""
from dok8s.cli.commands import COMMANDS


def test_commands():
    """test_commands
    """
    assert [C().name for C in COMMANDS] == [
        "component",
    ]
