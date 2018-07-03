# install dependency
# npm install -g http-server
# docker pull swaggerapi/swagger-ui

echo "swagger ui web will host at port http://127.0.0.1:7070"
echo "access the static swagger file at port http://127.0.0.1:7071"

SWAGGER_FOLDER_PATH = $1
docker run -d -p 7070:8080 swaggerapi/swagger-ui
cd $SWAGGER_FOLDER_PATH
http-server -p 7071 --cors
