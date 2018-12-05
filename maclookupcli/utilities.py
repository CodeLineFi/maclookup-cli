import sys
import os
from maclookup import exceptions
from maclookupcli.errors import *


def read_macs_from_stdin():

    '''
    Reads MAC addresses from STDIN

    :return: list of MAC addresses
    '''

    macs = []

    if not sys.stdin.closed:
        macs = sys.stdin.readlines()
    sys.stdin.close()
    return macs


def print_full_info(model, original_mac, separator):

    '''
    Outputs full info about given mac address

    :param model: maclookup.models.ResponseModel
    :param original_mac: The mac address
    :param separator: Boolean flag. When true it will print a string separator
    :return:
    '''

    if not sys.stdout.closed:
        if separator is True:
            sys.stdout.write(str('-' * 24) + os.linesep)

        if model.block_details.block_found is True:
            sys.stdout.write(u"OUI: {}{}".format(get_str(model.vendor_details.oui), os.linesep))
            sys.stdout.write(u"Is private: {}{}".format(get_str(model.vendor_details.is_private), os.linesep))
            sys.stdout.write(u"Company name: {}{}".format(get_str(model.vendor_details.company_name), os.linesep))
            sys.stdout.write(u"Company address: {}{}".format(get_str(model.vendor_details.company_address), os.linesep))
            sys.stdout.write(u"Country code: {}{}".format(get_str(model.vendor_details.country_code), os.linesep))
            sys.stdout.write(u"Left border: {}{}".format(get_str(model.block_details.border_left), os.linesep))
            sys.stdout.write(u"Right border: {}{}".format(get_str(model.block_details.border_right), os.linesep))
            sys.stdout.write(u"Block size: {}{}".format(get_str(model.block_details.block_size), os.linesep))
            sys.stdout.write(u"Assignment block size: {}{}".format(
                get_str(model.block_details.assignment_block_size),
                os.linesep
            ))
            sys.stdout.write(u"Created at: {}{}".format(get_str(model.block_details.date_created), os.linesep))
            sys.stdout.write(u"Updated at: {}{}".format(get_str(model.block_details.date_updated), os.linesep))
            sys.stdout.write(u"Transmission type: {}{}".format(
                get_str(model.mac_address_details.transmission_type),
                os.linesep
            ))
            sys.stdout.write(u"Administration type: {}{}".format(
                get_str(model.mac_address_details.administration_type),
                os.linesep
            ))
        else:
            sys.stdout.write("Not found" + os.linesep)


def print_vendor(model, original_mac, separator, mac_with_vendor):

    '''
    Outputs only vendor's name.

    :param model: maclookup.models.ResponseModel
    :param original_mac: The mac address
    :param separator: Boolean flag. When true it will print a string separator
    :param mac_with_vendor: Boolean flag. Changes output format to <mac> - <vendor_name>
    :return:
    '''

    if not sys.stdout.closed:
        if separator is True:
            sys.stdout.write(str('-' * 24) + os.linesep)

        if mac_with_vendor:
            sys.stdout.write("{} - ".format(original_mac.strip()))

        if model.block_details.block_found is True:
            sys.stdout.write(u"{}{}".format(get_str(model.vendor_details.company_name), os.linesep))
        else:
            sys.stdout.write("Not found" + os.linesep)


def make_request(mac, client):

    '''
    Perform an API request

    :param mac:
    :param client:
    :return:
    '''

    try:
        return client.get(mac)
    except exceptions.AuthorizationRequiredException:
        print('{}: You need to specify a valid API key'.format(mac))
        raise FatalError(1)

    except exceptions.AccessDeniedException:
        print('{}: You do not have an access to the API'.format(mac))
        raise FatalError(2)

    except exceptions.InvalidMacOrOuiException:
        print('{}: MAC address or OUI looks to be invalid'.format(mac))
        raise IgnorableError(3)

    except exceptions.NotEnoughCreditsException:
        print('{}: You are out of credits'.format(mac))
        raise FatalError(4)

    except exceptions.ServerErrorException:
        print('{}: Could not connect to the server'.format(mac))
        raise FatalError(5)

    except exceptions.UnparsableResponseException:
        print('{}: Server response is invalid'.format(mac))
        raise FatalError(6)

    except Exception:
        print('{}: Unknown error'.format(mac))
        raise FatalError(127)


def get_str(s):
    # helper function for the python 2.x
    try:
        return unicode(s)
    except NameError:
        pass
    return str(s)
