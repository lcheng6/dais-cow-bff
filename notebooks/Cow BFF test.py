# Databricks notebook source
# MAGIC %pip install -r ../requirements.txt
# MAGIC %load_ext autoreload
# MAGIC %autoreload 2
# MAGIC

# COMMAND ----------

import pytest
import sys

# Skip writing pyc files in case it is on a readonly filesystem.
sys.dont_write_bytecode = True

# Run pytest.
retcode = pytest.main(["../tests", "-v", "-p", "no:cacheprovider"])

# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."


# COMMAND ----------


