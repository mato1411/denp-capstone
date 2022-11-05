# US Immigrations, Demographics and Airports

The project focuses on the provision of a database containing United States (US) immigration from 2016, city demographics from 2015 and airport data for data analysts, statisticians or researcher within that field.

This Github repository was submitted as Capstone Project as part of this program.

## Requirements
* Python 3.6+
* Jupyter notebooks
* Pandas
* Pyspark (local installation, but AWS EMR recommended)
* AWS S3 (optional, but recommended due to the proessing duration)

## Data Directory Tree
```
data
├── cleaned
│   ├── airport_pq
│   ├── demographic_pq
│   └── immigration
│       ├── complete_pq
│       ├── sample_csv_pq
│       └── sample_month_pq
├── processed
│   ├── d_us_airports_pq
│   ├── d_us_demographics_pq
│   ├── d_visitors_pq
│   ├── immigration_complete
│   │   └── f_us_immigrations_pq
│   ├── immigration_data_dict
│   │   ├── I94ADDR.json
│   │   ├── I94CIT_I94RES.json
│   │   ├── I94MODE.json
│   │   ├── I94PORT.json
│   │   └── I94VISA.json
│   ├── immigration_sample_csv
│   │   └── f_us_immigrations_pq
│   └── immigration_sample_month
│       └── f_us_immigrations_pq
└── raw
    ├── 18-83510-I94-Data-2016
    │   ├── i94_apr16_sub.sas7bdat
    │   ├── i94_aug16_sub.sas7bdat
    │   ├── i94_dec16_sub.sas7bdat
    │   ├── i94_feb16_sub.sas7bdat
    │   ├── i94_jan16_sub.sas7bdat
    │   ├── i94_jul16_sub.sas7bdat
    │   ├── i94_jun16_sub.sas7bdat
    │   ├── i94_mar16_sub.sas7bdat
    │   ├── i94_may16_sub.sas7bdat
    │   ├── i94_nov16_sub.sas7bdat
    │   ├── i94_oct16_sub.sas7bdat
    │   └── i94_sep16_sub.sas7bdat
    ├── airport-codes.csv
    ├── global-land-temperature-by-city-sample.csv
    ├── GlobalLandTemperaturesByCity.csv
    ├── I94_SAS_Labels_Descriptions.SAS
    ├── immigration_data_sample.csv
    └── us-cities-demographics.csv
```

The raw datasets are stored in `data/raw`. The US immigration dataset `data/raw/18-83510-I94-Data-2016` and world temperature dataset `data/raw/GlobalLandTemperaturesByCity.csv` are not provided. They either need to be downloaded from Udacity workspace or from the source.

The cleaned data will be stored in `data/cleaned`. 

The data processed represents the data pipelined in into the chosen data model.

Any directory name containing `pq` stores data in Apache parquet format.

## Configurations
The following constants can be edited as required. They are part of the [Jupyter Notebook](us_immigration_census.ipynb) (one of the first cells).
```
# Set this to True, if Udacity workspace is used. For Udacity workspace symlinks will be created automatically
UDACITY_WS = True
# Set this to True, if data is stored on S3
S3 = False
# Set this to True, to use only a sample file for world temparature dataset
SAMPLE_TEMPERATURE = True
# Set this to True, to use only a sample file for US immigration dataset
SAMPLE_IMMIGRATION = True
# Set this to True, to use only a single month file for US immigration dataset
SAMPLE_IMMIGRATION_SAS = False
```

The other constants define the data directory tree as illustrated in [here](#data-directory-tree).

## Processing of sample data only
When running the ETL pipeline on a single-node Spark instance locally or within the Udacity workspace it's useful to process only a subset of data. Additionally, you might want to avoid downloading the large dataset. Hence, for the World Temperature and I94 immigration dataset are sample files provided within this repository. Using the samples will reduce the runtime of the ETL pipeline. Please adapt the [configuration constants](#configurations) as required.

## How to run the ETL

The ETL is outlined and implemented in the [Jupyter Notebook](us_immigration_census.ipynb).

### Udacity Workspace
To run the [Jupyter Notebook](us_immigration_census.ipynb) in Udacity workspace set the constants `UDACITY_WS = True` insides the notebook. The workspace already has the requirements installed and datasets are provided.

### Local 
1. To run the notebook anywhere else, install the requirements of this project.
1. The small datasets are provided within this repository in `data/raw/`. The larger ones need to be downloaded manually. In order to avoid downloading the large dataset, sample files are provided (see [Processing of sample data only](#processing-of-sample-data-only)).
1. Download the I94 immigration dataset SAS files from the udacity workspace or from the source. Create a new directory `data/raw/18-83510-I94-Data-2016` on S3 and copy the downloaded I94 immigration dataset SAS files to it.
1. Download the `GlobalLandTemperaturesByCity.csv` file from the udacity workspace. Store the file in the directory `data/raw`.

### Optional - Use AWS:
1. Open the `dl.cfg` file and replace ***** with your specific AWS parameters: AWS Access Key and Secret (parameter KEY and SECRET in section AWS)
1. Create a AWS EMR instance with Spark and adapt the Spark configuration in [Jupyter Notebook](us_immigration_census.ipynb)
1. Preparations in order to use S3 instead of the local or udacity workspace filesystem:
    1. Open `utils.py` and define S3 bucket name as variable `S3_BUCKET_NAME`
    1. Run `python -u utils.py -c` to create the S3 bucket
    1. Create the directory `raw` on S3 and copy the files from `data/raw` to the bucket
    1. Create a new directory `data/raw/18-83510-I94-Data-2016` on S3 and copy the I94 immigration dataset SAS files to it.
    1. Store the file `GlobalLandTemperaturesByCity.csv` in the directory `data/raw` on S3.
    1. Open the Jupyter Notebook and ensure that the constants `S3 = True` is set to use S3
    1. After running the Jupyter notebook, if you wish to delete the S3 bucket, run `python -u utils.py -d`.


## Additional files:
* `utils.py`: Script that creates and deletes the S3 bucket, run `python -u utils.py -h` to display the help of the CLI
* `dl.cfg`: Configuration of AWS credentials

## License & Disclaimer
The datasets where provided by Udacity. The original sources have been linked within the Jupyter Notebook. This data engineering project was done for personal educational purposes only.
