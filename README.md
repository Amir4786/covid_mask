loss= 22.02%
accuracy= 92.00%


# Mask Wear Detection

Covid-19 has been affecting the whole world and to abate it some necessary precautions are crucial to follow these precautions come with guidelines. From having social distancing to avoiding physical contact many steps has been taken so far but we humans can’t live like that however some precautions can be followed as long as possible to avoid Covid and wearing face mask is one of them. Public places like hospitals, malls, offices, schools etc are serious about Covid as there are more chances to spread and to avoid it social distancing and mask wearing are mandatory. For a person it is quite challenging to check masks on faces of each individual present at the public place but not for the machine and to make a machine intelligent enough to detect masks here this project comes with Convolution Neural Network technique using Artificial Intelligence to detect whether a person is wearing mask or not in real time.


## Acknowledgements

 - [GitHUB Repository](https://github.com/Amir4786/covid_mask)

## Appendix

Deep Learning technology using Computer vision CNN to detect covid-19 mask on faces in a real time video. 

## Authors

- [Amir Khan](https://github.com/Amir4786/)
- [Fazlullah Bokhari](https://github.com/FazlullahBokhari/)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## Configuration Setup

#### Command to the whole setup from scratch

#### For Virtual Environment and Requirements installation

```
  bash init_setup.sh
```



#### Activate the Environment

```
  conda activate ./env
```


#### Data Preprocessing Step

```
  python src//covid_md//pipeline//stage_01_data_preprocessing.py
```


#### Data Training Step

```
  python src//covid_md//pipeline//stage_02_data_training.py
```


#### Mask Detection Step

```
  python src//covid_md//pipeline//stage_03_mask_detection.py
```


## DVC

#### Used to know the Model Flow

#### To initialize DVC

```
  dvc init
```
#### To know dvc status
```
  dvc status
```

#### To run the Pipeline

```
  dvc repro
```
