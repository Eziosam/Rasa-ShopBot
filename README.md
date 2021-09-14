# Rasa Shop Bot

This is a sample shopping bot to help customers buy products from e-commerce sites. Built using Rasa 2.8.5 and Rasa x 0.39.3

## Install dependencies

Run:

First create an virtual environment in anaconda prompt using the command : 
```bash
conda create -n rasavirtualenv python = 3.6
```
Activate your environment using the command :
```bash
conda activate rasavirtualenv
```

Install latest rasa version:
```bash
pip3 install rasa
```
or install speicific version 2.8(if any error occurs with latest one)
```bash
pip3 install rasa==2.8.5
```

Install Rasa X:
```bash
pip3 install rasa-x==0.39.3 --extra-index-url https://pypi.rasa.com/simple
```

## Run the bot

Use `rasa train` to train a model.
Use `rasa shell` to talk with the bot(console).
Use `rasa x` to talk with the bot(browser).

For custom actions, first set up your action server in one terminal window:
```bash
rasa run actions
```

For entity extraction,  run the duckling server (In another window):
```bash
docker run -p 8000:8000 rasa/duckling
```

TO talk to your bot and debug at the same time:
```
rasa shell --debug
```

Note that , If you get errors follow these:
1. For c++ 14 related error : Install [MS Visual Studio Build Tools] (https://www.scivision.dev/python-windows-visual-c-14-required)
2. If Rasa doesn't start:
First: 
```
pip3 install SQLAlchemy==1.3.22
```
If it still doesn't launch:
Delete rasa.db and events.db files (only first time)


## Overview of the files

`data/stories.yml` - contains stories

`data/nlu.yml` - contains NLU training data


`data/rules.yml` - contains the rules upon which the bot responds to queries

`actions/actions.py` - contains custom action/api code

`domain.yml` - the domain file, including bot response templates

`config.yml` - training configurations for the NLU pipeline and policy ensemble

`tests/test_stories.yml` - end-to-end test stories


## Things you can ask the bot

1. Ask if a product is available or not.
2. Ask how many product in stock,price of product,view products by shop ,category or price range.
3. Add Product in Cart
4. Subscribe to product updates

Note: This project is still in development all features aren't implemented yet. Be patient.

