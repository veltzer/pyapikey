import config.project

package_name = config.project.project_name

test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
]
dev_requires = [
    "pypitools",
    "pydmt",
    "pyclassifiers",
    "pymakehelper",
]

python_requires = ">=3.9"
test_os = ["ubuntu-20.04"]
test_python = ["3.9"]
