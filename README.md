# Mock SFTP server

This repository is a simplified test version of a server that was used to mock the functionalities of an actual remote SFTP server.

The interaction with the original mocked server was as follows:

1. Open SFTP connection
2. Add a file named _filename_id.json_, where _filename_ is predefined and the id unique.
3. Wait for the server to create a response file, named _response_filename.json_, where _response_filename_ is predefined.
4. Fetch the response file
5. Delete the request file (created at step 2) from the server.

**_This repository does not include the functionalities to interact with the server but implements the functionality of the server itself._**

## Starting the server

1. Clone the repository
2. Run `docker compose up -d` (-d for detached mode) to start the application

## Testing the server

To test the server, you need to connect to it using SFTP. You can use ready-made SFTP libraries, or use a GUI tool such as [WinSCP](https://winscp.net/eng/index.php).

```
Host: localhost
Port: 2222
Username: user
Password: pass
folderpath: /upload
```

After you have established SFTP connection, adding a new file to the upload folder will trigger creating a new response file. The filename is in format "Response\_{original_filename}.json". The folder is also mounted to the sftp_data folder at the root of the cloned repository, so any files added to the SFTP server and the created response files will appear there.

Please note that any json file with a name starting with "Response\_" will be ignored to avoid creating an infinite loop.
