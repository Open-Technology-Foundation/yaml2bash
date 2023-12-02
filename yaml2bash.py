#!/usr/bin/python3
"""
Extract variables from a yaml file, and output
eqivalent `Bash` declare statements for each variable
into a list `yaml2bash(yaml_file):list`, or to stdout
if run from command line.

Script will take YAML files as input then output
equivalent Bash declare statements for each variable
to stdout.
"""
import sys
import yaml

def to_bash(variable, value):
  """
  Convert Python data structure into Bash declare statements.
  """
  if isinstance(value, str):
    # Strings are enclosed in double quotes
    return f'declare -- {variable}="{value}"'
  if isinstance(value, int):
    # Integers are declared directly
    return f'declare -i {variable}={value}'
  if isinstance(value, bool):
    # Booleans are declared directly (0 for False, 1 for True)
    return f'declare -ix {variable}={int(value)}'
  if value is None:
    # None is declared as an empty string
    return f'declare -- {variable}=""'
  if isinstance(value, float):
    # Floats are declared as strings (because Bash doesn't support floats)
    return f'declare -- {variable}="{value}"'
  if isinstance(value, list):
    # indexed arrays
    array_elements = " ".join(f'"{str(elem)}"' for elem in value)
    return f'declare -a {variable}=( {array_elements} )'
  if isinstance(value, dict):
    # associative arrays
    assoc_array_elements = " ".join(f'[{k}]="{v}"' for k, v in value.items())
    return f'declare -A {variable}=( {assoc_array_elements} )'
  raise TypeError(f"Unsupported type for Bash declare: {type(value)}")

def yaml2bash(yaml_file:str) ->list:
  """
  This function will take a YAML file as input
  and output equivalent Bash declare statements for each
  variable, returned as a list.
  """
  # Load the YAML file
  with open(yaml_file, 'r', encoding='utf-8') as file:
    parsed_yaml = yaml.safe_load(file)

  # Process Bash declare statements
  declares:list=[]
  for key, val in parsed_yaml.items():
    declares.append(to_bash(key, val))
  return declares

# For script mode.
if __name__ == "__main__":
  if len(sys.argv) <= 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print('usage: yaml2bash file.yaml [file.yaml...]', file=sys.stderr)
    sys.exit(1)
  decl:list=[]
  for arg in sys.argv[1:]:
    decl = yaml2bash(arg)
    for arg in decl:
      print(arg)

#fin
