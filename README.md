# dicom-filter

dicom-filter is a package which allows the user to check which DICOM JSON files in a directory/subdirectory match a specified list of key-value pairs.

## Installing dicom-filter

To install dicom-filter:

```bash
python3 -m pip install dist/dicom_filter_dschulz-0.0.1-py3-none-any.whl
```

## Using dicom-filter

Once installed:

```bash
dcm_filter --keys={keys} --values={values} {directory}
```

Example:

```bash
dcm_filter --keys="00080005,00080016" --values="ISO_IR 100,1.2.840.10008.5.1.4.1.1.1.1" ./example-data/
```
