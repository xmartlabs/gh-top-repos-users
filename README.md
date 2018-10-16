# gh-top-repos-users

It downloads the contributors of the top 5000 repos (by star count).

## Run locally

With Python 3 and pip:

```shell
pip install -r requirements.txt
```

Then run:

```shell
GH_TOKEN=YOUR_TOKEN scrapy crawl topreposusers -o output/output.json
```

## With Docker

```shell
docker build -t gh-top-repos-users .

docker run \
    --rm \
    -v $PWD/output:/usr/src/app/output \
    -e "GH_TOKEN=YOUR_TOKEN" \
    -t \
    -i \
    gh-top-repos-users
```
