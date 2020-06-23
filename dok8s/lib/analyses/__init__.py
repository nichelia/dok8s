"""Analyses init
"""
from dok8s.lib.analyses.component_analysis import ComponentAnalyser
from dok8s.lib.analyses.docker_analysis import DockerAnalyser

ANALYSES = [
    ComponentAnalyser,
    DockerAnalyser,
]
