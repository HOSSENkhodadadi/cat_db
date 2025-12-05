import os
import warnings
os.environ["SPARK_HOME"] = "spark-3.5.3-bin-hadoop3/"
os.environ["PYSPARK_PYTHON"] = "python"
print('done')
from catdb import config, create_report, generate_pipeline, prepare_dataset
from dataprofiling import build_catalog

# cfg = config(model="gpt-4o", API_key="...", iteration=7)
# cfg = config(model="llama-3.3-70b-versatile", API_key="...", iteration=7)
cfg = config(model="gemini-2.0-flash", API_key="AIzaSyAHKEelBGwSmTof2okcAlIZOm-peYTFUBE", iteration=5)
# from catdb import config, create_report, generate_pipeline, prepare_dataset
# from dataprofiling import build_catalog

# cfg = config(model="gpt-4o", API_key="...", iteration=5)

data = prepare_dataset(path="content/adult.csv", task_type="binary", target_attribute="income")

catalog = build_catalog(data=data, categorical_ratio=0.05, n_workers=1 ,max_memory=10)

pipeline = generate_pipeline(catalog, cfg)

print("%"*50)
print(data)
print("%"*50)
print(catalog)
print("%"*50)
print(pipeline)