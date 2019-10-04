#!/home/ec2-user/venv/python3/bin/python

__author__ = ['[Gerald Sim](https://github.com/meappy)']
__date__ = '2019.10.04'
__version__ = "1.0.0"

"""
Deploy AWS CloudFormation
"""

import sys
import json
import fire
import subprocess

cform_file = 'launch-web.yaml'
param_file = 'params/launch-web.json'

# https://bit.ly/2pjBDUd
# https://bit.ly/2otFmOT
def read_param(param_index, param_name='ParameterValue'):
    with open(param_file) as param:
        data = json.load(param)
        return (data[param_index][param_name])

def run(x, silent=True):
    if __name__ == '__main__':
        return fire.Fire(x)

stack_name = (run(read_param))

# https://bit.ly/2AM43sp
# https://bit.ly/2AFiXRn
cmd='aws --profile default cloudformation create-stack \
    --stack-name %s \
    --parameters file://params/launch-web.json \
    --template-body file://launch-web.yaml' % (stack_name).rstrip()

push=subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)
push.wait()
print(push.returncode)
