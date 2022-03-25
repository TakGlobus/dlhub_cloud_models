"""
A template for creating a DLHub-compatible description of a model.

The places where you need to fill in information are marked with "TODO" comments
"""

# TODO: Import a metadata template appropriate for your type of model
#  See:
from dlhub_sdk.models.servables.python import PythonStaticMethodModel
from dlhub_sdk.utils.schemas import validate_against_dlhub_schema
from dlhub_sdk.models.servables.tensorflow import TensorFlowModel
from dlhub_sdk.client import  DLHubClient
import json

# Read in model from disk
# TODO: Fill in options specific to this type of model
#model_info = PythonStaticMethodModel.create_model('TensorFlowModel.create_m', 'model_syn')
model_info = TensorFlowModel.create_model("./decoder-10021600")

# Define the name and title for the model
model_info.set_title("Decoder part of RI autoencoder trained on 1M MODIS patches from 2000-2020")
model_info.set_name("clouds_RI_encoder")

# TODO: Verify authors and affiliations
model_info.set_creators(["Kurihana , Takuya "], [["University of Chicago"]])

model_info.set_version("v1.0.0")

# TODO: Describe the scientific purpose of the model
model_info.set_domains(["climate science", 'MODIS', 'satelite imagery'])

# FIXME: append set_abstract triggers "TypeError: Object of type DataciteDescriptionType is not JSON serializable"
#model_info.set_abstract("Rotational-invariant (RI) autoencoder that Kurihana et al. 2021 \
#    works with 6 selected bands of MODIS021KM/MYD021KM products. \
#    Upscale the size of training set from 70,000 to 1M patches sampled from the period 2000--2020, and used to Kurihana et al. 2022.")

# TODO: Add references for the model
model_info.set_doi("DOI: 10.1109/TGRS.2021.3098008")  # Example: Paper describing the model

# TODO: Describe the computational environment
# Basic route: Add a specific Python requirement
# model.add_requirement('numpy', 'detect')
# Advanced: Include repo2docker config files in submission
# model.parse_repo2docker_configuration()  # You can specify a different path for config files

# TODO: Describe the inputs and outputs of the model
#  This is not required for some model types (e.g., TensorFlow), delete if needed
#model_info.set_inputs('string', 'Your name')
#model_info.set_outputs('string', 'A greeting: "Hello <your name>!"')

# Check the schema against a DLHub Schema
validate_against_dlhub_schema(model_info.to_dict(), 'servable')

# Save the metadata
with open('dlhub.json', 'w') as fp:
    json.dump(model_info.to_dict(), fp, indent=2)

# Publish model
client = DLHubClient()
taskid = client.publish_servable(model_info)
print(taskid)

