# phonemizer-docker

We use linux-server.iso (preinstalled OpenSSH, GIT and Docker)

Run the application:

git clone https://github.com/jlalus/phonemizer-docker

chmod 744 phonemizer-docker/configuration.sh

./phonemizer-docker/configuration.sh


The index.html page is the server test page. In order to test the docker, complete the AJAX queries with the Server IP address.
Then add a few words to the list (type one word -> add to list). Then send the query to the server and wait for the reply.


If you want check logs from docker app use:

sudo docker inspect --format='{{.LogPath}}' PhonemizerApp | xargs sudo cat >  ~/phonemizer/out.log
