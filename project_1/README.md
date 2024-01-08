# project_1

This project is a practice. I want to use Rasa to create and edit worklfows on Apachi nifi.

# Train model

```
rasa train
```

# Run rasa after training

```
rasa run --enable-api
```

# config.yml

1. Copy the pipeline from an official example.

Must include the RegexFeaturizer and RegexEntityExtractor to support lookup.

```
- name: RegexEntityExtractor
  use_lookup_tables: True 
```

2. Copy the policies from an official example.

# nlu.yml

1. Add a new file "nifi_processor.yml" to keep the lookup "nifi_processor".

```
- lookup: nifi_processor
  examples: |
    - ExtractTNEFAttachments
    - QueryDatabaseTable
	...
```

2. Add an intent to create an nifi processor "create_processor".

```
- intent: create_processor
  examples: |
    - Create a [GetFile]{"entity":"nifi_processor"} processor.
    - Add one [EncryptContent] {"entity":"nifi_processor"}.
    - Give me a [PutFile] {"entity":"nifi_processor"}.
```


# domain.yml

1. Add the new intent to the domain.

2. Add an entity.

```
entities:
  - nifi_processor
```

2. Add a slot to keep the processor name.

```
slots:
  nifi_processor_name: 
    type: text
    influence_conversation: false
    mappings:
    - type: from_entity
      entity: nifi_processor
```

# story.yml

1. Add a story for processor creation.

```
- story: ask_to_create_processor
  steps:
  - intent: create_processor
  - action: utter_confirm
```