#!/usr/bin/env python
import xmltodict
import yaml
import argparse
import sys

def convert_xml_to_yaml(xml_file_path, yaml_file_path):
  try:
    with open(xml_file_path, 'r', encoding='utf-8') as xml_file:
      xml_content = xml_file.read()
    xml_dict = xmltodict.parse(xml_content)
    
    with open(yaml_file_path, 'w', encoding='utf-8') as yaml_file:
      yaml_content = yaml.dump(xml_dict, sort_keys=False, allow_unicode=True)
      yaml_file.write(yaml_content)
    
    print(f"Successfully converted '{xml_file_path}' to '{yaml_file_path}'.")
  except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

def main():
  parser = argparse.ArgumentParser(description='Convert XML file to YAML file.')
  parser.add_argument('xml_file', help='Path to the input XML file')
  parser.add_argument('yaml_file', help='Path to the output YAML file')
  
  args = parser.parse_args()
  
  convert_xml_to_yaml(args.xml_file, args.yaml_file)

if __name__ == '__main__':
  main()
  