### Potassium/Banana Implementation

This repository is the implementation of [stable-diffusion-webui](!https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/v1.3.1/modules/api/api.py) with support for Negative Embeddings

### Endpoints

At the moment only one endpoint is implemented.

- `/txt2img` is the implementation of stable-diffusion-webui `/sdapi/v1/txt2img` api.

  Json Input

  ```JSON
  {
      "body": {
          "params": {
              "prompt": "CAT",
              "negative_prompt": "low quality",
              "steps": 25,
              "sampler_name": "Euler a",
              "cfg_scale": 7.5,
              "seed": 42,
              "batch_size": 1,
              "n_iter": 1,
              "width": 400,
              "height": 400,
              "tiling": 'false',
          }
      }
  }
  ```

  OUTPUT:

  ```JSON
  {
      "output": "<base64 image>"
  }
  ```

### Client Implementation in Python

```Python
import banana_dev as client

my_model = client.Client(
    api_key="[API_KEY]",
    model_key="[MODEL_KEY]",
    url="[MODEL_URL]",
)

inputs = {
    "params": {
        "prompt": "a girl with long black hair wearing a white shirt and red bow tie, a character portrait, by Muqi, reddit post, sadness look, black hair in braids, dark hallway, red uniform, concerned, visual novel sprite, extremely long forehead, 3 pm, cute scene, wearing tight shirt, female protagonist, red rain, full shot photo",
        "negative_prompt": "EasyNegative, text, close up, cropped, out of frame, worst quality, artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face",
        "steps": 40,
        "sampler_name": "Euler a",
        "cfg_scale": 7.5,
        "seed": 1339,
        "batch_size": 1,
        "n_iter": 1,
        "width": 512,
        "height": 512,
        "tiling": "false",
    }
}

# Call your model's inference endpoint on Banana.
# If you have set up your Potassium app with a
# non-default endpoint, change the first
# method argument ("/")to specify a
# different route.
result, meta = my_model.call("/text2img", inputs)
print(result)
```

### Negative Embeddings

WITHOUT negative embeddings called via negative prompt
![alt text](outputNoNE.jpg)

WITH negative embeddings called via negative prompt
![alt text](outputWithNE.jpg)
