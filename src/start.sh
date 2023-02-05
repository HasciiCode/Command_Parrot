ENVIROMENT="env"
CURRENT=$(cd $(dirname $0);pwd)

source "$CURRENT"/"$ENVIROMENT"/bin/activate
python3 main.py