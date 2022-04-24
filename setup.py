import setuptools

setuptools.setup(
    entry_points = {
        'console_scripts': ['dcm_filter=dicom_filter.dicom_filter:cli'],
    },
    name="dicom-filter-dschulz",
    version="0.0.1",
    author="Daniel Schulz",
    author_email="schulzy.d@gmail.com",
    description="Package for filtering DICOM files",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
