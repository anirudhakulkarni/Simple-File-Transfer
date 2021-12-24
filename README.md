# Simple-File-Transfer

## Dependencies
1. ngrok
2. python3
3. curl

## Steps:
### Server side
1. install ngrok & setup ngrok free account
2. copy `server.py` to the directory where files will be uploaded
3. start server with `python3 server.py`
4. expose server to internet with ngrok with `ngrok http 8080`
5. copy ngrok url shown on terminal. example url: http://49e8-103-40-199-45.ngrok.io 

### Client side
1. upload file to ngrok address with `curl -F "filename=@test.json" NGROK_URL`
example: `curl -F "filename=@test.json" http://49e8-103-40-199-45.ngrok.io`

### Related work
Similar steps can be used for server in php. Follow exact steps with `upload.php` instead of `server.py` as above except add /upload.php in ngrok url before sending curl request.
example: `curl -F "filename=@test.json" http://49e8-103-40-199-45.ngrok.io/upload.php`

### Why:
1. To automate download process on colab notebook or kaggle notebooks where output files are cleared after execution
2. To transfer files from terminals where ftp/scp access is blocked. Worked with one of the firms where I worked.
