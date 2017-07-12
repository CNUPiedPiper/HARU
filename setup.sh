echo y | command

apt-get update
apt-get -y upgrade 
apt-get install -y python-dev python-setuptools swig
apt-get install -y ttf-unfonts-core
apt-get install -y python-pyaudio python3-pyaudio sox
apt-get install -y libatlas-base-dev libblas-dev liblapack-dev
apt-get install -y gfortran
apt-get install -y build-essential scons

pip install -U pip pip install -r requirements.txt
pip install --upgrade gensim

geo_data="./src/GeoLiteCity.dat"
if [ -f "$geo_data" ]
then
    echo "$geo_data already exist."
else
    cd src
    wget -N http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
    gzip -d GeoLiteCity.dat.gz
fi

wiring_pi="./WiringPi-Python"
if [ -f "$wiring_pi" ]
then
    echo "$wiring_pi already exist."
else
    git clone --recursive https://github.com/neuralpi/WiringPi-Python.git
    cd WiringPi-Python/WiringPi
    wget https://raw.githubusercontent.com/neuralassembly/raspi/master/wp-pwm-warning.patch
    patch -p2 -i wp-pwm-warning.patch
    sudo ./build
    cd ..
    swig2.0 -python wiringpi.i
    sudo python setup.py install
fi

led_pi="./rpi_ws281x"
if [ -f "$led_pi" ]
then
    echo "$led_pi already exist."
else
    git clone https://github.com/jgarff/rpi_ws281x.git
    cd rpi_ws281x
    scons
    cd python
    python setup.py install
fi

echo "Haru perfectly installed !" 
