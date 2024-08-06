# url_builder

The url_builder is a tool that builds a URL using a JSON file as an input.

In the terminal, we would run the following command:

```sh
$ python open_file.py your_dictionary_object.json 
```

The url_builder is a program that uses the JSON file containing a dictionary with arguments such as the scheme, hostname, port, path, and parameters. 

Here's an example of the dictionary JSON object! 😃
```python
# your_dictionary_object.json
{
        "scheme": "ftp",
        "hostname": "github.com",
        "port": "288",
        "path": "alexa-ngo",
        "params": {"explore":  "coding", "school": "3", "interest": "exercise"}
}
```

So if the scheme argument is missing, the url_builder will use HTTPS by default. If the hostname is missing, an error will be raised. Additionally, if the scheme is either HTTP or HTTPS, and if the port number is either 80 or 443, the port number will not be displayed in the URL. Other than that, if other arguments are missing the constructed URL will be reflective of that. 


After we run the command for the sample dictionary object, this following URL will be returned in your terminal! 

```bash
ftp://github.com:288/alexa-ngo?explore=coding&school=3&interest=exercise
```

So give it a try! 😊