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
  current_processor_name: 
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

# Use the info saved in the slot.
1. Add a "slot_was_set" step to the story.

```
- story: ask_to_create_processor
  steps:
  - intent: create_processor
  - slot_was_set: 
    - current_processor_name: PutCassandraRecord
  - action: utter_confirm
```

2. Add the slot into the response:

```
  utter_confirm:
  - text: "OK. I'm to create a {current_processor_name}..."
```

# How to finish a story with API visits.

1. Append a message to a conversation by posting to "/{conversation_id}/messages".

Method: POST

URL example:
http://localhost:5005/conversations/11/messages

Body example:
```
{
    "text": "Give me one SplitXml.",
	"sender": "user"
}
```

The api should return the intent. 

2. Take the intent to "/{conversation_id}/predict" to predict the next event.

Method: POST

URL example:
http://localhost:5005/conversations/11/predict

Body empty

The return should have a list of actions and scores.

3. Take the choosen action to "/{conversation_id}/execute"

Method: POST

URL example:
http://localhost:5005/conversations/11/execute

Body example:
```
{
	"name": "utter_confirm"
}
```

The return contains the output message.