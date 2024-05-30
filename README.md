# Repo for working with Python in HUST

## Generate requirements.txt 

Requirements for each folder is managed by pipreqs:
```sh
pip install pipreqs
```

Pipreqs documents can be found in this [Github Repo](https://github.com/bndr/pipreqs).


## Use Python virtual environments

Create a virtual environment:
```sh
python -m venv <environment-name>
```

Activate the virtual environment
```sh
<environment-name>/scripts/activate
```

## Install dependencies

To run the contents in this repository, please install the dependencies listed in [requirements.txt](/requirements.txt) by running:

```sh
pip install -r <path-to-requirements.txt>
```

To execute Python notebook, ipykernel package is required:
```
pip install ipykernel
```