# must be run in the parent jobapp dir
export RDS_DB_NAME=zl_local
export RDS_USERNAME=nanjpkgd
export RDS_PASSWORD=eecs99retour
export RDS_HOSTNAME=zldblocal.c6uwtwcozuqn.us-west-2.rds.amazonaws.com
export RDS_PORT=3306
CURRDIR=$(pwd)
export PYTHONPATH=$CURRDIR:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=jobapp.settings