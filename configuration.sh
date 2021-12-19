#git clone https://github.com/jlalus/phonemizer-docker
cd ~
git clone https://github.com/bootphon/phonemizer
cd phonemizer
python setup.py install
cp phonemizer-docker/Dockerfile phonemizer/Dockerfile
cp phonemizer-docker/app.py phonemizer/app.py


sudo docker build -t phonemizer .


