"""Commands init
"""
from dok8s.cli.commands.component import ComponentCommand
from dok8s.cli.commands.docker import DockerCommand

COMMANDS = [
    ComponentCommand,
    DockerCommand,
]
