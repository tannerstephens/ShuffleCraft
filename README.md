![ShuffleCraft](app/static/ShuffleCraft.png)

An unofficial Minecraft datapack generator to shuffle your recipes. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3.7.1

Using [pyenv](https://github.com/pyenv/pyenv)

`$ pyenv install 3.7.1`

Pip & Pipenv

`$ sudo apt install python3-pip`

`$ sudo pip3 install pipenv`


### Installing

Install python dependencies

`$ pipenv install`

Populate original_recipes

1. Open your prefered minecraft version, >=1.13, in a file explorer (7zip, winzip, etc...)
2. Navigate to `data/minecraft/recipes`
3. Create a folder in `app/shuffle/versions` with the name of your selected version (e.g. `app/shuffle/versions/1.13.2`)
4. Copy the contents of this folder to `app/shuffle/versions/<your_version>`

Run the dev server

`$ pipenv run python serve.py`

## Built With

* [Flask](http://flask.pocoo.org/) - Web Framework
* [Pipenv](https://docs.pipenv.org/en/latest/) - Dependency Management

## Authors

* **Tanner Stephens** - [tannerstephens](https://github.com/tannerstephens)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements

* [Mojang](https://mojang.com/)
* [Minecraft](https://minecraft.net/)
* [Textcraft](https://textcraft.net/)