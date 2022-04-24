import argparse
import glob
import json

def dicom_filter(dicom, filter_criteria):
  """Takes in a DICOM dictionary and a list of filter criteria and checks to
  whether the DICOM matches the filter criteria.

  Args:
      dicom (dict): The DICOM
      filter_criteria (list): A list of filter criteria pairs (key, value)

  Returns:
      bool: True if DICOM matches filter criteria, else False
  """

  for x in filter_criteria:
    if x[0] in dicom:
      if dicom[x[0]]['Value'][0] != x[1]:
        return False

  return True

def cli():
  """Parses the filter criteria keys, and values, and the directory from the
  command line and applies the dicom_filter function to each JSON file in the
  directory/subdirectiories. Prints the path of files whos DICOM matches the
  filter criteria.
  """
  parser = argparse.ArgumentParser()
  parser.add_argument("--keys", help="")
  parser.add_argument("--values", help="")
  parser.add_argument("directory", help="")
  args = parser.parse_args()

  keys = args.keys.split(",")
  values = args.values.split(",")
  directory = args.directory

  filter_criteria = list(zip(keys, values))
  filepaths = [x for x in glob.glob(f'{directory}**/*.json', recursive=True)]

  matches = []
  for filepath in filepaths:
    with open(filepath) as f:
      dicom = json.loads(json.loads(f.read()))

      if dicom_filter(dicom, filter_criteria):
        matches.append(filepath)

  for match in matches:
    print(match)

if __name__ == "__main__":
  cli()
