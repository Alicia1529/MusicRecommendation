# MusicRecommendation

Folder `/metadata` contains raw data from [Million Song Dataset](http://millionsongdataset.com)
  
Folder `/data` includes the different kinds of preprocessed by `/data_generator/*` to simulate normal cases and cold start problem.

To run Matrix Factorization model, run `python main.py` under folder `/mf`

To run [RippleNet](https://arxiv.org/pdf/1803.03467.pdf) model by 
```
$ cd kg
$ python preprocess.py --dataset <sub folder under /data>
$ python main.py --dataset <sub folder name /data>
```

To compare the two algorithms, run `python graph.py` under folder `/graph`
