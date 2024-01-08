# rasa_space
A practice of rasa NLU.

## Environment

Rasa doesn't support Python later than 3.9. It's a good idea to prepare the environment with Anaconda and install Rasa there. I created "RASA_env".

All the operations to Rasa can be committed on Anaconda prompt. Choose the environment on Anaconda prompt with this command:

```
conda activate RASA_env
```

## Install Rasa

```
pip3 install rasa
``` 

## How to create a new project.

This command can create a new Rasa project. 

```
rasa init
```

## How to run the project.

It is recommended to open the api at the start.

```
rasa run --enable-api
```


