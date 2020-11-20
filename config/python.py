import config.project

package_name = config.project.project_name

console_scripts = [
]

setup_requires = [
]

test_requires = [
    'pylint',
    'pytest',
    'pytest-cov',
    'flake8',
]

install_requires = [
]

dev_requires = [
    'pypitools',
    'pydmt',
    'pyclassifiers',
    'pymakehelper',
]

python_requires = ">=3.6"

extras_require = {
}
