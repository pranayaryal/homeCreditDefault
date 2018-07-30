# homeCreditDefault
Kaggle's home credit default competition.

Run using docker for Python 3.0 environment

Run:
```
docker -t homecred:latest build .
```
This will build using the dockerfile

Once the image is built run it using:

```
docker run --rm -p 10000:8888 -e JUPYTER_LAB_ENABLE=yes -v "$PWD":/home/jovyan/work homecred:latest
```
