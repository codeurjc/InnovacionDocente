if [ -z "$(docker images -q innovacion-docente 2> /dev/null)" ]; then
  docker build -f _dockerfiles/Dockerfile -t innovacion-docente .
fi

docker run --rm -d -p 8888:8888 -v $PWD:/home/jovyan/work/ innovacion-docente