FROM ubuntu:latest
FROM python:3.12-slim
LABEL authors="yuvan"

ENTRYPOINT ["top", "-b"]

# 设置工作目录
WORKDIR /gmgn

# 复制依赖文件并安装依赖
COPY requirements.txt /gmgn/
RUN pip install --no-cache-dir -r requirements.txt

# 复制所有源代码到容器
COPY . /gmgn/

# 设置容器启动时执行的命令
CMD ["tail", "-f", "/dev/null"]