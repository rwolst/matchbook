try:
    from matchbook.apiclient import APIClient
    from matchbook.exceptions import MBError
except ModuleNotFoundError:
    # Issue occurs that we want the version before installing dependencies
    # causing issues in the setup.py.
    pass


__title__ = 'matchbook'
__version__ = '0.0.7'
