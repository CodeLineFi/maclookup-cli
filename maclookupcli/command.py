import click
from maclookup import ApiClient
from maclookupcli.utilities import *
from maclookupcli.errors import *

ENV_API_KEY = 'MAC_ADDRESS_IO_API_KEY'

HELP_API_KEY = '''
Your API key. 

Also, it can be specified as env variable:

export {}="your-api-key"

'''.format(ENV_API_KEY)

HELP_LIMIT = '''
Maximum allowed number of MACs to be processed. Default: 100.

Use 0 to disable limitation.

'''

HELP_VENDOR = '''
Show only the vendor name.
Without this option the command will output multiline MAC or OUI description.

'''

HELP_DELIMITER = '''
Add a string delimiter to the output.

-------------------------------------

'''

HELP_MAC_WITH_VENDOR = '''
Change output format to: <mac> - <vendor_name>. (Only with -V option).

'''

HELP_IGNORE_ERROR = '''
Ignore Invalid MAC or OUI error.

'''


@click.command()
@click.argument('macs', nargs=-1, required=False)
@click.option('-k', '--api-key', 'api_key', envvar=ENV_API_KEY,
              required=True, type=str, help=HELP_API_KEY)
@click.option('-l', '--limit', 'limit', required=False, type=int, default=100,
              help=HELP_LIMIT)
@click.option('-V', '--only-vendor', 'vendor', required=False, is_flag=True,
              default=False, type=bool, help=HELP_VENDOR)
@click.option('-d', '--delimiter', 'separator', required=False, is_flag=True,
              default=False, type=bool, help=HELP_DELIMITER)
@click.option('-m', '--mac-with-vendor', 'mac_with_vendor', required=False, is_flag=True,
              default=False, type=bool, help=HELP_MAC_WITH_VENDOR)
@click.option('-i', '--ignore-errors', 'ignore_errors', required=False, is_flag=True,
              default=False, type=bool, help=HELP_IGNORE_ERROR)
def cli(macs, api_key, limit, vendor, separator, mac_with_vendor, ignore_errors):
    '''
        MACs: List of MAC addresses. Also you can input your MACs to the STDIN, one per line.

    Example:

    $ macaddress-info -mV f4:0f:24:36:da:57

    f4:0f:24:36:da:57 - Apple, Inc

    $
    '''
    client = ApiClient(api_key)
    if not isinstance(macs, tuple) or len(macs) == 0:
        macs = read_macs_from_stdin()

    count = 0
    for mac in macs:
        if count >= limit and limit > 0:
            break

        count += 1

        try:
            model = make_request(str(mac).strip(), client)
        except IgnorableError as error:
            if ignore_errors:
                continue
            else:
                exit(error.code)

        except FatalError as error:
            exit(error.code)

        if vendor:
            print_vendor(model, mac, separator, mac_with_vendor)
        else:
            print_full_info(model, mac, separator)
