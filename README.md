# scripts
Repository for scripts in bash and python. 


## Dynamic DNS Script
A script for dynamically updating web servers ip address with google domains

### Usage 
Make sure you install the requirements in `requirements.txt` and set necessary environment variables in a `.env` file.

```bash
pip install -r requirements.txt
python ddns-update.py
```

### Environment Variables
```
DDNS_USERNAME=<username given by google>
DDNS_PASSWORD=<password given by google>
GOOGLE_HOSTNAME=<should be domains.google.com>
PERSONAL_HOSTNAME=<personal hostname registered with google domains, can also be subdomain>
```