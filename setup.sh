apt-get update
apt-get upgrade 
apt-get install python-dev
apt-get install ttf-unfonts-core
apt-get install python-pyaudio python3-pyaudio sox
apt-get install libatlas-base-dev libblas-dev liblapack-dev
apt-get install gfortran
pip install -U pip
pip install -r requirements.txt
pip install --upgrade gensim
file="./src/GeoLiteCity.dat"
if [ -f "$file" ]
then
    echo "$file already exist."
else
    cd src
    wget -N http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
    gzip -d GeoLiteCity.dat.gz
fi
