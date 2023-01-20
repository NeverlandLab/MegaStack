FROM python:3.10.9
WORKDIR /opt

ADD ./apps ./apps
ADD ./MegaStack ./MegaStack
ADD ./static ./static
ADD ./staticfiles ./staticfiles
ADD ./templates ./templates
ADD ./manage.py ./manage.py
ADD ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt  -i https://mirrors.cloud.tencent.com/pypi/simple
RUN python ./manage.py collectstatic --noinput