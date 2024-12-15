#/usr/bin/python3
from dataclasses import dataclass
from typing import List
import yaml

@dataclass
class SRmSpec(object):
    srm_name: str
    redistributable: bool
    built_on: List[str]

    build_spec: 'BuildSpec'

@dataclass
class BuildSpec(object):
    type: str
    options: 'BuildOptions'

@dataclass
class BuildOptions(object):
    pass

@dataclass
class BuildOptionsBuildscript(BuildOptions):
    script: str
    output_location: str

class SrmBuilder(object):
    def go():
        TARGET_SPEC="../specs/physlock.yml"
        
    
