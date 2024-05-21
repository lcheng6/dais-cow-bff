# Databricks notebook source
# MAGIC %md
# MAGIC ## First we install Python packages and initialize our globals

# COMMAND ----------

# MAGIC %pip install -r ../requirements.txt
# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

# load table into spark dataframe
cows_bff = spark.read.table("db.cows_bff")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Lets compute meal overlap

# COMMAND ----------

from cow_bff.heatmap import compute_heatmap

df = compute_heatmap(cows_bff)
display(df.limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC # Display Heatmap

# COMMAND ----------

pdf = df.toPandas()
pdf = pdf.pivot(index='cow1', columns='cow2', values='distance').fillna(0)

import plotly.express as px
fig = px.imshow(pdf, x=pdf.columns, y=pdf.index, labels=dict(x="Cow 2", y="Cow 1", color="Distance"), title="Cow BFFs", color_continuous_scale='redor')
px.imshow(pdf, x=pdf.columns, y=pdf.index, labels=dict(x="Cow 2", y="Cow 1", color="Distance"),)

fig.update_layout(width=800,height=500)
fig.show()

# COMMAND ----------

# DBTITLE 1,Verify with notebook viz
display(df)

# COMMAND ----------


