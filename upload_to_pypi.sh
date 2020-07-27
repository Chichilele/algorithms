# activate venv
source /Users/gauthier.castro/Code/algorithms/venv/bin/activate
# update setuptools and wheel
python3 -m pip install --upgrade setuptools wheel
# create package artefacts
python3 setup.py sdist bdist_wheel
# update twine (package uploader)
python3 -m pip install --upgrade twine

# upload package to testpypi repo
# use the following credentials:
#   username: __token__
#   password: [API TOKEN]
python3 -m twine upload --repository testpypi dist/*
