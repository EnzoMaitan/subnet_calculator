import SubnetCalculator as sC
import IpCalculator as iC


class SubnetListCalculator:
    subnet_calculator: sC
    available_subnets: int
    borrowed_bits: int
    current_index = 0

    def __init__(self, subnet_calculator, borrowed_bits, available_subnets):
        self.subnet_calculator = subnet_calculator
        self.borrowed_bits = borrowed_bits
        self.available_subnets = available_subnets

    def calculate_new_network_address(self, network):
        """Receive an IPv4 Address and Adds 1 to the borrowed zone"""

        # Creates an Object of Ip calculator
        new_SID = iC.IpCalculator('.'.join(network))

        # Gets the IP information in different formats of the current Subnet Network Address
        new_SID.convert_octects_to_binary()
        new_SID.calculate_decimal_ip()
        new_SID.get_ip_class()

        # Gets the current borrowed part
        borrowed_zone = ''.join(new_SID.ip_binary_octects_list)[new_SID.ip_class[3]:(new_SID.ip_class[3]+ self.borrowed_bits)]

        # Adding + 1 to the borrowed part
        new_borrowed_zone = format(int(borrowed_zone, 2) + 1,'0' + str(self.borrowed_bits)+'b')

        # Sets the current index of the subnet to the class variable
        self.current_index = int(new_borrowed_zone, 2)

        # Add the new borrowed zone to the rest of the IP
        new_SID.ipv4 = ''.join(new_SID.ip_binary_octects_list)[:new_SID.ip_class[3]] + new_borrowed_zone

        # Fill the host portion with Zeroes
        new_SID.ipv4 = new_SID.ipv4.ljust(32, '0')

        # Convert the binary IPV4 into a decimal dotted format
        first_octet = str(int(new_SID.ipv4[:8], 2))
        second_octet = str(int(new_SID.ipv4[8:16], 2))
        third_octet = str(int(new_SID.ipv4[16:24], 2))
        fourth_octet = str(int(new_SID.ipv4[24:], 2))
        new_SID.ipv4 = '.'.join([first_octet, second_octet, third_octet, fourth_octet])

        return new_SID.ipv4

    def calculate_all_subnets(self):
        """Calculates and displays all the possible Subnet networks
            It displays Index, Network Address, First Host IP, Last Host IP and Broadcast Address
        """

        print("Possible Networks / Showing " + str(self.available_subnets))
        print("+---------+-----------------+-----------------+-----------------+-------------------+")
        print("|  Index  | Network Address | First Host IP   | Last Host IP    | Broadcast Address |")
        print("+---------+-----------------+-----------------+-----------------+-------------------+")

        network_ipv4 = ".".join(self.subnet_calculator.calculate_first_index())

        for x in range(0, self.available_subnets):
            # Creates an Object of Ip calculator
            new = iC.IpCalculator(network_ipv4)

            # Gets the IP information in different formats of the current Subnet Network Address
            new.calculate_decimal_ip()
            new.convert_octects_to_binary()

            # Converts the IP to a list string format
            network_ipv4 = [str(i) for i in new.ip_decimal_octects_list]

            # Creates an object that will calculate the information(BA, FH, LH) of the Subnet Network Address
            new_calculator = sC.SubnetCalculator(new, self.subnet_calculator.host_ip_mask)

            # Calculates the information related to the current Subnet Network Address
            new_calculator.subnet_id = ''.join(new.ip_binary_octects_list)
            new_calculator.calculate_broadcast_address()
            new_calculator.calculate_first_host()
            new_calculator.calculate_last_host()
            new_calculator.calculate_decimal_values()

            # Prints the formatted result
            print("| "+str(self.current_index).rjust(7)+" | " + '.'.join(new_calculator.subnet_id_decimal).ljust(15) + " | " + '.'.join(
                new_calculator.first_host_decimal).ljust(15) + " | " + '.'.join(new_calculator.last_host_decimal).ljust(
                15) + " | " + '.'.join(new_calculator.broadcast_address_decimal).ljust(18) + "|")

            # Calculates the next network address IP (Increasing 1 to the borrowed zone until it's full)
            network_ipv4 = self.calculate_new_network_address(network_ipv4)
        print("+---------+-----------------+-----------------+-----------------+-------------------+")
