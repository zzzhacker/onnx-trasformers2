# onnx_transformers2 
![onnx_transformers2](https://github.com/zzzhacker/onnx-trasformers2/blob/main/onnx-transformers2.png?raw=True)
> Accelerated NLP pipelines for fast inference 🚀 on CPU AND GPUS. Built with 🤗Transformers Pipeline and ONNX runtime.

## Installation:

```bash
pip install git+https://github.com/zzzhacker/onnx-trasformers2.git
```

## Usage:

> *NOTE* : This is an Project going under development currenlty working with pytorch 4.5.x

- The pipeline API is similar to transformers [pipeline](https://huggingface.co/transformers/main_classes/pipelines.html) with just a few differences which are explained below.

- Just provide the path/url to the model and it'll download the model if needed from the [hub](https://huggingface.co/models) and automatically create onnx graph and run inference.

- You can Also Specify the onnx output graph as 'onnx_output_dir' parameter

```python
from onnx_transformers2 import pipeline

# Initialize a pipeline by passing the task name and 
# set onnx to True (default value is also True)
>>> nlp = pipeline("sentiment-analysis", onnx=True)
>>> nlp("Transformers and onnx runtime is an awesome combo!")
[{'label': 'POSITIVE', 'score': 0.999721109867096}]  
```

Or provide a different model using the `model` argument.

```python
from onnx_transformers import pipeline

>>> nlp = pipeline("question-answering", model="deepset/roberta-base-squad2", onnx=True)
>>> nlp({
  "question": "What is ONNX Runtime ?", 
  "context": "ONNX Runtime is a highly performant single inference engine for multiple platforms and hardware"
})
{'answer': 'highly performant single inference engine for multiple platforms and hardware', 'end': 94, 'score': 0.751201868057251, 'start': 18}
```

Set `onnx` to `False` for standard torch inference.

You can create `Pipeline` objects for the following down-stream tasks:

 - `feature-extraction`: Generates a tensor representation for the input sequence
 - `ner`: Generates named entity mapping for each word in the input sequence.
 - `sentiment-analysis`: Gives the polarity (positive / negative) of the whole input sequence. Can be used for any text classification model.
 - `question-answering`: Provided some context and a question referring to the context, it will extract the answer to the question in the context.
 - `fill-mask`: Provide sentence with mask token and in will get words predictions for fill the blank or mask token.
  

Calling the pipeline for the first time loads the model, creates the onnx graph, and caches it for future use. Due to this, the first load will take some time. Subsequent calls to the same model will load the onnx graph automatically from the cache.


The key difference between HF pipeline and onnx_transformers is that the `model` parameter should always be a `string` (path or url to the saved model).

#### Credits
I built this on top of @patil-suraj  [onnx_transformers](https://github.com/patil-suraj/onnx_transformers) repo to extend it to support more pipelines
