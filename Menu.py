import IpCalculator as ic
import SubnetCalculator as sc
import sys

def perfom_calculations():
    try:
        host_ip = ic.IpCalculator(input("Enter the Host IP: "))
        #host_ip = ic.IpCalculator('172.26.239.254') # Dummy Host IP for easy testing

        host_ip.calculate_decimal_ip()
        host_ip.convert_octects_to_binary()
        host_ip.get_ip_class()

        host_ip_mask = ic.IpCalculator(input("Enter the Subnet Mask: "))
        #host_ip_mask = ic.IpCalculator('255.255.254.0') # Dummy Mask IP for easy testing

        host_ip_mask.calculate_decimal_ip()
        host_ip_mask.convert_octects_to_binary()

        # Creates an object of SubnetCalculator
        subnet_information = sc.SubnetCalculator(host_ip, host_ip_mask)

        # Calculates all the information related to that IPv4
        subnet_information.calculate_all_values()

        # Prints the results
        print_results(host_ip, host_ip_mask, subnet_information)

        # Prints the subnet list
        subnet_information.print_subnets_list()

    except Exception as e:
        print(e)



def print_results(host_ip, host_ip_mask, subnet_information):
    """
    Displays all the information related to the given HostIPv4 and MaskIPv4
    :param host_ip: IpCalculator object of the HostIPv4
    :param host_ip_mask: IpCalculator object of the Given IPv4 Mask
    :param subnet_information: SubnetCalculator object which has the information
    :return:
    """
    print("+".ljust(40,'-')+"IP INFORMATION".ljust(53,'-')+"+")
    print("| Class : " + host_ip.ip_class[0])
    print("| Borrowed bits: " + str(subnet_information.borrowed_bits))
    print("| Available Subnets: " + str(subnet_information.available_subnets))
    print("| Subnet Index: " + str(subnet_information.subnet_index))
    print("| Host Bits: " + str(subnet_information.host_bits))
    print("| Available hosts: " + str(subnet_information.available_hosts))
    print("+-------------------+--------------------------+---------------------------------------------+")
    print("| Given Host ip".ljust(20) + "| Decimal: " + host_ip.ipv4.ljust(16) + "| Binary: " + '.'.join(
        host_ip.ip_binary_octects_list)+" |")
    print("| Given Subnet Mask".ljust(20) + "| Decimal: " + host_ip_mask.ipv4.ljust(16) + "| Binary: " + '.'.join(
        host_ip_mask.ip_binary_octects_list)+" |")
    print("| DSM".ljust(20) + "| Decimal: " + str(host_ip.ip_class[2]).ljust(16) + "| Binary: " + '.'.join(
        subnet_information.format_binary_8bit(str((host_ip.ip_class[1]))))+" |")
    print("| Network ID".ljust(20) + "| Decimal: " + '.'.join(subnet_information.subnet_id_decimal).ljust(16) + "| Binary: " + '.'.join(
        subnet_information.format_binary_8bit(subnet_information.subnet_id))+" |")
    print("| Broadcast  ip".ljust(20) + "| Decimal: " + '.'.join(subnet_information.broadcast_address_decimal).ljust(
        16) + "| Binary: " + '.'.join(subnet_information.format_binary_8bit(subnet_information.broadcast_address))+" |")
    print("| First Host ip".ljust(20) + "| Decimal: " + '.'.join(subnet_information.first_host_decimal).ljust(16) + '| Binary: ' + '.'.join(
        subnet_information.format_binary_8bit(str(subnet_information.first_host))) +" |")
    print("| Last Host  ip".ljust(20) + "| Decimal: " + '.'.join(subnet_information.last_host_decimal).ljust(16) + "| Binary: " + '.'.join(
        subnet_information.format_binary_8bit(str(subnet_information.last_host)))+" |")
    print("+-------------------+--------------------------+---------------------------------------------+")
    print("\n")
    

# Runs the menu
while True:
    print("\nc: calculate a new subnet")
    print("q: exit program")
    user_choice = input().upper()
    if user_choice == 'C':
        perfom_calculations()
    elif user_choice == 'Q':
        sys.exit()
