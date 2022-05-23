# INSECURE

Insecure is a tool for the discovery of leaks, relevant information on email addresses and social networks. This tool is based on the https://github.com/saeeddhqan project, licensed under the GPL 3.0.

I am using it as a project to hone my Python skills

# DISCLAIMER

I want to make it clear, this is a rework of maryam and it is nothing more than a modification of its code if you want to see the original code go to: https://github.com/saeeddhqan/Maryam

# Install

### Supported OS
 - Linux
 - FreeBSD
 - OSX

### Prerequisites
 - Python 3.8.x or 3.9.x (NOT 3.7, ...)
 - requests module

```bash
git clone https://github.com/natone2/insecure.git
cd insecure
pip install -r requirements
python3 insecure.py -e help
```

## Tips

```bash
# Using dns_search. --max means all of resources. --api shows the results as json.
# .. -t means use multi-threading.
python 3 insecure.py -e dns_search -d ibm.com -t 5 --max --api --form 
# Using youtube. -q means query
python3 insecure.py -e youtube -q "<QUERY>"
python3 insecure.py -e google -q "<QUERY>"
python3 insecure.py -e dnsbrute -d domain.tld
# Show the framework modules
python3 insecure.py -e show modules
# Set framework options. It'll save in the workspace.
python3 insecure.py -e set proxy ..
python3 insecure.py -e set agent ..
python3 insecure.py -e set timeout ..
```
