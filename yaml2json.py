#!/usr/bin/python3
"""
Extract variables from yaml file, and output to json.
"""
import sys
import json
import yaml

def yaml2json(yaml_file):
  """
  This function will take a YAML file as input
  and export json to stdout.
  """
  # Load the YAML file
  with open(yaml_file, 'r', encoding='utf-8') as file:
    parsed_yaml = yaml.safe_load(file)
  # Convert the parsed YAML to JSON
  print(json.dumps(parsed_yaml, indent=2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    yaml2json(sys.argv[2])

#fin
