FROM python:3.6

WORKDIR /server

ADD DjangoBlog/requirements.txt /server/

# RUN pip install git+https://github.com/Supervisor/supervisor
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# USER ebrose

EXPOSE 80 8000 443