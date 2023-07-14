import banana_dev as client
from io import BytesIO
from PIL import Image
import base64

my_model = client.Client(
    api_key="",
    model_key="",
    #Test locally via:
    # docker build -t auto .
    # docker run --gpus=all -p 8000:8000 auto
    url="http://localhost:8000",
    # url="https://....run.banana.dev",
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
result, meta = my_model.call("/txt2img", inputs)
# print(result)
base64_output = result["output"]
image_encoded = base64_output.encode('utf-8')
image_bytes = BytesIO(base64.b64decode(image_encoded))
image = Image.open(image_bytes)
image.save("output.jpg")

