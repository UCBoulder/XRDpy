from setuptools import setup
from pathlib import Path
import shutil
import yaml
import XRDpy.package_params as package

detector_dir = package.directory / "detectors"
detector_dir.mkdir(parents=True, exist_ok=True)
for det_file in Path("files").glob("*.h5"):
    shutil.copyfile(det_file, detector_dir / det_file.name)
with open(package.directory / "config.yaml", "w") as f:
    yaml.dump({"data_path": package.data_path.as_posix()}, f)

setup(
    name="XRDpy",
    version='1.0',
    packages=["XRDpy", "XRDpy.incident"],
    scripts=["XRDpy/main.py",],
    py_modules=["XRDpy.transform"],
    entry_points = {
        "console_scripts": [
            "XRD-film=XRDpy.main:film",
            "XRD-stitch=XRDpy.main:stitch",
            # "XRD-default=XRDpy.main:default",
            "XRD-imacro=XRDpy.incident.main:make",
            "XRD-imove=XRDpy.incident.main:move",
            "XRD-iplot=XRDpy.incident.main:plot",
        ],
    },
    # data_files=[(str(install_dir), [str(Path("files") / "1 3 detector.h5")])],
    install_requires=[
        "numpy",
        "matplotlib",
        "pyFAI",
        "fabio",
        "gixpy",
        "pyside6",
        "pyopencl"
    ],
)