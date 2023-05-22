# labels: test_group::monthly,daily author::microsoft name::swin-base-patch4-window7-224-in22k downloads::6,434 license::apache-2.0 task::Computer_Vision sub_task::Image_Classification
from transformers import AutoFeatureExtractor, SwinForImageClassification
from PIL import Image
import requests

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

feature_extractor = AutoFeatureExtractor.from_pretrained("microsoft/swin-base-patch4-window7-224-in22k")
model = SwinForImageClassification.from_pretrained("microsoft/swin-base-patch4-window7-224-in22k")

inputs = feature_extractor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits
# model predicts one of the 1000 ImageNet classes
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
