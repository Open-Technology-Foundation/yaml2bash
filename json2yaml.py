#!/usr/bin/env python3
import json
import yaml
import argparse
import sys

def setup_yaml():
  """Configure YAML to use folded style for multiline strings."""
  def folded_unicode_representer(dumper, data):
    style = '>' if '\n' in data else None
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style=style)

  yaml.add_representer(str, folded_unicode_representer)

def json_to_yaml(input_file, output_file):
  try:
    if input_file == '-':
      data = json.load(sys.stdin)
    else:
      with open(input_file, 'r') as f:
        data = json.load(f)

    if output_file == '-':
      yaml.dump(data, sys.stdout, default_flow_style=False)
    else:
      with open(output_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

    if input_file != '-' and output_file != '-':
      print(f"Successfully converted {input_file} to {output_file}", file=sys.stderr)
  except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)

def main():
  parser = argparse.ArgumentParser(description='Convert JSON to YAML.')
  parser.add_argument('input', nargs='?', default='-', help='Input JSON file (default: stdin)')
  parser.add_argument('output', nargs='?', default='-', help='Output YAML file (default: stdout)')
  args = parser.parse_args()
  setup_yaml()
  json_to_yaml(args.input, args.output)

if __name__ == '__main__':
  main()
  
#fin
