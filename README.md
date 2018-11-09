# MAC address vendor lookup

MAC lookup CLI allows you to retrieve information about MAC address or OUI 
directly from your console. You can get a vendor's name and vendor's address.
The list of all provided information is available on the API documentation 
[page](https://macaddress.io/api-documentation).

## Preparation

To use this tool you need to create an account on [macaddress.io](https://macaddress.io/)
On the site, you can get your API key. When these steps have been taken, 
specify the key as an environment variable, something like this:

```bash
export MAC_ADDRESS_IO_API_KEY="your-api-key"
```

You can add this to your *.bash_profile* file:

```bash
echo 'export MAC_ADDRESS_IO_API_KEY="your-api-key"' >> ~/.bash_profile
``` 

## Get started

Good! Now you are ready to start using command line tool for MAC vendor 
lookups. Let's first start with the easiest example:

```bash
$ maclookup B8:C2:53:AC:DC:EF
OUI: B8C253
Is private: False
Company name: Juniper Networks
Company address: 1133 Innovation Way Sunnyvale  CA  94089 US
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

As you can see, there is full info about the block of MAC addresses printed 
to the standard output. Be careful, as the "Created at" means the date when 
we got that block info for the first time. The "Updated at" refers to the 
date when we got the last update for this block.


May be you need to get info about multiple MAC addresses, let's consider the
next example:

```bash
$ maclookup -d B8:C2:53:AC:DC:EF 7C:60:4A:AA::3E:65
------------------------
OUI: B8C253
Is private: False
Company name: Juniper Networks
Company address: 1133 Innovation Way Sunnyvale  CA  94089 US
Country code: US
Left border: B8C2530000000000
Right border: B8C253FFFFFFFFFF
Block size: 1099511627776
Assignment block size: MA-L
Created at: 2018-10-26 00:00:00
Updated at: 2018-10-26 00:00:00
Transmission type: unicast
Administration type: UAA
------------------------
OUI: 7C604A
Is private: False
Company name: Avelon
Company address: Bändliweg 20 Zurich    8048 CH
Country code: CH
Left border: 7C604A0000000000
Right border: 7C604AFFFFFFFFFF
Block size: 1099511627776
Assignment block size: MA-L
Created at: 2018-10-26 00:00:00
Updated at: 2018-10-26 00:00:00
Transmission type: unicast
Administration type: UAA

```

Take a look at this useful `-d` option. This option adds a string of dashes 
before each block of information.


Sometimes, you need to get just a vendor's name, which is possible by means 
of the `maclookup` command. Just add two more options:

```bash
$ maclookup -V B8:C2:53:AC:DC:EF
Juniper Networks
$ maclookup -mV B8:C2:53:AC:DC:EF
B8:C2:53:AC:DC:EF - Juniper Networks
```

Now you are ready to use this tool in a wild world. For example, you may use 
`maclookup` with `nmap`:

```bash
$ sudo nmap -sn 172.28.128.0/24 | awk '/^MAC Address:/ {print $3;}' \
> | maclookup -mV
00:25:90:A4:8B:85 - Super Micro Computer, Inc
0C:C4:7A:40:07:09 - Super Micro Computer, Inc
0C:C4:7A:31:EF:8B - Super Micro Computer, Inc
00:25:90:FC:7A:CF - Super Micro Computer, Inc
00:25:90:2D:D4:01 - Super Micro Computer, Inc
```

or just a text file with one MAC address per line:

```bash
$ cat macs.txt 
C8:3A:35:5C:A6:80 
C4:0B:CB:19:1D:B0
BC:EE:7B:73:04:42
A4:17:31:79:1E:01
$ cat macs.txt | maclookup -mV
C8:3A:35:5C:A6:80 - Tenda Tech Co, Ltd
C4:0B:CB:19:1D:B0 - Xiaomi Communications Co Ltd
BC:EE:7B:73:04:42 - ASUSTek Computer Inc
A4:17:31:79:1E:01 - Hon Hai Precision Ind. Co, Ltd
```

What if your text file contains too many lines? In this case, you need to use 
the `-l` option to limit the number of MAC addresses to be processed.

```bash
$ cat macs.txt | maclookup -mV -l 2
C8:3A:35:5C:A6:80 - Tenda Tech Co, Ltd
C4:0B:CB:19:1D:B0 - Xiaomi Communications Co Ltd
```

The default value for this option is 100. You can use zero value to remove 
the limit.


## Error codes

You can use the following command to get the status code.

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
