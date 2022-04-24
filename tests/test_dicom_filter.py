import json
import os
import pytest

from src.dicom_filter.dicom_filter import dicom_filter

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/test_dicom.json'), 'r') as f:
  example_dicom = json.load(f)

@pytest.mark.parametrize(
    "dicom,filter_criteria,expected",
    [
        (example_dicom, [("00080005", "ISO_IR 100"), ("00080016", "1.2.840.10008.5.1.4.1.1.1.1")], True),
        (example_dicom, [("00080005", "ISO_IR 72"), ("00080016", "1.2.840.10008.5.1.4.1.1.1.1")], False),
    ],
)
def test_dicom_filter(dicom, filter_criteria, expected):
    assert dicom_filter(dicom, filter_criteria) == expected
