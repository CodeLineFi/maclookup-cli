# MAC Address Vendor Lookup

MAC lookup CLI allows you to retrieve information about a MAC address or OUI
directly from your console including the vendor's name, address and other
data.  
The description of provided info is available in the API
[documentation](https://macaddress.io/api-documentation).

## Installation

```bash
$ pip install maclookup-cli
```

Specify the [-user](https://pip.pypa.io/en/stable/user_guide/#user-installs)
flag if you want the installation to be specific to the current user.  
In this case you'll have to make sure your **PATH** contains
`~/Library/Python/<ver>/bin`
([more info](https://gist.github.com/haircut/14705555d58432a5f01f9188006a04ed))
for **macOS** and `%AppData%\Python\Python<version>\Scripts` for **Windows**.

## API Key

Using this tool requires signing up for a
[macaddress.io](https://macaddress.io/) account and getting an API key
[here](https://macaddress.io/account/general).  
This key can either be specified via the `-k, --api-key` command option or
the *MAC_ADDRESS_IO_API_KEY* environment variable:

```bash
# macOS and Linux
export MAC_ADDRESS_IO_API_KEY="your-api-key"

# Windows (CMD)
set MAC_ADDRESS_IO_API_KEY="your-api-key"

# Windows (PowerShell)
$env:MAC_ADDRESS_IO_API_KEY="your-api-key"
```

You can add this to your *.bash_profile* for convenience:

```bash
echo 'export MAC_ADDRESS_IO_API_KEY="your-api-key"' >> ~/.bash_profile
``` 

## Getting Started

```bash
$ maclookup --help
```

### Basics

Just feed a MAC address to the command:

```bash
$ maclookup B8:C2:53:AC:DC:EF
```

This would print the complete information available for this address:

```bash
OUI: B8C253
Is private: False
Company name: Juniper Networks
Company address: 1133 Innovation Way Sunnyvale CA 94089 US
Country code: US
Left border: B8C2530000000000
Right border: B8C253FFFFFFFFFF
Block size: 1099511627776
Assignment block size: MA-L
Created at: 2018-10-26 00:00:00
Updated at: 2018-10-26 00:00:00
Transmission type: unicast
Administration type: UAA
```

### Multiple MACs

A list of addresses can be used as well:

```bash
$ maclookup -d B8C253ACDCEF DC4A3ED930C6
```

```bash
OUI: B8C253
Is private: False
Company name: Juniper Networks
Company address: 1133 Innovation Way Sunnyvale CA 94089 US
...
------------------------
OUI: DC4A3E
Is private: False
Company name: Hewlett Packard
Company address: 11445 Compaq Center Drive Houston 77070 US
...
```

The `-d` option separates info blocks with lines of dashes.

### Controlling the Output

You can limit the output to vendor names (`-V`) or MACs with vendors only (
`-mV`):

```bash
$ maclookup -V B8:C2:53:AC:DC:EF
Juniper Networks
```
```bash
$ maclookup -mV B8:C2:53:AC:DC:EF
B8:C2:53:AC:DC:EF - Juniper Networks
```

### Input Files

A text file containing one MAC address per line can also be used:

```bash
$ cat macs.txt 
C8:3A:35:5C:A6:80 
C4:0B:CB:19:1D:B0
BC:EE:7B:73:04:42
A4:17:31:79:1E:01
```

```bash
$ cat macs.txt | maclookup -mV
C8:3A:35:5C:A6:80 - Tenda Tech Co, Ltd
C4:0B:CB:19:1D:B0 - Xiaomi Communications Co Ltd
BC:EE:7B:73:04:42 - ASUSTek Computer Inc
A4:17:31:79:1E:01 - Hon Hai Precision Ind. Co, Ltd
```

You can specify the `-l` option to limit the number of MAC addresses to be
processed. The default value for this option is **100**. Use **0** to remove
the limit.

```bash
$ cat macs.txt | maclookup -mV -l 2
```

```bash
C8:3A:35:5C:A6:80 - Tenda Tech Co, Ltd
C4:0B:CB:19:1D:B0 - Xiaomi Communications Co Ltd
```

### Advanced Example

```bash
$ sudo nmap -sn 172.28.128.0/24|awk '/^MAC Address:/{print $3;}'|maclookup -mV
```
```bash
00:25:90:A4:8B:85 - Super Micro Computer, Inc
0C:C4:7A:40:07:09 - Super Micro Computer, Inc
0C:C4:7A:31:EF:8B - Super Micro Computer, Inc
00:25:90:FC:7A:CF - Super Micro Computer, Inc
00:25:90:2D:D4:01 - Super Micro Computer, Inc
```

## Error codes

Use the following to get the command's status code:

```bash
$ echo $?
```

|  Code  |          Description        |  Can be ignored (`-i`) |
|:------:|:---------------------------:|:----------------------:|
|   0    |         Success             |              -         |
|   1    | Authentication failed       |              -         |
|   2    | You don't have an access    |              -         |
|   3    |MAC address or OUI is invalid|              +         |
|   4    |You don't have enough credits|              -         |
|   5    |Cannot connect to the server |              -         |
|   6    |Cannot parse server response |              -         |
|  127   |         Other               |              -         |