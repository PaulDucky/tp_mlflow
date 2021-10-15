import os
import click
import pandas as pd
import mlflow
import mlflow.pyfunc
import mlflow.tracking
from mlflow.utils import mlflow_tags
from foodcast.domain.forecast import plotly_predictions
from foodcast.application.mlflow_utils import get_run, mlflow_log_pandas, mlflow_log_plotly
from foodcast.settings import LOGGING_CONFIGURATION_FILE  # type: ignore
import yaml
import logging
import logging.config
with open(LOGGING_CONFIGURATION_FILE, 'r') as f:  # to import
    logging.config.dictConfig(yaml.safe_load(f.read()))  # to import
