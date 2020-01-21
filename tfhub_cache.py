import tensorflow as tf
import tensorflow_hub as hub
import os

module_url = os.environ["TFHUB_MODULE_URL"]
print(f"Caching: {module_url}...")
embed = hub.KerasLayer(module_url)
print("Caching complete")

# embed = hub.KerasLayer(module_url)
# embeddings = embed(["A long sentence.", "single-word", "http://example.com"])
# print(embeddings.shape)  #(3,128)