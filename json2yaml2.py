#!/usr/bin/env python3
import json
import yaml
import argparse
import sys

class CustomDumper(yaml.SafeDumper):
  def represent_scalar(self, tag, value, style=None):
    if isinstance(value, str) and '\n' in value:
      # Decide whether to use folded or literal style
      if self._safe_to_fold(value):
        style = '>'
      else:
        style = '|'
    return super().represent_scalar(tag, value, style)

  def _safe_to_fold(self, value):
    """
    Determine if folded style is safe for the given string.
    Folded style is unsafe if any line starts with a YAML indicator.
    """
    problem_prefixes = ('-', '?', ':', ',', '[', ']', '{', '}',
                        '&', '*', '#', '|', '>', '!', '%', '@', '`')
    lines = value.split('\n')
    for line in lines:
      stripped_line = line.lstrip()
      if stripped_line and stripped_line[0] in problem_prefixes:
        return False
    return True

def json_to_yaml(input_file, output_file):
  try:
    if input_file == '-':
      data = json.load(sys.stdin)
    else:
      with open(input_file, 'r') as f:
        data = json.load(f)

    if output_file == '-':
      yaml.dump(data, sys.stdout, Dumper=CustomDumper,
                default_flow_style=False, allow_unicode=True)
    else:
      with open(output_file, 'w') as f:
        yaml.dump(data, f, Dumper=CustomDumper,
                  default_flow_style=False, allow_unicode=True)

    if input_file != '-' and output_file != '-':
      print(f"Successfully converted {input_file} to {output_file}", file=sys.stderr)
  except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)

def main():
  parser = argparse.ArgumentParser(description='Convert JSON to YAML.')
  parser.add_argument('input', nargs='?', default='-',
                      help='Input JSON file (default: stdin)')
  parser.add_argument('output', nargs='?', default='-',
                      help='Output YAML file (default: stdout)')
  args = parser.parse_args()
  json_to_yaml(args.input, args.output)

if __name__ == '__main__':
  main()          
#fin
