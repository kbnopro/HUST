# Repo for working with Python in HUST

<!-- Table of content  -->


## 1. Use Python virtual environments

#### Create a virtual environment:
```sh
python -m venv <environment-name>
```

#### Activate the virtual environment
```sh
<environment-name>/scripts/activate
```


## 2. Install global dependencies
```sh
pip install -r requirements.txt
```


## 3. Install project dependencies

To run the contents in this repository, please install the dependencies listed in [requirements.txt](/requirements.txt) in each project by running:

```sh
pip install -r <path-to-requirements.txt>
```
quirements.txt 

Requirement for each project is  managed by [pipreqs](https://github.com/bndr/pipreqs):
```sh
pip install pipreqs
```
