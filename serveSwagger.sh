# install dependency
# npm install -g http-server
# docker pull swaggerapi/swagger-ui
# Usage: serveSwagger.sh /Path/to/your/swaggerFile/Folder

echo "swagger ui web will host at http://127.0.0.1:7070"
echo "access the static swagger file at http://127.0.0.1:7071/yourSwaggerFileName.json(or .yml)"

SWAGGER_FOLDER_PATH="$1"

echo "docker container id:"
docker run -d -p 7070:8080 swaggerapi/swagger-ui
cd $SWAGGER_FOLDER_PATH
http-server -p 7071 --cors
