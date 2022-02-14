#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "Restaurant-Management-System"
default_task = "publish"
version= "1.0"


@init
def set_properties(project):
    project.set_property('pdoc_source', 'src/main/python')
    project.set_property('pdoc_output_dir','/docs')
    project.set_property('pdoc_module_name', 'src.main.python')
    project.set_property('pdoc_command_args',['--html'])
    project.set_property("coverage_break_build", False) 
