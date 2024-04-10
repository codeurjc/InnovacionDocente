FROM jupyter/minimal-notebook:notebook-7.0.3

RUN pip install --upgrade pip

USER jovyan

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /home/jovyan/work/

CMD ["jupyter-notebook", "--notebook-dir=/home/jovyan/work/", "--ip='0.0.0.0'", "--port=8888","--NotebookApp.token=''","--allow-root"]

# BUILD docker build -f dockerfiles/Dockerfile -t innovacion-docente .